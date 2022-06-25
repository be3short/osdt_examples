import osdt as dt
from osdt_examples.models import simple_pendulum


@dt.root
def pendulum_app():
    app = dt.app(
        sys1=dt.create_sys(simple_pendulum),
        fig1=figure()
    )
    return app

def figure():
    fig = dt.create_fig(
        title="Simple Pendulum",
        layout=[[1], [2]])
    fig.config(1,x_axis="Time(s)",y_axis="Angle(rad)")
    fig.config(2,x_axis="Time(s)",y_axis="Velocity (rad/s)")
    fig.plot(1,"angle")
    fig.plot(2,"velocity")
    print(fig.get_subplot(1))
    return fig


if __name__ == "__main__":
    app = pendulum_app()
    app.sys1.state.set(angle=.3,velocity=1.1)
    app.sys2.state.set(angle=1.3,velocity=0.1)
    app.fig1.set_style({"font.size":  15.0,"figure.titlesize":20.0})
    app.run(True)
