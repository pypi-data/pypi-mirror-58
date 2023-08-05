#! /usr/bin/env python
# encoding: utf-8
from __future__ import print_function, division, absolute_import

# Copyright © 2018 Uwe Schmitt <uwe.schmitt@id.ethz.ch>

def _profile(fun):
    return fun

try:
    profile
except NameError:

    __builtins__["profile"] = _profile
