import sys,os

import osdt

from osdt_example_lib.models import bouncing_ball as bb
import osdt as dt

from random import random


def plot():
    # create a figure
    fig = dt.create_figure(layout=[[1,3,4,4], [2,3,4,4]],title="Bouncing Ball",
                           width=1600, height=600)
    fig.subplot(1).plot("y_position",max_points=200)
    fig.subplot(2).plot("y_velocity",max_points=200)
    fig.subplot(3).plot(["y_position", "y_velocity"],max_points=200)
    fig.subplot(4).plot(x="y_velocity", y="y_position",max_points=200)
    dt.display()

def main(action_file="operators/bouncing_ball.yaml"):

    ball1 = osdt.scripting.run_task(action_file,"create_ball")
    osdt.scripting.run_task(action_file,"edit_config")
    dt.run()
    plot()
    ball1 = osdt.scripting.run_task(action_file,"save_env")




if __name__ == "__main__":
    main()



