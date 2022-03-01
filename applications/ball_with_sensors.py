import osdt
from osdt_examples.models import sensor
from osdt_examples.models import ball

def main(y_position = 1.0,
        y_velocity = 0.0,
        gravity = 9.81,
        restitution = .95,
        pos_sample_period = 0.2,
        vel_sample_period = 0.2
    ):
    # create ball system
    ball_state = ball.State(y_position=y_position, y_velocity=y_velocity)
    ball_params = ball.Params(gravity=gravity, restitution=restitution)
    ball_system = osdt.create_system(x=ball_state,c=ball.C,f=ball.F,d=ball.D,g=ball.G,y=ball.Y_dict,id="ball",vars={ball.Params: ball_params})

    # create sensor systems
    pos_sensor_state = sensor.State(value=0.0,timer=0.0)
    pos_sensor_params = sensor.Params(sample_period=pos_sample_period,sample_field="y_position")
    pos_sensor = osdt.create_system(x=pos_sensor_state, c=sensor.C, f=sensor.F, d=sensor.D, g=sensor.G,u=sensor.U, id="pos_sensor",vars={sensor.Params: pos_sensor_params})
    vel_sensor_state = sensor.State(value=0.0,timer=0.0)
    vel_sensor_params = sensor.Params(sample_period=vel_sample_period,sample_field="y_velocity")
    vel_sensor = osdt.create_system(x=vel_sensor_state, c=sensor.C, f=sensor.F, d=sensor.D, g=sensor.G, u=sensor.U, id="vel_sensor",vars={sensor.Params: vel_sensor_params})

    # connect the sensors
    pos_sensor.set(sensor.INPUT, ball)
    vel_sensor.set(sensor.INPUT, ball)

    # run the environment
    osdt.run()

    # create the figure
    figure1 = osdt.create_figure(1200, 800, layout=[[1], [2]],
                                 title="Bouncing Ball with Sensors")
    figure1.plot(1, "y_position")
    figure1.plot(1, "value", system="pos_sensor")
    figure1.plot(2, "y_velocity")
    figure1.plot(2, "value", system="vel_sensor")
    figure1.export("figure1",format=".png")


    osdt.display()
