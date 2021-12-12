import osdt

def octo_figure():
    # create a figure
    fig = osdt.create_figure(layout=[[1,2,5,5],[3,4,5,5] ],title="Dubins",
                           width=1600, height=600)
    # configure the subplots
    fig.subplot(1).edit_config(title="X Position")
    fig.subplot(2).edit_config(title="Y Position")
    fig.subplot(3).edit_config(title="Orientation")
    fig.subplot(4).edit_config(title="Turn State")
    fig.subplot(5).edit_config(title="X Position vs Y Position")
    # plot the data
    fig.subplot(1).plot("x_position")
    fig.subplot(2).plot("y_position")
    fig.subplot(3).plot("orientation")
    fig.subplot(4).plot("turn")
    fig.subplot(5).plot(x="x_position",y="y_position")