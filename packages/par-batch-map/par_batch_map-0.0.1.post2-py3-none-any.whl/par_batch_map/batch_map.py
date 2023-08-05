# -*- coding: utf-8 -*-
"""
This module contains base function
"""

from functools import reduce, partial, wraps
from itertools import chain, islice, count, zip_longest, takewhile, repeat
from multiprocessing import Queue, Lock, Event, Value, Process, cpu_count
from pymongo import MongoClient
import json
from time import time
import resource
import os

from par_batch_map.utils import *

def batch_map(f, iterable, cleaning=empty_f, optimize_batch=False, batch=1000, maxd = None, njobs=None,
              VERBOSE=False,
              END="END"):
    """
    This function in functionality is equivalent of map functor.
    Result of map(callable, iterable) should be the same as batch_map(callable, iterable),
    batch_map function allows parallel computation in batches, especially useful when
    iterable is stream data (iterator) and we don't know size of the data.
    Global variables are upper case.

    Parameters
    ----------
    f : callable
        function applied to each element of iterable
    iterable : iterable
        list of elements to process
    cleaning : callable
        function applied for each process to perform additional cleaning of resources,
        default is empty function
    optimize_batch : bool
        if number of batches must be estimated. Estimation is calculated as a function of average
        time of computation of f(x), where x is element of iterable, default False
    batch : int
        size of one batch, each process takes batch number of elements of iterable for computations, default 1000
    maxd : int
        max size of allowed open descriptors, if not set it is computed using system limitations
    NJOBS : int
        number of parallel processes, default is set on number of cores -1
    VERBOSE : bool
        if presented additional informations on output
    END : string
        string indicating end of computations
    Returns
    -------
    iterable
        equivalent of list(map(f, iterable))
    """

    def info(message):
        """
        Function for printing info

        Parameters
        ----------
        message : str
            message to print
        """
        if VERBOSE:
            print("[INFO] {0}".format(message))

    def process_batch(num, iterable, fun, njobs, active_proc_len):
        """
        Function for processing one batch of elements

        Parameters
        ----------
        num : int
            number of batch, used in collecting results to sort
        iterable : iterable
            list of batch elements
        fun : callable
            function applied for each element
        njobs : int
            number of jobs used in processing
        active_proc_len : Value
            shared variable between processes, number of active processes
        """

        def check_end(f):
            """
            Decorator for checking if END string is argument of the function
            """

            @wraps(f)
            def wrap(arg):
                if arg == END:
                    return arg
                return f(arg)

            return wrap

        RESULTS_QUEUE.put((num, list(map_ifnotnone(check_end(fun), iterable))))
        info("Batch num {0} calculated, process pid: {1} ending ...".format(num, os.getpid()))
        with active_proc_len.get_lock():
            active_proc_len.value -= 1
            if active_proc_len.value < njobs:
                FREE_RESOURCES.set()

    def start_process(fun, active_proc_len, args):
        """
        Function for statring one process

        Parameters
        ----------
        fun : callable
            function applied for each element
        active_proc_len : Value
            shared variable between processes, number of active processes
        args: tuple
            arguments to fun
        Returns
        -------
        Process
            instance of started multiprocessing.Process
        """
        num, iterable = args
        ar = (num, iterable, fun, NJOBS, active_proc_len, )
        with active_proc_len.get_lock():
            info("waiting ..., number of running processes: {0}".format(active_proc_len.value))
        FREE_RESOURCES.wait()
        with active_proc_len.get_lock():
            info("Resources free: {0} starting process num: {1}, fun: {2}".format(
                active_proc_len.value, num, fun.__name__))
        p = Process(target=process_batch, args=ar)
        p.start()
        with active_proc_len.get_lock():
            active_proc_len.value += 1
            if active_proc_len.value >= NJOBS:
                FREE_RESOURCES.clear()
        return p

    def pop_result(p):
        """
        Pop result from queue of results

        Parameters
        ----------
        p : Process
            process to return
        Returns
        -------
        tuple(Process, type)
            process and result of function
        """
        res = RESULTS_QUEUE.get()
        info("Pop result num {0}".format(res[0]))
        return p, res

    def collect_results(out):
        """
        Collect results from processes. Sorting in the way elements were in list before computations.

        Parameters
        ----------
        out : iterable
            list of tuples (index, result) - results from computations
        Returns
        -------
        iterable
            flattened list of results
        """
        proc, res = zip(*out)
        for p in proc:
            p.join()
            cleaning(p)
        return reduce(lambda x, y: x + y[1], sorted(res, key=lambda x: x[0]), [])

    def prepare_processing(iterable):
        """
        Preparing variables for running computations. Global variables used in all functions and shared variables between processed.

        Parameters
        ----------
        iterable : iterable
            iterable of elements, for computations iterator will be created
        Returns
        -------
        tuple(Queue, Event, Value, int, iterator, int, int)
            tuple of results for processing
        """

        def set_batch_number_and_iterator():
            INF = 10000
            batch_intervals = {(0, 0.0002): INF,
                               (0.0002, 0.02): 2000,
                               (0.02, 1): 500,
                               (1, 4): 50,
                               (4, INF): 20}
            if optimize_batch:
                it = iter(iterable)
                elem = next(it)
                ts, _ = timing_with_return(f)(elem)
                for interval, batchn in batch_intervals.items():
                    if interval[0] <= ts <= interval[1]:
                        return int(batchn * (cpu_count() / 100)), chain([elem], it)
            return batch, iter(iterable)

        def set_max_descriptors():
            return int(resource.getrlimit(resource.RLIMIT_NOFILE)[0] / 2) if maxd is None else maxd

        def set_njobs():
            return cpu_count() if njobs is None else njobs

        q = Queue()
        free_resources = Event()
        free_resources.set()
        active_proc_len = Value('i', 0)
        return q, free_resources, active_proc_len, *set_batch_number_and_iterator(), set_max_descriptors(), set_njobs()


    def run_calculations(iterable, fun, active_proc_len):
        return list(map(lambda x: start_process(fun, active_proc_len, x),
                        enumerate_iter(group(iterable, BATCH), max_it=MAX_DESCRIPTORS, end=[END])))

    def results_not_finished(results):
        if len(results) > 0 and results[-1][-1] == END:
            return False
        return True

    def drop_end(results):
        return results[:-1]

    RESULTS_QUEUE, FREE_RESOURCES, active_proc_len, BATCH, iterator, MAX_DESCRIPTORS, NJOBS = prepare_processing(iterable)
    info("Running with parameters: NJOBS: {0}, BATCH: {1}".format(NJOBS, BATCH))
    results = []
    while results_not_finished(results):
        results.append(collect_results(map(pop_result, run_calculations(iterator, f, active_proc_len))))
    return drop_end(list(chain(*results)))


def run_mongo_query_processing(db_config, run_config,
                               query,
                               process_fun,
                               after_fun):
    """
    Running parallel processing of mongo query with batches

    Parameters
    ----------
    db_config : dict
        config of mongo database, should include: host, username, password, authSource, db_name and collection
    run_config: dict
        config of parallel batch processing, should include: optimize, njobs, batch_num and verbose
    query: dict
        find query to mongo db
    process_fun: callable
        function to call on each document
    after_fun: callable
        function to call on result, it may be writing to file or printing some statistics
    """
    client = MongoClient(db_config["host"],
                         username=db_config["username"],
                         password=db_config["password"],
                         authSource=db_config["authSource"],
                         authMechanism='SCRAM-SHA-1')
    db = client[db_config["db_name"]]
    cursor = db[db_config["collection"]].find(query)
    res = list(batch_map(process_fun, cursor,
                         optimize_batch=run_config["optimize"],
                         njobs=run_config["njobs"],
                         batch=run_config["batch_num"],
                         VERBOSE=run_config["verbose"]))
    after_fun(res)
