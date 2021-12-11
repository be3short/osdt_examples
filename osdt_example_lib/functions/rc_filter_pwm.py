import osdt
from osdt_example_lib.models import rc_filter_pwm

def figure1():
    # create a figure
    fig = osdt.create_figure(layout=[[1], [2], [3]], title="RC System",
                           width=1600, height=600)

    fig.subplot(1).plot("v_out", max_points=4000)
    fig.subplot(2).plot("v_in", max_points=4000)
    fig.subplot(3).plot("toggle_timer", max_points=4000)

def adjust_integrator_step(system_id):
    rc_sys=osdt.get_system(system_id)
    osdt.set_integrator("vode",max_step=(1.0/(rc_sys.get(rc_filter_pwm.PARAMS).frequency*100)))
