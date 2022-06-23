import copy
import inspect

import osdt
import osdt as dt
from osdt_examples.models import ball


@dt.task
def create_random_balls(
        num_balls = 1,
        min_state = ball.State(),
        max_state = ball.State(),
        ball_params = ball.Params()):
    min_state=min_state.copy()
    max_state=max_state.copy()
    balls = dt.var()
    for ind in range(0, num_balls):
        y_position = dt.random(min_state.y_position, max_state.y_position)
        y_velocity = dt.random(min_state.y_velocity, max_state.y_velocity)
        ball_sys=ball.create(x=ball.State(y_position, y_velocity),p=ball_params)
        balls.set(ball_sys.get_id(),ball_sys)

    return balls


def create_app(app=None):
    if app is None:
        app = osdt.app()

        add_tasks(app,create_balls=create_random_balls,
                      create_balls2=create_random_balls)
        app.save("funcap2")
        return app
    else:

        call(app,balls1=app.create_balls,
                 balls2=app.create_balls2)


def add_tasks(app,**calls):
    for callvar in calls:
        func=calls[callvar]
  #  app=osdt.app()
        script=[]
        args=inspect.getfullargspec(create_random_balls)
        keys = args.args
        funcargs={}#{"$call":create_random_balls}
        defaults = args.defaults
        for ind in range(0,len(defaults)):
            funcargs[keys[ind]]=copy.deepcopy(defaults[ind])
        script.append({"$call":create_random_balls,"$args":funcargs})
        app.set(callvar,{"$call":create_random_balls,"$args":funcargs})

def call(app,**calls):
    for retvar in calls:
        callvar=calls[retvar]
        #if callvar in app.__dict__:
        entry = callvar#app.__dict__[callvar]

        # print(entry)
        call = entry["$call"]
        args = entry["$args"]
        retval = call(**args)
        app.set(retvar,retval)
    #print(args)
    #print(app.__dict__)
  #  app.save("funcapp")
  #  return app
    '''
    if app is None: app = dt.app(
        func=attach_sensors
        measured_sys = None,
        measured_values = [],
        sensor_params = sensor.Params()
    )
    else:
    '''


if __name__ == "__main__":
    #App1().save("app1")
    app=create_app()
    #app=dt.load("funcap2.json")
    #create_app(app)
    #app.run()
    #ball.plot().display()
   # app.save("postfunc")

