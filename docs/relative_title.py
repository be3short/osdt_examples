import sys, os

import osdt
#osdt.import_library("osdt_example")

from osdt_example.models import simple_timer
import osdt

# create a figure
fig = osdt.create_figure(layout=[[1]], title="Forced Centering",
                         width=800, height=200, force_center=True)
fig.configure_subplot(1, y_axis="Y Axis Label", title="Subplot")
#fig.configure(2, title="Timer2", x_axis="Time (sec)", y_axis="Timer Value")
fig.export("files/forced_centering",format="png")

fig = osdt.create_figure(layout=[[1]], title="No Forced Centering",
                         width=800, height=200, force_center=False)
fig.configure_subplot(1, y_axis="Y Axis Label", title="Subplot")
# fig.configure(2, title="Timer2", x_axis="Time (sec)", y_axis="Timer Value")
fig.export("files/non_forced_centering",format="png")
