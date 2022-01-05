import osdt


osdt.utils.generate_system_file("sampler","osdt_example.models.sample_hold_sensor","State","Params")
#print(osdt.load_objfile("test_sys_file.yaml"))
#osdt.load_objfile("runtest.yaml")


def generate_system_default(module_name, state, params=[],model={"c":"C","f":"F","d":"D","g":"G","u":"U","y":"Y","initialize":"initialize"}):
    return osdt.utils.generate_system_args(module_name,state,params=params,model=model)

def output_default_file(file_path, default_args):
    osdt.utils.write_yaml_file(default_args,file_path)

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

