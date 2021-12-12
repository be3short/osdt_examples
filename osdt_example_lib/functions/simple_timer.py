import osdt


def timer_figure():
    # create a figure
    fig = osdt.create_figure(layout=[[1]], title="Simple Timer",
                           width=800, height=600)
    fig.subplot(1).plot("value")
