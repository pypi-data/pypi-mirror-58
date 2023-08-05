#! /usr/bin/env python
# encoding: utf-8
from __future__ import print_function, division, absolute_import

from scipy.interpolate import interp1d as _interp1d


class interp1d(object):

    """original interp1d can not be pickled. This class solves this"""

    def __init__(self, x, y, *args, **kws):
        self.x = x
        self.y = y
        self.args = args
        self.kws = kws
        self._setup()

    def _setup(self):
        self.function = _interp1d(self.x, self.y, *self.args, **self.kws)

    def __call__(self, *args, **kws):
        return self.function(*args, **kws)

    def __getstate__(self):
        return self.x, self.y, self.args, self.kws

    def __setstate__(self, data):
        self.x, self.y, self.args, self.kws = data
        self._setup()

