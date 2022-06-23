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

@dt.task
def app1():
    app = dt.app()
    app.add_tasks(
        create_balls_1=create_random_balls,
        create_balls_2=create_random_balls
    )
    app.run_func = app1_run
    return app
def app1_run(app):
    app.call(
        balls1=app.create_balls_1,
        balls2=app.create_balls_2
    )
    app.balls = {i: app.balls1.__dict__[i] for i in app.balls1.__dict__}
    for ballid in app.balls2.__dict__:
        app.balls[ballid] = app.balls2.__dict__[ballid]

    for ballid in app.balls:
        ball_sys = app.balls[ballid]
        sh_sensor.attach_sensors(ball_sys, list(ball_sys.state.__dict__.keys()))
    app1_plot1(app)
    return app

def app1_plot1(app):
    dt.run(jumps=300)
    app.fig = ball.plot()  # .display()
    app.fig.get_subplot(1).legend = False
    app.fig.get_subplot(2).legend = False
    app.fig.plot(1, "value", system="*y_position*")
    app.fig.plot(2, "value", system="*y_velocity*")
    dt.display()

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


if __name__ == "__main__":
    if len(sys.argv)<2:
        App1().save("app1")
    else:
        app=dt.load(sys.argv[1])
        app.run()