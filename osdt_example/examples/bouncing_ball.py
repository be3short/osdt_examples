import sys, os

import osdt

from osdt_example.models import bouncing_ball as bb
import osdt

state = bb.State(y_position=5.3, y_velocity=1.0)
params = bb.Params(gravity=9.81, restitution=.95)
system = osdt.create_system(x=state, c=bb.C, f=bb.F, d=bb.D, g=bb.G, u=bb.U,
                          y=bb.Y, vars={bb.PARAMS: params}, id="ball")


osdt.run(time=10.0, jumps=20)

# create a figure
fig = osdt.create_figure(layout=[[1,3,4,4], [2,3,4,4]],width=1200, height=600,
                         title="Bouncing Ball",dpi=130)
fig.configure(1,)
fig.subplot(1).plot("y_position", max_points=200)
fig.subplot(2).plot("y_velocity", max_points=200)
fig.subplot(3).plot(["y_position", "y_velocity"], max_points=200)
fig.subplot(4).plot(x="y_velocity", y="y_position", max_points=200)

# create a figure
fig2 = osdt.create_figure(width=800, height=600, layout=[[1],[2]], title="Bouncing Ball",dpi=130)
fig2.configure(1,x_axis="Time (s)", y_axis="Position (m)")
fig2.configure(2,x_axis="Time (s)", y_axis="Velocity (m/s)")
fig2.plot(1,"y_position")
fig2.plot(2,"y_velocity")
osdt.display()

