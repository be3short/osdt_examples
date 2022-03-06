import osdt
from osdt_examples.models import ball
def main(def_file = "",
         systems_key="systems",
         system_args_key="system_args",
         connections_key="connections",
         figures_key="figures",
         system_def_file = "sysfiles/ball_w_sensors.yaml",
         system_args_file="sysfiles/ball_w_sensors.yaml",
         connections_file="sysfiles/ball_w_sensors.yaml",
         figure_file="sysfiles/figure.yaml"):
    pathmap={"system_def_file":system_def_file,"system_arg_file":system_args_file,"connections_file":connections_file,"figure_file":figure_file}
    def_data = osdt.load(def_file)
    print(def_data)
    systems = def_data[systems_key]
    system_args = def_data[system_args_key]
    connections = def_data[connections_key]
    figures = def_data[figures_key]
    params= ball.Params(restitution=1.05)
    osdt.set("params",params)
    osdt.set("gravity",9.81)
    for file in systems:
        file_path = pathmap[file]
        id_key_map = systems[file]
        osdt.construct_systems(file_path,**id_key_map,system_args=system_args[file])

    for file in connections:
        file_path = pathmap[file]
        map={osdt.get_path(file_path): connections[file]}
        osdt.construct_connections(map)

    osdt.run()

    for file in figures:
        file_path = pathmap[file]
        figure_list = figures[file]
        osdt.construct_figures(osdt.get_path(file_path),*figure_list)