import osdt


osdt.utils.generate_system_file("test_sys_file","osdt_example.models.simple_timer","State","Params","Params2")
print(osdt.load_objfile("test_sys_file.yaml"))
osdt.load_objfile("runtest.yaml")

def run():
    print(osdt.get_system("system").get("PARAMS"))
    osdt.run()


def timer_figure():
    # create a figure
    fig = osdt.create_figure(width=800, height=600, layout=[[1]],
                             title="Simple Timer")
    fig.subplot(1).edit_config(x_axis_label="Time (sec)",y_axis_label="Timer Value")
    fig.subplot(1).plot("value")

    fig.export("../output/timer_fig",format="png")
