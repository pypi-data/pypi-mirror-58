# Copyright (C) 2014 ETH Zurich, Institute for Astronomy

# System imports
from __future__ import print_function, division, absolute_import

import functools
import hashlib
import types

import dill
import numpy as np


def _check_a_ode(a=1.0, tilltoday=False):
    """
    Checks that the a vector used in for the Boltz integrator statisfies some basic condition:
    (i) a is listed in increasing order,
    (ii) that the first value of a is early enough

    :param a:
    :param tilltoday:
    """
    aa = np.atleast_1d(a)
    ind_sort = aa.argsort()
    ind_unsort = ind_sort.argsort()
    a_sort = aa[ind_sort]
    return a_sort, ind_unsort


def relative_differences(a=1., b=1.):
    a = np.atleast_1d(a)
    b = np.atleast_1d(b)
    return np.absolute((a - b) / a)
