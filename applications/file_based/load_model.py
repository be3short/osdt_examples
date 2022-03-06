import osdt.utils


def main(system_file="", system_keys=[], export=""):
    systems = osdt.construct_systems(system_file, system_keys)

    system = list(systems.values())[0]

    if len(export)>0:
        system.export_constructor(export,"exported_sys")

    osdt.run()

    figure1 = osdt.create_figure(1200, 800, layout=[[1]], title="Timer")
    figure1.plot(1, "value")
    figure1.export("figure1", format="png")


 # create a figure
    fig = osdt.create_figure(layout=[[1, 3, 4, 4], [2, 3, 4, 4]], width=1200,
                             height=600,
                             title="Bouncing Ball", dpi=130)
    #   fig.configure_subplot(1, )
    fig.configure_subplot(1,legend=True)
    fig.plot(1, "y_position", max_points=1000)
    fig.plot(2, "y_velocity", max_points=1000)
    fig.plot(3, ["y_position", "y_velocity"], max_points=1000)
    fig.plot(4, x="y_velocity", y="y_position", max_points=1000)

 # create the figure
    figure2 = osdt.create_figure(1200, 800, layout=[[1], [2]],
                                 title="Bouncing Ball with Sensors")

    figure2.plot(1, "y_position")
    figure2.plot(1, "value", system="pos_sensor")
    figure2.plot(2, "y_velocity")
    figure2.plot(2, "value", system="vel_sensor")

    figure2.export("figure2",format="png")