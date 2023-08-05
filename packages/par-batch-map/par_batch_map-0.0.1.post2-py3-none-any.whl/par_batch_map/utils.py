# -*- coding: utf-8 -*-
"""
Module with utils functions
"""

from functools import reduce, partial, wraps, update_wrapper
from itertools import chain, islice, count, zip_longest, takewhile, repeat
from time import time
import zlib
import json
import base64

def check_if_none(optional=None):
    """
    Decorator checking input of function, if all of input is None, then returned
    is optional value (default None)

    Parameters
    ----------
    optional : Any
        element returned from function when all arguments are null
    Returns
    -------
    callable
        decorated function
    """

    def fun_wrap(fun):
        @wraps(fun)
        def wrapper(*args):
            if all(map(lambda x: x is not None, args)):
                return fun(*args)
            return optional

        return wrapper

    return fun_wrap

def partial_info(repres=lambda x: x):
    """
    Decorator printing output of the function, it may be processed by function repres

    Parameters
    ----------
    repres : callable
        function creating represenation of ouput, default identity
    Returns
    -------
    callable
        decorated function
    """

    def fun_wrap(fun):
        @wraps(fun)
        def wrapper(*args):
            ret = fun(*args)
            print("[INFO] fun: {0}, out: {1}".format(fun.__name__, repres(ret)))
            return ret
        return wrapper
    return fun_wrap

def debug_info(repres=lambda x: x):
    """
    Decorator for debugging input and output of the function

    Parameters
    ----------
    repres : callable
        function creating represenation of input, default identity
    Returns
    -------
    callable
        decorated function
    """

    def fun_wrap(fun):
        @wraps(fun)
        def wrapper(*args):
            try:
                ret = fun(*args)
            except Exception as e:
                print("[ERROR] function: {0},\nError: {1},\nArgs: {2}\n".format(fun.__name__, e, list(map(repres, args))))
                ret = None
            return ret
        return wrapper
    return fun_wrap

def pipeline(x, funcs):
    """
    Pipeline of functions, it is equivalent with compund of functions:
    pipeline(x, [f1, f2, f3]) = f3(f2(f1(x)))

    Parameters
    ----------
    x : Any
        input to the first function
    funcs : iterable
        list of functions to apply
    Returns
    -------
    Any
        result of the compund
    """
    return reduce(lambda res, f: f(res), funcs, x)

def timing(f):
    """
    Decorator printing time of function computation

    Parameters
    ----------
    f : callable
        function for timing
    Returns
    -------
    callable
        decorated function
    """
    @wraps(f)
    def wrap(*args, **kw):
        ts = time()
        result = f(*args, **kw)
        te = time()
        print("func: {0} args: [{1}, {2}] took: {3:.2f} sec".format(f.__name__, args, kw, te-ts))
        return result
    return wrap

def wrapped_partial(func, *args, **kwargs):
    """
    partial with __name__ and __doc__ attributes
    """
    partial_func = partial(func, *args, **kwargs)
    update_wrapper(partial_func, func)
    return partial_func

def timing_with_return(f):
    """
    Decorator printing time of function computation with return this time

    Parameters
    ----------
    f : callable
        function for timing
    Returns
    -------
    callable
        decorated function
    """
    @wraps(f)
    def wrap(*args, **kw):
        ts = time()
        result = f(*args, **kw)
        te = time()
        return te-ts, result
    return wrap

def group(iterable, n, fillvalue=None):
    """
    Collect data into fixed-length chunks or blocks
    group('ABCDEFG', 3) --> [A,B,C] [D,E,F] [G, None, None]
    Parameters
    ----------
    iterable : iterable
        iterable for grouping
    n : int
        size of group
    Returns
    -------
    iterator
        iterator of subsequent groups
    """
    args = [iter(iterable)] * n
    return zip_longest(*args, fillvalue=fillvalue)

def map_ifnotnone(f, l):
    return map(f, filter(lambda x: x is not None, l))

def enumerate_iter(iterator, end="END", max_it=None):
    """
    Function enumerating iterator with limit

    Parameters
    ----------
    iterator : iterator
        iterator for iterating
    end : str
        indicator of end of iterator
    max_it: int
        max number of iterations
    Returns
    -------
    generator
        generated enumerated elements
    """
    ct = 0
    iterate = True
    while iterate:
        try:
            yield ct, next(iterator)
        except StopIteration:
            iterate = False
            yield ct, end
        ct += 1
        if max_it and ct >= max_it:
            iterate = False

def get_from_dict(d, path):
    """
    Function getting element from dict according to list of subsequent keys,
    get_from_dict(d, [k1, k2, k3]) = d[k1][k2][k3]

    Parameters
    ----------
    d : dict
        input dictionary
    path : iterable
        list of keys
    Returns
    -------
    Any
        element of dict
    """
    try:
        return reduce(lambda x, key: x.get(key), path, d)
    except Exception as e:
        return None

def get_key(iterable, key):
    """
    Get elements with key from list of dicts

    Parameters
    ----------
    iterable : iterable
        iterable with dicts
    key : Hashable
        key to extract elements
    Returns
    -------
    iterable
        iterable of values
    """
    return list(map(lambda x: x[key], iterable))

def empty_f(x):
    pass


def json_zip(j):

    return base64.b64encode(zlib.compress(json.dumps(j).encode('utf-8'))).decode('ascii')


def json_unzip(j):

    try:
        j = zlib.decompress(base64.b64decode(j))
    except:
        raise RuntimeError("Could not decode/unzip the contents")

    try:
        j = json.loads(j)
    except:
        raise RuntimeError("Could interpret the unzipped contents")

    return j
