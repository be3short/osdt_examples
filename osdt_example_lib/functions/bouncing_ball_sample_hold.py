import osdt

def figure1(pos_sensor, vel_sensor):
    # create a figure
    fig = osdt.create_figure(layout=[[1, 2]], title="Bouncing Ball with Sensors",
                           width=1600, height=600)

    fig.subplot(1).plot("y_position", label="ball y position")
    fig.subplot(1).plot("value", label="sensor y position", sys=osdt.get_system(pos_sensor),
                        field_label=" : ")
    fig.subplot(2).plot("y_velocity", label="ball y velocity")
    fig.subplot(2).plot("value", label="sensor y velocity", sys=osdt.get_system(vel_sensor),
                        color="red")
    
