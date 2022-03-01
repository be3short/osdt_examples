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

    osdt.run(time=time,jumps=jumps)

    # create a figure
    fig = osdt.create_figure(layout=[[1,3,4,4], [2,3,4,4]],width=1200, height=600,
                             title="Bouncing Ball",dpi=130)
    fig.configure_subplot(1, )
    fig.subplot(1).plot("y_position", max_points=200)
    fig.subplot(2).plot("y_velocity", max_points=200)
    fig.subplot(3).plot(["y_position", "y_velocity"], max_points=200)
    fig.subplot(4).plot(x="y_velocity", y="y_position", max_points=200)

    osdt.display()

# default if file is run with python
if __name__ == "__main__":
    main()

