# model template
# arguments: x = state, system = dynamical system, x_dot = state derivative,
# x_plus = post-jump state, *args = non-keyword args, **argmap = keyword args
import osdt as dt


class State(dt.UniversalObject):  # state object
    def __init__(self, value=0.0):
        self.value = value


class Params(dt.UniversalObject):  # parameters object
    def __init__(self, interval=1.0):
        self.interval = interval


def C(x, system):  # flow set (determine if state in continuous domain)
    return x.value >= 0.0


def F(x, x_dot, system):  # flow map (compute continuous dynamics)
    x_dot.value = -1.0


def D(x, system):  # jump set (determine if state in discrete domain)
    return x.value <= 0.0


def G(x, x_plus, system):  # jump map (compute discrete dynamics)
    x_plus.value = system.params.interval


def U(x, system, *args, **argmap):  # input map (determine input)
    return None


def Y(x, system, *args, **argmap):  # output map (determine output)
    return None


def initialize(system):  # initialize the system when the environment starts
    pass


@dt.task
def create(state=State(), params=Params(), c=C, f=F, d=D, g=G, u=U, y=Y, id="simple_timer"):  # create a new system
    return dt.create_sys(x=state, c=c, f=f, d=d, g=g, u=u, y=y, params=params, id=id)
