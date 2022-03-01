import argparse

import osdt
import yaml
from osdt_examples.models import ball

def main(
        argument_file = "osdt_examples/applications/ball/ball_args.yaml"
    ):
    args = osdt.get_file_args(argument_file)
    state = ball.State(y_position=args["y_position"], y_velocity=args["y_velocity"])
    params = ball.Params(gravity=args["gravity"], restitution=args["restitution"])
    system = osdt.create_system(x=state, vars={ball.Params: params}, id="ball", **args["model"])

    osdt.run(time=args["time"],jumps=args["jumps"])

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

