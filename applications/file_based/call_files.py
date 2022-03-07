import osdt
from osdt_examples.models import ball, timer, point_mass,sensor,heater_system,heater_controller,dubins_vehicle,dubins_controller
from osdt import load_obj



def main(path="osdt_examples/sysfiles/argtest3.yaml", key="system" ):  ##.ball.__name__, read_file=""

    vehicle = load_obj(path,"dubins_vehicle", state=dubins_vehicle.State(
        x_position=0.0,y_position=0.0,orientation=0.0))

    controller = load_obj(path,"dubins_controller",state=dubins_controller.State(velocity=0.75,turn=1.0))

    vehicle.set(dubins_vehicle.CONTROLLER,controller)

    controller.set(dubins_controller.VEHICLE,vehicle)

    osdt.run()

    osdt.construct_figures("osdt_examples/sysfiles/figure.yaml","figure5")


def main5(path="osdt_examples/sysfiles/argtest3.yaml", key="system" ):  ##.ball.__name__, read_file=""

    heater_sys = load_obj(path,"heater_system")

    controller_sys = load_obj(path, "heater_controller")

    heater_sensor = load_obj(path, "sensor", input_sys=heater_sys, id="heater_sensor")

    controller_sensor = load_obj(path, "sensor", input_sys=controller_sys, id="controller_sensor")

    heater_sys.set(heater_system.CONTROLLER,controller_sensor)

    controller_sys.set(heater_controller.TEMPERATURE,heater_sensor)

    osdt.run()

    osdt.construct_figures("osdt_examples/sysfiles/figure.yaml","figure4")



def main3(path="osdt_examples/sysfiles/argtest3.yaml", key="system" ):  ##.ball.__name__, read_file=""

    heater_sys = load_obj(path,"heater_system")

    controller_sys = load_obj(path, "heater_controller")

    heater_sys.set(heater_system.CONTROLLER,controller_sys)

    controller_sys.set(heater_controller.TEMPERATURE,heater_sys)

    osdt.run()

    osdt.construct_figures("osdt_examples/sysfiles/figure.yaml","figure4")


def main2(path="osdt_examples/sysfiles/argtest3.yaml",
         key="system"):  ##.ball.__name__, read_file=""

    ball_sys = osdt.load_obj(path, key)  # ,params=p)

    pos_sensor = load_obj(path, "sensor", params=sensor.Params(
        sample_field="y_position"), input_sys=ball_sys, id="pos_sensor")

    vel_sensor = load_obj(path, "sensor", params=sensor.Params(
        sample_field="y_velocity"), input_sys=ball_sys, id="vel_sensor")

    osdt.run()

    osdt.construct_figures("osdt_examples/sysfiles/figure.yaml", "figure1")
