# -*- coding: utf-8 -*-
"""
Example functions for processing mongo tracks
"""

from haversine import haversine
from shapely.geometry import Point, Polygon
import numpy as np
from bisect import bisect_right
from datetime import datetime
from time import time
from pymongo import MongoClient
from functools import partial
import pickle
import numpy as np
from collections import Counter
import json
import argparse

from par_batch_map.batch_map import batch_map, run_mongo_query_processing
from par_batch_map.utils import *


def process_example(level, track):
    for _ in range(level):
        5 * 5
    track.update({"CAT_62": {}})
    track.update({"airline": track["callsign"][:3]})
    return track

def process_track(track,
                  airport_config={},
                  base_category="CAT_21",
                  additional_categories=["CAT_62"],
                  features={},
                  lag_first=600,
                  lag_last=0,
                  step=10):

    """
    Function for post-processing one track from database to create features to ML

    Parameters
    ----------
    track : dict
        track from database
    airport_config : dict
        configuration of airport
    base_category : str
        base category of track, to which additional categories was joined (default "CAT_21" - "ADS-B")
    additional_categories : list
        list of categories joined with base categories, default only "CAT_62" - "tracker"
    features : dict
        dict of features to extract from each category
    lag_first: int
        number of seconds before landing to extract output track points
    lag_last: int
        number of seconds before landing as output track last point
    step: int
        number of seconds between subsequent track points
    """

    def preprocess_filter(track):
        if all(map(lambda cat: track.get(cat) is not None, additional_categories)):
            for cat in additional_categories:
                track[cat] = track[cat] if type(track[cat]) == list else [track[cat]]
            return track
        return None

    def count_landing_time(track):

        def get_landing_time(track_simple):
            runway_border = Polygon(airport_config["runway_border"])
            on_runway = lambda x: runway_border.contains(Point(x[1][0], x[1][1]))
            idx = next(filter(on_runway, enumerate(track_simple["LatLon"]["coordinates"])),
                   (None, None))[0]
            if idx is None:
                return None
            return int(track_simple["created"] + track_simple["LatLon_timestamp"][idx])

        def check_landing_times(times, base_time):
            if all(map(lambda t: t is None, times)):
                return None
            difs = list(map(lambda t: abs(t - base_time) if t is not None else 100000, times))
            if min(difs) <= 10:
                return np.argmin(difs)
            return None

        def update_track(cat, index, base_land):
            if index is not None:
                track.update({cat: track[cat][index]})
                track[cat]["landing"] = base_land
                track[cat]["landing_timestamp"] = base_land - int(track[cat]["created"])
            else:
                track.update({cat: None})

        base_land = get_landing_time(track)
        if base_land is None:
            return None
        new_indexes = map(lambda cat: (cat, check_landing_times(
            list(map(get_landing_time, track[cat])), base_land)),
                          additional_categories)
        track["landing"] = base_land
        track["landing_timestamp"] = base_land - int(track["created"])
        for cat, index in new_indexes:
            update_track(cat, index, base_land)
        return track


    def count_ts_features(track):

        @check_if_none(optional={})
        def count_ts_features_for_track(track_simple, features, suf):

            def count_compressed_ts(ft):

                @check_if_none(optional=[0] * ts_len)
                def find_closest(timestamps, fields, start, stop, step):
                    if ft == "LatLon":
                        fields = fields["coordinates"]
                    find_ts = lambda ts: fields[max(0, bisect_right(timestamps, ts) - 1)]
                    return map(find_ts, range(start, stop, step))

                return "{0}_{1}".format(ft, suf), list(find_closest(track_simple.get(ft + "_timestamp"),
                                                                    track_simple.get(ft),
                                                                    start, stop, step))
            return dict(map(count_compressed_ts, features))

        start = track["landing_timestamp"] - lag_first
        stop = track["landing_timestamp"] - lag_last
        ts_len = int((stop - start) / step)
        track.update(count_ts_features_for_track(track,
                                                 features[base_category],
                                                 base_category))
        for additional_category in additional_categories:
            track.update(count_ts_features_for_track(track[additional_category],
                                                     features[additional_category],
                                                     additional_category))
        return track

    def count_dir_and_exit(track):

        def count_dir(runway_points):
            if len(runway_points) > 0:
                return int(runway_points[-1][0] > runway_points[0][0])
            return None

        def count_exit(runway_points):
            if len(runway_points) > 0:
                dist_last_point = partial(haversine, runway_points[-1])
                return np.argmin(list(map(dist_last_point, airport_config["taxi_points"])))
            return None

        runway_border = Polygon(airport_config["runway_border"])
        runway_points = [(x, y) for x, y in track["LatLon"]["coordinates"]
                         if runway_border.contains(Point(x, y))]
        track.update({"dir": count_dir(runway_points),
                      "exit": count_exit(runway_points)})
        return track

    def count_delay(track):

        @check_if_none()
        def count_from_fpl(landing, planned_hr, planned_min):
            planned_arr_ts = planned_hr * 60 * 60 + planned_min * 60
            landing_ts = landing % (24 * 60 * 60)
            return landing_ts - planned_arr_ts


        track.update({"delay": count_from_fpl(track["landing"],
                                              get_from_dict(track, ["CAT_62", "arrTime", "hour"]),
                                              get_from_dict(track, ["CAT_62", "arrTime", "min"]))})
        return track

    def count_cruise_time(track):

        @check_if_none()
        def count_from_fpl(dep_hr, dep_min, arr_hr, arr_min):
            dep_ts = dep_hr * 60 * 60 + dep_min * 60
            arr_ts = arr_hr * 60 * 60 + arr_min * 60
            if arr_ts > dep_ts:
                return arr_ts - dep_ts
            return 24 * 60 * 60 - (dep_ts - arr_ts)

        track.update({"cruise_time": count_from_fpl(get_from_dict(track, ["CAT_62", "depTime", "hour"]),
                                                    get_from_dict(track, ["CAT_62", "depTime", "min"]),
                                                    get_from_dict(track, ["CAT_62", "arrTime", "hour"]),
                                                    get_from_dict(track, ["CAT_62", "arrTime", "min"]))})
        return track

    def count_airline(track):
        track.update({"airline": track["callsign"][:3]})
        return track

    def postprocess(track):
        if track["exit"] is None:
            return None
        fts = ["dir", "exit", "cruise_time", "callsign", "delay", "airline", "id",
               "landing"]
        ok_keys = list(filter(lambda x: "_CAT_" in x, track.keys()))
        return {k: v for k, v in track.items() if k in ok_keys + fts}

    funcs = [preprocess_filter, count_landing_time, count_ts_features, count_dir_and_exit,
             count_delay, count_cruise_time, postprocess]
    return pipeline(track, map(check_if_none(), funcs))


