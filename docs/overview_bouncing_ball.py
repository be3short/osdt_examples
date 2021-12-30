import sys, os

import osdt
import random
from osdt_example.models import bouncing_ball as bb
from osdt_example.functions.bouncing_ball import ball_figure

import osdt

state = bb.State(y_position=5.3, y_velocity=1.0)
params = bb.Params(gravity=9.81, restitution=.95)
system = osdt.create_system(x=state, c=bb.C, f=bb.F, d=bb.D, g=bb.G, u=bb.U,
                          y=bb.Y, vars={bb.PARAMS: params}, id="ball")

# set integrator and/or edit configuration if different from the defaults (optional)
osdt.set_integrator("vode",max_step=0.1)
osdt.set_configuration(max_plot_points=1000)
random.randrange(1,3)

osdt.run(time=10.0, jumps=20)
ball_figure()
# create a figure
fig = osdt.create_figure(width=1000, height=500, layout=[[1],[2]], title="Bouncing Ball")
fig.configure_subplot(1, x_axis="Time (s)", y_axis="Position (m)")
fig.configure_subplot(2, x_axis="Time (s)", y_axis="Velocity (m/s)")
fig.plot(1,"y_position")
fig.plot(2,"y_velocity")
osdt.display()
fig.export("files/bouncing_ball_overview_example",format="png")

data = system.get_data()
data.to_csv("files/system_data_csv")

osdt.save(system,"files/saved_system")
osdt.save_environment("files/saved_environment")
