import osdt
from osdt_examples.models import dubins_controller
from osdt_examples.models import dubins_vehicle

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