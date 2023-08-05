from __future__ import absolute_import

import os

# needed for headless mode on ci server
if os.environ.get("CI") is not None:
    import sys

    assert "matplotlib" not in sys.modules, "init matplotlib broken"
    import matplotlib

    matplotlib.use("Agg")

if True:
    # this if is a hack to avoid resorting imports

    import pkg_resources  # part of setuptools

    from . import patches  # installs some hooks
    from .Cosmo import Cosmo
    from .load_configs import loadConfigs
    from .Obs import Obs


# Copyright (C) 2013 ETH Zurich, Institute for Astronomy


version = pkg_resources.require("PyCosmoLite")[0].version

"""
This is the PyCosmo package.
"""
__all__ = ["Cosmo"]

__version__ = version
__author__ = "Adam Amara, Alexander Refregier, Joel Akeret, Lukas Gamper, Uwe Schmitt"
__credits__ = "Institute for Astronomy ETHZ"
