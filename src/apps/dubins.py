import osdt as dt
from osdt_examples.models import dubins_vehicle,dubins_controller


def figure():
    fig = dt.create_fig(layout=[[1,2,5,5],[3,4,5,5]])
    fig.config(1, title="X Position")
    fig.config(2, title="Y Position")
    fig.config(3, title="Orientation")
    fig.config(4, title="Turn State")
    fig.config(5, title="X Position vs Y Position")
    fig.plot(1, "x_position")
    fig.plot(2, "y_position")
    fig.plot(3, "orientation")
    fig.plot(4, "turn")
    fig.plot(5, x="x_position", y="y_position")
    return fig


def connect(app):
    app.controller.vehicle = app.vehicle
    app.vehicle.controller = app.controller


@dt.root
def dubins():
    app = dt.app(
        vehicle=dt.create_sys(dubins_vehicle),
        controller=dt.create_sys(dubins_controller),
        figure=figure()
    )
    app.add_setup(connect)
    return app


if __name__ == "__main__":
    app = dubins()
    app.run(True)




