import osdt


def ball_sampled_figure(pos_sensor, vel_sensor):
    # create a figure
    fig = osdt.create_figure(layout=[[1, 2]], title="Bouncing Ball with Sensors",
                           width=1600, height=600)
    fig.subplot(1).plot("y_position", label="ball y position")
    fig.subplot(1).plot("value", label="sensor y position", sys=osdt.get_system(pos_sensor),
                        field_label=" : ")
    fig.subplot(2).plot("y_velocity", label="ball y velocity")
    fig.subplot(2).plot("value", label="sensor y velocity", sys=osdt.get_system(vel_sensor),
                        color="red")


def ball_figure():
    # create a figure
    fig = osdt.create_figure(layout=[[1,3,4,4], [2,3,4,4]],title="Bouncing Ball",
                           width=1600, height=600)
    fig.subplot(1).plot("y_position",max_points=200)
    fig.subplot(2).plot("y_velocity",max_points=200)
    fig.subplot(3).plot(["y_position", "y_velocity"],max_points=200)
    fig.subplot(4).plot(x="y_velocity", y="y_position",max_points=200)