def run_example(optimize_batch=False, njobs=None, batch_num=1000, verbose=False):

    def print_statistics(trks):
        print("Numer of ids: {0}".format(len(trks)))
        print("Number of not None elements: {0}".format(len(list(filter(lambda x: x is not None, trks)))))
        print("Example element: {0}".format(list(filter(lambda x: x is not None, trks))[1]))
        # print("Number of qunique ids: {0}".format(len(set(get_key(trks, "id")))))
        # print("Number of unique gen ids: {0}".format(len(set(get_key(trks, "gid")))))
        # print("Len of track, 1st quartile: {0}, median: {1}, 3rd quertile: {2}".format(*map(lambda x: np.percentile(get_key(trks, "len"), x), [25, 50, 75])))
        # print("Distribution of hours: {0}".format(Counter(map(lambda x: x.hour, get_key(trks, "date")))))

    features = {"CAT_62": ["VxVy", "indicatedAirSpeed",
                          "groundSpeed", "turbulence", "rateOfClimb",
                          "trackAngle", "magHeading", "traLoVe"],
                "CAT_21": ["LatLon", "mfl", "baroVertRate"]}

    EPGD_config ={"runway_border": [[ 54.3708 , 18.4919 ],
                         [ 54.3714 , 18.4923 ],
                         [ 54.3818 , 18.4518 ],
                         [ 54.3808 , 18.4515 ],
                         [ 54.3708 ,  18.4919 ]],
                  "taxi_points": [(54.371807, 18.490809),
                       (54.373038, 18.485809),
                       (54.375963, 18.474029),
                       (54.377244, 18.468654),
                       (54.378006, 18.465618),
                       (54.379681, 18.458762),
                       (54.380450, 18.455865)] ,
                  "dir_exits": {1 :[3, 5, 6],
                                0: [0, 1, 2, 4]}}

    db_config = {"host": "127.0.0.1",
                 "username": "sesar",
                 "password": "sesar",
                 "authSource": "sesar",
                 "db_name": "sesar",
                 "collection": "lands_EPGD"}

    run_config = {"optimize": optimize_batch,
                  "njobs": njobs,
                  "batch_num": batch_num,
                  "verbose": verbose}

    process_track_fun = wrapped_partial(process_track,
                                        airport_config=EPGD_config,
                                        features=features,
                                        lag_first=600,
                                        lag_last=0,
                                        step=10)
    run_mongo_query_processing(db_config, run_config, {}, process_track_fun, print_statistics)

if __name__ == "__main__":
    for batch in [100, 500, 1000, 2000]:
        print("Running batch map for batch_num: {0}".format(batch))
        run_example(batch_num=100)
