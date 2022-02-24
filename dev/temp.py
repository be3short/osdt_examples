import inspect

import osdt.utils

from osdt_example.models import ball
from osdt_example.models import sensor

class Const:
    def __init__(self):
        self.systems = {}
    def add_system(self,name, module,state,*params):#,**vars):

        pz=[]
        if type(module) is not str:

            module=str(module.__dict__["__name__"])
            state = str(state.__name__)
        for p in params:
            pz.append(p.__name__)

        sys=osdt.utils.generate_sys_args(module,state,*pz)
        self.systems[name]=(sys)

    def write(self, path="dddddd"):
        osdt.utils.write_yaml_file(self.systems,path,overwrite=True)
      #  print(sys)

def get_systems():
    c=Const()#
    c.add_system("ball",bouncing_ball,bouncing_ball.State,bouncing_ball.Params)
    c.add_system("pos_sensor",sample_hold_sensor, sample_hold_sensor.State,
                 sample_hold_sensor.Params  )
    c.add_system("vel_sensor",sample_hold_sensor,sample_hold_sensor.State,sample_hold_sensor.Params)
    c.write()
def tempt(ball, pos_sensor, vel_sensor):
    pos_sensor.set(ball,sample_hold_sensor.INPUT)
    vel_sensor.set(ball, sample_hold_sensor.INPUT)



print(get_systems())