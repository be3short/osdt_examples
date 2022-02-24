import osdt
from osdt_examples.models import ball

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

if __name__ == "__main__":
    main()