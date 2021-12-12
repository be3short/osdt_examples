import sys
sys.path.append("..")
from osdt_example.models import dubins_vehicle,dubins_controller
import osdt

def run():
    # create the vehicle1 and controller1 systems
    vehicle1 = osdt.create_system(x=dubins_vehicle.State(x_position=0.0, y_position=0.0, orientation=0.6),c=dubins_vehicle.C,f=dubins_vehicle.F,u=dubins_vehicle.U_convert,y=dubins_vehicle.Y)
    controller1 =  osdt.create_system(x=dubins_controller.State(turn=1.0,velocity=0.5),d=dubins_controller.D,g=dubins_controller.G,u=dubins_controller.U_convert,y=dubins_controller.Y)
    # create the vehicle2 and controller2 systems
    vehicle2 = osdt.create_system(x=dubins_vehicle.State(x_position=0.0, y_position=0.0, orientation=0.3),c=dubins_vehicle.C,f=dubins_vehicle.F,u=dubins_vehicle.U_convert,y=dubins_vehicle.Y)
    controller2 = osdt.create_system(x=dubins_controller.State(turn=1.0,velocity=0.75),d=dubins_controller.D,g=dubins_controller.G,u=dubins_controller.U_convert,y=dubins_controller.Y)

    # connect controller1 and vehicle1
    vehicle1.set(dubins_vehicle.CONTROLLER,controller1)
    controller1.set(dubins_controller.VEHICLE,vehicle1)
    # connect controller2 and vehicle2
    vehicle2.set(dubins_vehicle.CONTROLLER,controller2)
    controller2.set(dubins_controller.VEHICLE,vehicle2)

    # run the environment
    osdt.run(t=50.0, j=60)

    # create a figure
    fig = osdt.create_figure(layout=[[1,2,5,5],[3,4,5,5] ],title="Thermostat Controlled Temperature",
                           width=1600, height=600)
    # configure the subplots
    fig.subplot(1).edit_config(title="X Position")
    fig.subplot(2).edit_config(title="Y Position")
    fig.subplot(3).edit_config(title="Orientation")
    fig.subplot(4).edit_config(title="Turn State")
    fig.subplot(5).edit_config(title="X Position vs Y Position")
    # plot the data
    fig.subplot(1).plot("x_position")
    fig.subplot(2).plot("y_position")
    fig.subplot(3).plot("orientation")
    fig.subplot(4).plot("turn")
    fig.subplot(5).plot(x="x_position",y="y_position")
    # display figure
    osdt.display()








if __name__ == "__main__":
    run()