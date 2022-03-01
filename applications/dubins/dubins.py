import osdt
from osdt_examples.models import dubins_controller
from osdt_examples.models import dubins_vehicle

def main2(
    x_position= 0.0,
    y_position= 0.0,
    orientation= 0.5,
    velocity= 0.5,
    ):
    vehicle_state = dubins_vehicle.State(x_position=x_position,y_position=y_position,orientation=orientation)
    vehicle = osdt.create_system(x=vehicle_state, c=dubins_vehicle.C,f=dubins_vehicle.F,u=dubins_vehicle.U,y=dubins_vehicle.Y)

    controller_state = dubins_controller.State(velocity=velocity)
    controller = osdt.create_system(x=controller_state,d=dubins_controller.D,g=dubins_controller.G,u=dubins_controller.U,y=dubins_controller.Y)

    vehicle.set(dubins_vehicle.CONTROLLER,controller)
    controller.set(dubins_controller.VEHICLE,vehicle)

    osdt.run()

    # create a figure
    fig = osdt.create_figure(layout=[[1, 2, 5], [3, 4, 5]],
                             title="Dubins Vehicle",title_align=True,
                             width=1600, height=800)
    # configure the subplots
    fig.configure_subplot(1,title="X Position",y_axis="D")
    fig.configure_subplot(2,title="Orientation")
    fig.configure_subplot(3,title="Y Position")
    fig.configure_subplot(4,title="Turn State")
    fig.configure_subplot(5,title="X Position vs Y Position")
    # plot the data
    fig.plot(1,"x_position")
    fig.plot(2,"orientation")
    fig.plot(3,"y_position")
    fig.plot(4,"turn")
    fig.plot(5,x="x_position", y="y_position")

    fig.export("figure1",format="png")
    # display figure
    osdt.display()

    osdt.save_environment("environment")

def main(
    sys=[],
    ):
    for syst in sys:
        osdt.load(syst)

    # create a figure
    fig = osdt.create_figure(layout=[[1, 2, 5], [3, 4, 5]],
                             title="Dubins Vehicle",title_align=True,
                             width=1600, height=800)
    # configure the subplots
    fig.configure_subplot(1,title="X Position",y_axis="D")
    fig.configure_subplot(2,title="Orientation")
    fig.configure_subplot(3,title="Y Position")
    fig.configure_subplot(4,title="Turn State")
    fig.configure_subplot(5,title="X Position vs Y Position")
    # plot the data
    fig.plot(1,"x_position")
    fig.plot(2,"orientation")
    fig.plot(3,"y_position")
    fig.plot(4,"turn")
    fig.plot(5,x="x_position", y="y_position")

    fig.export("figure1",format="png")
    # display figure
    osdt.display()

    osdt.save_environment("environment")

def create_opfile():
    fb=osdt.get_opfile_builder()
    fb.add_sys("dubins1",dubins_vehicle,dubins_vehicle.State )
    fb.add_sys("controller1",dubins_controller,dubins_controller.State )
    fb.add_connections(2)
    fb.add_func(None,osdt.run)
    fb.add_fig("figure",layout=[[1,2,5,5],[3,4,5,5]])
    fb.create_opfile("applications/dubins/dubins.yaml")


if __name__ == "__main__":
    create_opfile()