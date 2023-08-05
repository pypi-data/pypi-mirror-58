#! /usr/bin/env python
#encoding: utf-8
# Copyright © 2019 Uwe Schitt <uwe.schmitt@id.ethz.ch>

import os
import sys

if sys.version_info[0] == 3:
    basestring = str


def base_cache_folder():
    home = os.path.expanduser("~")
    if sys.platform.startswith("darwin"):
        base_folder = os.path.join(home, "Library", "Cache")
    else:
        base_folder = os.path.join(home, "_cache")
    return os.path.join(base_folder, "PyCosmo")
