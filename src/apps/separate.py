import copy
import inspect
import sys

import osdt
import osdt as dt
from osdt_examples.models import ball
from osdt_examples.apps import sh_sensor
from osdt_examples.apps.ball import create_random_balls
'''
attach_sensors(
        measured_sys = None,
        measured_values = [],
        sensor_params = sensor.Params()):
'''

@dt.app_def
def app1():
    app = dt.app(
        fig=app1_plot1(),
        balls=[]
    )
    app.add_tasks(
        app1plot=app1_plot1,
        create_balls_1=create_random_balls,
        create_balls_2=create_random_balls,
        dump=example_script
    )


    print(app.dump)
    app.run_func = app1_run2

    return app

def example_script(fixed1,fixed2,*argz,val1=True,val2=True,**kwargs):##fixed1,fixed2,*argz,val1=True,val2=True,**kwargs):
    return (fixed1,fixed2,argz,val1,val2,kwargs)

def app1_run2(app:dt.Application):
    print(app.__dict__)
    ret=app.run_tasks(app.create_balls_1,app.create_balls_2 )
    print(app.dump.__dict__)
    app.dumps=app.dump.run()#dumps=app.dump.run()
    app.balls=[]
    app.balls.extend(app.create_balls_1.run().__dict__.values())
    app.balls.extend(app.create_balls_2.run().__dict__.values())
    for ball_sys in app.balls:
        sh_sensor.attach_sensors(ball_sys, list(ball_sys.state.__dict__.keys()))
    dt.run(jumps=50)
    app1_plot1()
    dt.core.get_objects()
    print(app.dumps)

def app1_run(app):
    app.run_tasks(
        balls1=app.create_balls_1,
        balls2=app.create_balls_2
    )
    app.balls = {i: app.balls1.__dict__[i] for i in app.balls1.__dict__}
    for ballid in app.balls2.__dict__:
        app.balls[ballid] = app.balls2.__dict__[ballid]

    for ballid in app.balls:
        ball_sys = app.balls[ballid]
        sh_sensor.attach_sensors(ball_sys, list(ball_sys.state.__dict__.keys()))

    dt.run(jumps=400)

    return app

def app1_plot1():
    fig = ball.plot()  # .display()
    fig.get_subplot(1).legend = False
    fig.get_subplot(2).legend = False
    fig.plot(1, "value", system="*y_position*")
    fig.plot(2, "value", system="*y_velocity*")
    return fig


'''
@dt.task
class App1(dt.Application):
    def __init__(self):
        self.run_func=None
        self.add_tasks(
            create_balls_1=create_random_balls,
            create_balls_2=create_random_balls,
        )



    def run(self,display=False):
        self.call(
            balls1=self.create_balls_1,
            balls2=self.create_balls_2
        )
        self.balls={i:self.balls1.__dict__[i] for i in self.balls1.__dict__}
        for ballid in self.balls2.__dict__:
            self.balls[ballid]=self.balls2.__dict__[ballid]

        for ballid in self.balls:
            ball_sys=self.balls[ballid]
            sh_sensor.attach_sensors(ball_sys,list(ball_sys.state.__dict__.keys()))

        print(dt.get_systems())
        dt.run(jumps=300)
        self.fig=ball.plot()#.display()
        self.fig.get_subplot(1).legend=False
        self.fig.get_subplot(2).legend=False
        self.fig.plot(1,"value",system="*y_position*")
        self.fig.plot(2,"value",system="*y_velocity*")
        if display: dt.display()
'''
'''
if __name__ == "__main__":
    if len(sys.argv)<2:
        App1().save("app1")
    else:
        app=dt.load(sys.argv[1])
        app.run()

'''