import sys, os

import osdt

from osdt_example.models import bouncing_ball as bb
import osdt

state = bb.State(y_position=5.0, y_velocity=1.0)
params = bb.Params(gravity=9.81, restitution=.95)
ball = osdt.create_system(x=state, c=bb.C, f=bb.F, d=bb.D, g=bb.G, u=bb.U,
                          y=bb.Y, vars={bb.PARAMS: params}, id="ball")


osdt.run(time=10.0, jumps=20)

# create a figure
fig = osdt.create_figure(layout=[[1, 3, 4, 4], [2, 3, 4, 4]],
                         title="Bouncing Ball",
                         width=1600, height=600)
fig.subplot(1).plot("y_position", max_points=200)
fig.subplot(2).plot("y_velocity", max_points=200)
fig.subplot(3).plot(["y_position", "y_velocity"], max_points=200)
fig.subplot(4).plot(x="y_velocity", y="y_position", max_points=200)
osdt.display()
