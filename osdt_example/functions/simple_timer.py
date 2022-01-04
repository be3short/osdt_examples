import osdt


#osdt.utils.generate_system_file("test_sys_file","osdt_example.models.simple_timer","State","Params","Params2")
#print(osdt.load_objfile("test_sys_file.yaml"))
#osdt.load_objfile("runtest.yaml")




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

def objfile_figure_dict(dictionary):
    return objfile_figure(**dictionary)

def objfile_figure(figure={}, subplots={}, data={}, export={}, display=True):
    fig = osdt.create_figure(**figure)
    for subplot in subplots:
        fig.configure_subplot(subplot=subplot,**subplots[subplot])
    for subplot in data:
        plot_data = data[subplot]
        for dat in plot_data:
            fig.plot(subplot, **dat)
    try:
        path = export["path"]
        if path is not None:
            fig.export(**export)
    except:
        pass
    if not display:
        fig.close()

def call_func():
    kwdict = dictionary
    return kwdict
