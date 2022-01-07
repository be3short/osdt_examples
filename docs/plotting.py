import sys, os

import osdt
import random
from osdt_example.models import timer
from osdt_example.functions.bouncing_ball import ball_figure

import osdt

state = simple_timer.State(value=1.0)
params = simple_timer.Params(interval=1.0)
system = osdt.create_system(x=state, c=simple_timer.C, f=simple_timer.F, d=simple_timer.D, g=simple_timer.G, u=simple_timer.U,
                          y=simple_timer.Y, vars={simple_timer.PARAMS: params}, id="Timer")

# set integrator and/or edit configuration if different from the defaults (optional)
osdt.set_integrator("vode",max_step=0.1)
osdt.set_configuration(max_plot_points=1000)
random.randrange(1,3)

osdt.run(time=10.0, jumps=20)
#ball_figure()
# create a figure

fig = osdt.create_figure(width=500, height=500,layout=[[1, 2], [3, 3]],
                         title="Figure Title", dpi=100.0, style=None,
                         autofit=True, pad_w=1.08, pad_h=1.08)
fig.edit_configuration(width=500, height=500, title="Updated Title",
                       dpi=100.0, style=None)
fig.configure_subplot(1, title="Subplot 1", x_axis="X Axis Label",
                      y_axis="Y Axis Label", legend=False, colors=[])
fig.configure_subplot(2, title="Subplot 2")
fig.configure_subplot(3, title="Subplot 3")

fig2 = osdt.create_figure(width=500, height=500,layout=[[1]],
                         title="Figure Title", dpi=100.0, style=None,
                         autofit=True, pad_w=1.08, pad_h=1.08)
fig2.configure_subplot(1, title="Subplot 1", x_axis="X Axis Label",
                      y_axis="Y Axis Label", legend=False, colors=[])
fig2.plot(1, x=osdt.TIME, y="value", system=None, label=None, color=None,
         dash_style=None, field_label=False, max_points=None)
osdt.display()

fig.configure_subplot(1, x_axis="Time (s)", y_axis="Position (m)")
fig.configure_subplot(2, x_axis="Time (s)", y_axis="Velocity (m/s)")
fig.plot(1, x=osdt.TIME, y="value", system=None, label=None, color=None,
         dash_style=None, field_label=False, max_points=None)

fig.figure()

subplot1=fig.subplot(1)

subplot1.axes()

fig.plot(2,"y_velocity")
osdt.display()
fig.export("files/bouncing_ball_overview_example",format="png")
fig.export("figure_file", format="png", close=False, overwrite=True)
data = system.get_data()
data.to_csv("files/system_data_csv")

osdt.save(system,"files/saved_system")
osdt.save_environment("files/saved_environment")
