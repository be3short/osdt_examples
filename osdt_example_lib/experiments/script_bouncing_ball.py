import sys,os

import osdt

from osdt_example_lib.models import bouncing_ball as bb
import osdt as dt

from random import random

def main(y_position=1.0,
        y_velocity=0.0,
        gravity=9.81,
        restitution=.95,
        t=5.0,
        j=20):

    ball1 = osdt.scripting.run_task("tasks/test.yaml","ball1")
    ball2 = osdt.scripting.run_task("tasks/test.yaml","ball2")

    dt.run(t=t, j=j)

    # create a figure
    fig = dt.create_figure(layout=[[1,3,4,4], [2,3,4,4]],title="Bouncing Ball",
                           width=1600, height=600)

    fig.subplot(1).plot("y_position",max_points=200)
    fig.subplot(2).plot("y_velocity",max_points=200)
    fig.subplot(3).plot(["y_position", "y_velocity"],max_points=200)
    fig.subplot(4).plot(x="y_velocity", y="y_position",max_points=200)
    #fig.export("output/single_bouncing_ball/figure.pdf",format="pdf")
    print(dt.toolbox.global_operator.integrator._integrator.__dict__)
    dt.display()


if __name__ == "__main__":
    main()



