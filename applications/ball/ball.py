import argparse

import osdt
import yaml
from osdt_examples.models import ball

def main(
        y_position = 1.0,
        y_velocity = 0.0,
        gravity = 9.81,
        restitution = .95,
    ):

    state = ball.State(y_position=y_position, y_velocity=y_velocity)
    params = ball.Params(gravity=gravity, restitution=restitution)
    system = osdt.create_system(x=state, c=ball.C, f=ball.F, d=ball.D, g=ball.G, u=ball.U,
                              y=ball.Y, vars={ball.Params: params}, id="ball")

    osdt.run()

    # create a figure
    fig = osdt.create_figure(layout=[[1,1,3,3], [2,2,3,3]],width=1200, height=600,
                             title="Bouncing Ball",dpi=100)

    # configure subplots
    fig.configure_subplot(1,title="State vs Time", y_axis="Y Position (m)",legend=False)
    fig.configure_subplot(2, x_axis="Time(s)", y_axis="Y Velocity (m/s)", legend=False)
    fig.configure_subplot(3, title="Position vs Velocity", x_axis="Y Position (m)", y_axis="Y Velocity (m/s)", legend=False)

    # plot data
    fig.subplot(1).plot("y_position", max_points=1000)
    fig.subplot(2).plot("y_velocity", max_points=1000)
    fig.subplot(3).plot(x="y_position",y="y_velocity", max_points=1000)
    fig.export("figure1",format="png")

    osdt.display()

# default if file is run with python
if __name__ == "__main__":
    main()

