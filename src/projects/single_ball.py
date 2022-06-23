import osdt as dt
from osdt_examples.models import ball


def single_ball() -> dt.Project:
    proj = dt.proj()
    proj.ball = ball.create()
    proj.fig = ball.plot()
    # proj.run()
    #  proj.display()
    return proj


def single_ball2() -> dt.Project:
    proj = dt.proj(
        ball=ball.create(),
        fig=ball.plot()
    )
    return proj


def three_ball() -> dt.Project:
    proj = dt.proj(
        p=ball.Params()
    )
    proj.set(
        ball1=ball.create(x=ball.State(y_position=1.0, y_velocity=3.0), p=proj.p),
        ball2=ball.create(x=ball.State(y_position=2.0, y_velocity=2.0), p=proj.p),
        ball3=ball.create(x=ball.State(y_position=3.0, y_velocity=1.0), p=proj.p),
    )

    return proj


def setupA(proj):
    for ind in range(1, (proj.n + 1)):
        y_pos = dt.random(proj.y_pos_min, proj.y_pos_max)
        y_vel = dt.random(proj.y_vel_min, proj.y_vel_max)
        sys = ball.create(x=ball.State(y_position=y_pos, y_velocity=y_vel), p=proj.p)
        proj.set(("ball" + str(ind)), sys)

def random_ball() -> dt.Project:
    project = dt.proj(
        p=ball.Params(),
        n=3,
        y_pos_min=1.0,
        y_pos_max=10.0,
        y_vel_min=-1.0,
        y_vel_max=5.0,
        fig=ball.plot()
    )

    project.set_process(setup=setupA)

    return project

def ball_plotter() -> dt.Project:
    fig = ball.plot()
    return fig


def save_single_ball2():
    single_ball2().save("project3")

def ball_figs() -> dt.Project:
    proj = dt.proj(
        fig1=ball.plot(),
        fig2=ball.plot(),
        fig3=ball.plot()
    )
    proj.fig1.title="Figure 1"
    proj.fig2.title="Figure 2"
    proj.fig3.title="Figure 3"
    return proj


def print_dict(proj):
    dt.view(proj.figs)
def three_ball2() -> dt.Project:
    proj = dt.proj(
        p=ball.Params(),
        p2=ball.Params()
    )
    proj.set(
        ball1=ball.create(x=ball.State(y_position=1.0, y_velocity=3.0), p=proj.p),
        ball2=ball.create(x=ball.State(y_position=2.0, y_velocity=2.0), p=proj.p),
        ball3=ball.create(x=ball.State(y_position=3.0, y_velocity=1.0), p=proj.p2),
        ball4=ball.create(x=ball.State(y_position=4.0, y_velocity=0.0), p=proj.p2),
    )
    del proj.__dict__["p"]
    del proj.__dict__["p2"]

    #proj.set(figs=dt.lnf("osdt_examples/figures/ball_figures.json"))#,figsolo=dt.ext("osdt_examples/figures/ball_fig1.json"))
    proj.otherfigs=[dt.lnf("osdt_examples/figures/ball_fig1.json"),
                    dt.lnf("osdt_examples/figures/ball_fig2.json"),
                    dt.lnf("osdt_examples/figures/ball_figures.json")]
    proj.set_process(cleanup=print_dict)
    return proj

if __name__ == "__main__":
    single_ball2()
