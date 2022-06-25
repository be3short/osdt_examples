import osdt as dt
from osdt_examples import simple_pendulum

def func(arg1, args, somearg=1):
    print(arg1)

def scratch():

    o = dt.obj(
        func_call=func,
        pendulum=simple_pendulum.pendulum_app,
    )




    o.add_outputs(
        figure1=figure2,
        figure2=figure2
    )

