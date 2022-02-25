import osdt
from osdt_examples.models import timer

def main():
    timer_state = timer.State(value=0.0)
    timer_params = timer.Params(interval=1.0)
    timer_system = osdt.create_system(x=timer_state,c=timer.C,f=timer.F,d=timer.D,g=timer.G,id="timer",vars={timer.Params: timer_params})
    osdt.run(time=10.0,jumps=100)
    figure1(export_path=None,export_format="png")

def figure1(export_path=None,export_format="png"):
    figure1 = osdt.create_figure(1200,800,layout=[[1]],title="Timer")
    figure1.plot(1,"value")
    figure1.export(export_path,format=export_format)
    return figure1

def create_opfile():
    op = osdt.constructor.OpfileBuilder()
    op.add_sys("timer",timer,timer.State(),vars={timer.Params: timer.Params()})
    op.add_func(None, osdt.run)
    op.add_file("figure","osdt_examples/timer_fig.yaml")
    op.create_opfile("timer_opfile")

if __name__ == "__main__":
    create_opfile()
    #main()