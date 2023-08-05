# Copyright (C) 2014 ETH Zurich, Institute for Astronomy
#
# System imports
from __future__ import print_function, division, absolute_import

import os
import click

import numpy as np
from matplotlib import pylab

from .Cosmo import Cosmo


@click.command()
@click.option('--config-file', default=None, help='config file to use')
@click.option('--plot-file', default=None, help='file for quality plot, if not set plot is shown afterwards')
@click.option('--traces-folder', default=None, help='traces folder to use')
@click.option('--cache-folder', default=None, help='cache folder to use')
@click.option('--k', required=True, help='wave number k', type=float)
@click.option('--a-grid', required=False, help='grid for a in format a_min:a_max:step_size', type=str)
@click.option('--compile/--no-compile', default=True, help='create and compile solver if needed')
@click.argument('override_settings', nargs=-1)
def main(config_file, plot_file, traces_folder, cache_folder, k, a_grid, compile, override_settings):
    """
    compute and plot fields
    """
    if config_file is None:
        here = os.path.dirname(os.path.abspath(__file__))
        config_file = os.path.join(here, "config/default.py")
    if not os.path.exists(config_file):
        raise ValueError("config file {} does not exist".format(config_file))

    if a_grid is not None:
        if a_grid.count(":") != 2:
            raise ValueError("grid {} has wrong format".format(a_grid))
        a_fields = a_grid.split(":")
        try:
            a_min, a_max, a_step = map(float, a_fields)
        except ValueError:
            raise ValueError("grid entries must be numbers")
        grid = np.log(np.arange(a_min, a_max, a_step))
        print(grid)
    else:
        grid = None

    c = Cosmo(config_file)
    c.set(pk_type="boltz")
    if traces_folder:
        c.set(traces_folder=traces_folder)
    if cache_folder:
        c.set(cache_folder=cache_folder)

    for name, value in (setting.split("=") for setting in override_settings):
        try:
            value = int(value)
        except ValueError:
            try:
                value = float(value)
            except ValueError:
                pass
        c.set(**{name: value})

    fields = c.lin_pert.fields(k=k, grid=grid, verbose=True, interactive=compile)

    n = fields._ptr[0]
    pylab.subplot(211)
    pylab.title("step size")
    pylab.plot(np.diff(fields.lna)[:n])

    pylab.subplot(212)
    pylab.title("econ")
    pylab.plot(fields.econ[:n], label="econ")
    econ_max = c.params.econ_max
    econ_min = econ_max / c.params.econ_ratio
    pylab.axhline(y=econ_min, c="green", label="econ_min")
    pylab.axhline(y=econ_max, c="red", label="econ_max")
    pylab.legend()

    if plot_file is None:
        pylab.show()
    else:
        pylab.savefig(plot_file)
