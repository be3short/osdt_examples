import sys

import osdt as dt
from osdt_examples.models import simple_timer

@dt.task
def figure():
    fig = dt.create_fig(layout=[[1]])
    fig.plot(1,"value")
    return fig

@dt.task
def runz(x=simple_timer.State(),
        p=simple_timer.Params()):
    timer_sys = simple_timer.create(x=x,p=p)
    dt.run()
    fig = figure()
    dt.display()

def app_setup(app):
    print("startup: {}".format(app))

def app_cleanup(app):
    print("cleanup: {}".format(app))

@dt.task
def app():
    app = dt.app(
        timer_sys=simple_timer.create(),
        fig = figure()
    )
    app.set_process(setup=app_setup, cleanup=app_cleanup)
    return app

@dt.task
def app_ext():
    app = dt.app(
        timer_sys=simple_timer.create(),
        fig = dt.lnf("project1/components/figure.json")
    )
    return app


@dt.task
def app_long():
    pass
    '''
    app = dt.app(
        x=simple_timer.State(),
        p=simple_timer.Params()
    )
    app.set(
        timer_sys = simple_timer.create(x=app.x,p=app.p)
    )
    '''

@dt.task
def timer_app():
    app = dt.app(
        timer1=dt.build_sys(simple_timer),
        timer2=simple_timer.create(),
        fig=figure()
    )
    return app






