# -*- coding: utf-8 -*-

""" Module summary description.

More detailed description.
"""

__author__ = 'Benjamin Pillot'
__copyright__ = 'Copyright 2019, Benjamin Pillot'
__email__ = 'benjaminpillot@riseup.net'

import time
from functools import wraps

from tqdm import tqdm


def decorator(function):
    @wraps(function)
    def add_tqdm(iterator, *args, **kwargs):
        return function(tqdm(iterator, desc=function.__name__ + " run"), *args, **kwargs)
    return add_tqdm


# @decorator
def process(alist):
    new_list = []
    for element in alist:
        new_list.append(element)
        time.sleep(1)
    return new_list


test = process([1, 2, 3])
print(test)
