import osdt
import yaml
from osdt_examples.models import ball,sensor,timer

osdt.constructor.set_default_sys_opfile(ball,ball.State(), p={ball.Params: ball.Params()})
osdt.constructor.set_default_sys_opfile(timer,timer.State(), p={timer.Params: timer.Params()})
osdt.constructor.set_default_sys_opfile(sensor,sensor.State(), p={sensor.Params: sensor.Params()})

def main():
    ball_state = ball.State(y_position=1.0,y_velocity=0.0)
    ball_params = ball.Params(gravity=9.81,restitution=.95)
    ball_system = osdt.create_system(x=ball_state,c=ball.C,f=ball.F,d=ball.D,g=ball.G,y=ball.Y,id="ball",vars={ball.Params: ball_params})
    osdt.run(time=10.0,jumps=100)
    figure1()
    osdt.display()

def figure1(export_path=None,export_format="png"):
    figure1 = osdt.create_figure(1200,800,layout=[[1],[2]],title="Bouncing Ball")
    figure1.plot(1,"y_position")
    figure1.plot(2, "y_velocity")
    figure1.export(export_path,format=export_format)
    return figure1

conns={sys1:[key], sys2[key]}

def create_opfile():
    systems = {
        "ball1": ball,
        "sensor1":sensor,
        "timer1":timer
    }
    opfile_map = {}
    for system in systems:
        opfile = osdt.constructor.get_default_opfile(systems[system])
        opfile_map[system]=opfile["system"]

    print(yaml.safe_dump(opfile_map,sort_keys=False))

if __name__ == "__main__":
    create_opfile()


