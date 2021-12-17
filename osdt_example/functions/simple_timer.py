import osdt


def run():
    print(osdt.get_system("system").get("PARAMS"))
    osdt.run()


def timer_figure():
    # create a figure
    fig = osdt.create_figure(layout=[[1]], title="Simple Timer",
                           width=500, height=500)
    fig.subplot(1).edit_config(x_axis_label="Time (sec)",y_axis_label="Timer Value")
    fig.subplot(1).plot("value")

    fig.export("../output/timer_fig",format="png")
