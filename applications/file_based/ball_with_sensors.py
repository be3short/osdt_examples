import traceback

import osdt
from osdt_examples.models import sensor
from osdt_examples.models import ball

def main(
        system_file="osdt_examples/applications/file_based/ball_with_sensors.yaml"
    ):


    # load system arg file
    args = osdt.load(system_file)

    # create ball system
    ball_state = ball.State(**args["ball"]["state"])
    ball_params = ball.Params(**args["ball"]["params"])
    ball_system = osdt.create_system(x=ball_state, vars={ball.Params: ball_params},**args["ball"]["model"])

    # create position sensor
    pos_sensor_state = sensor.State(**args["pos_sensor"]["state"])
    pos_sensor_params = sensor.Params(**args["pos_sensor"]["params"])
    pos_sensor = osdt.create_system(x=pos_sensor_state, vars={sensor.Params: pos_sensor_params}, **args["pos_sensor"]["model"])

    # create velocity sensor
    vel_sensor_state = sensor.State(**args["vel_sensor"]["state"])
    vel_sensor_params = sensor.Params(**args["vel_sensor"]["params"])
    vel_sensor = osdt.create_system(x=vel_sensor_state, vars={sensor.Params: vel_sensor_params}, **args["vel_sensor"]["model"])

    # connect the sensors
    pos_sensor.set(sensor.INPUT, ball_system)
    vel_sensor.set(sensor.INPUT, ball_system)

    # run the environment
    osdt.run()

    # create the figure
    figure1 = osdt.create_figure(1200, 800, layout=[[1], [2]],
                                 title="Bouncing Ball with Sensors")

    figure1.plot(1, "y_position")
    figure1.plot(1, "value", system=pos_sensor)
    figure1.plot(2, "y_velocity")
    figure1.plot(2, "value", system=vel_sensor)

    figure1.export("figure1",format="png")


    osdt.display()
  #  except:
 #       osdt.get_logger().error("fail"+traceback.format_exc())
if __name__=="__main__":
    main()