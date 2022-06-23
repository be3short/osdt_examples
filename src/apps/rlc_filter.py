import osdt as dt
from osdt_examples.models import rlc_filter


@dt.task
def figure():
    fig = dt.create_fig(
        title="Simple Pendulum",
        layout=[[1,2,3], [4,5,6]])
    fig.config(1,x_axis="Time(s)",y_axis="Angle(rad)")
    fig.config(2,x_axis="Time(s)",y_axis="Velocity (rad/s)")
    fig.plot(1,"vc")
    fig.plot(2,"vl")
    fig.plot(3,"vr")
    fig.plot(4,"i")
    fig.plot(5,"di_dt")
    fig.plot(2,x="vc",y="vl")

    print(fig.get_subplot(1))
    return fig


@dt.task
def rlc_filter_app():
    app = dt.app(
        sys1=dt.build_sys(rlc_filter),
        fig1=figure()
    )
    return app


if __name__ == "__main__":
    app = rlc_filter_app()
    app.run(True)
