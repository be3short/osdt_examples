import sys, os

import osdt
#osdt.import_library("osdt_example")

from osdt_example.models import simple_timer
import osdt

state = simple_timer.State(value=1.0)
params = simple_timer.Params(interval=1.0)
timer_sys = osdt.create_system(
    x=state, c=simple_timer.C, f=simple_timer.F, d=simple_timer.D,
    g=simple_timer.G, u=simple_timer.U, y=simple_timer.Y,
    vars={simple_timer.PARAMS: params}, id="timer")


osdt.run(time=10.0, jumps=20)

# create a figure
fig = osdt.create_figure(layout=[[1],[2]], title="Simple Timer",
                         width=500, height=500, relative_title=False)
fig.configure(1, title="Timer1", x_axis="Time (sec)", y_axis="Timer Value")
#fig.configure(2, title="Timer2", x_axis="Time (sec)", y_axis="Timer Value")

fig.plot(1, "value")
fig.subplot(2).plot("value")
#fig.subplot(3).plot("value")

#fig.subplot(1).edit_config(x_axis_label="Time (sec)",
                          # y_axis_label="Timer Value")
#fig.subplot(1).plot("value")
fig.export("files/simple_timer")

osdt.display()
fig.export("files/simple_timer_after")

osdt.save_environment("files/saved_environment")