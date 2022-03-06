import osdt

def main(system_files = []):
    for system_path in system_files:
        osdt.load(system_path)

    # create a figure
    fig = osdt.create_figure(layout=[[1, 3, 4, 4], [2, 3, 4, 4]], width=1200,
                             height=600,
                             title="Bouncing Ball", dpi=130)
    #   fig.configure_subplot(1, )
    fig.plot(1, "y_position", max_points=1000)
    fig.plot(2, "y_velocity", max_points=1000)
    fig.plot(3, ["y_position", "y_velocity"], max_points=1000)
    fig.plot(4, x="y_velocity", y="y_position", max_points=1000)

