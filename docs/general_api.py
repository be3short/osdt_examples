import osdt
from osdt_example.models import simple_timer

state = simple_timer.State(value=1.0)
params = simple_timer.Params(interval=1.0)
object = osdt.create_system(x=state, c=simple_timer.C, f=simple_timer.F, d=simple_timer.D, g=simple_timer.G, u=simple_timer.U,
                          y=simple_timer.Y, vars={simple_timer.PARAMS: params}, id="Timer")

#osdt.load_objfile("objfile.yaml")

osdt.save(object, "saved_object")

osdt.load("saved_object.obj")