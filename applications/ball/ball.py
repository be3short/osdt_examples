import argparse

import osdt
import yaml
from osdt_examples.models import ball,sensor,timer



def create_ball(
        y_position = 1.0,
        y_velocity = 0.0,
        gravity = 9.81,
        restitution = .95
    ):
    state = ball.State(y_position=y_position, y_velocity=y_velocity)
    params = ball.Params(gravity=gravity, restitution=restitution)
    system = osdt.create_system(x=state, c=ball.C, f=ball.F, d=ball.D, g=ball.G, u=ball.U,
                              y=ball.Y, vars={ball.Params: params}, id="ball")
    create_figures()

def create_figures():
    # create a figure
    fig = osdt.create_figure(layout=[[1,3,4,4], [2,3,4,4]],width=1200, height=600,
                             title="Bouncing Ball",dpi=130)
    fig.configure_subplot(1, )
    fig.subplot(1).plot("y_position", max_points=200)
    fig.subplot(2).plot("y_velocity", max_points=200)
    fig.subplot(3).plot(["y_position", "y_velocity"], max_points=200)
    fig.subplot(4).plot(x="y_velocity", y="y_position", max_points=200)

    # create a figure
    fig2 = osdt.create_figure(width=800, height=600, layout=[[1],[2]], title="Bouncing Ball",dpi=130)
    fig2.configure_subplot(1, x_axis="Time (s)", y_axis="Position (m)")
    fig2.configure_subplot(2, x_axis="Time (s)", y_axis="Velocity (m/s)")
    fig2.plot(1,"y_position")
    fig2.plot(2,"y_velocity")

    return fig,fig2


def main(
        y_position = 1.0,
        y_velocity = 0.0,
        gravity = 9.81,
        restitution = .95,
        time=10.0,
        jumps=20,
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


def main_old(y_position = 1.0,
         y_velocity = 0.0,
         gravity = 9.81,
         restitution = .95,
         time=10.0,
         jumps=20):
    create_ball(y_position,y_velocity,gravity,restitution)
    osdt.run(time=time,jumps=jumps)
    create_figures()
    osdt.display()


def get_argparse():
    argpars = osdt.args.Args(function=main)
    parsed_args = argpars.get_parsed_args()
    main(**parsed_args)



def figure1(export_path=None,export_format="png"):
    figure1 = osdt.create_figure(1200,800,layout=[[1],[2]],title="Bouncing Ball")
    figure1.plot(1,"y_position")
    figure1.plot(2, "y_velocity")
    figure1.export(export_path,format=export_format)
    return figure1


def create_opfile():
    systems = {
        "ball1": ball,
        "sensor1":sensor,
        "timer1":timer
    }
    opfile_map = {}
    for system in systems:
        opfile = osdt.constructor.get_default_opfile(systems[system])
        opfile_map[system]=opfile["system"]

    print(yaml.safe_dump(opfile_map,sort_keys=False))

if __name__ == "__main__":
   # create_opfile()
    get_argparse()


