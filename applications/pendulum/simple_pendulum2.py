"""Bouncing ball model"""
import os.path
import sys

import osdt as dt
from osdt_examples.models import simple_pendulum,simple_pendulum2


import osdt.constructor



fb = osdt.constructor.OpfileBuilder()

fb.add_sys("pendulum",simple_pendulum,simple_pendulum.State,simple_pendulum.Params)
fb.add_func(None, osdt.run)
osdt.constructor.build_figure_file(layout=[[1],[2]],path="applications/pendulum/figure1.yaml")
fb.add_file("figure",osdt.get_path("osdt_examples/applications/pendulum/figure1.yaml"))
fb.create_opfile("applications/pendulum/pendulum")




dt.display()




