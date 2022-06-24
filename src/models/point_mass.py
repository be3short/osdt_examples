import osdt
import math

ALL_MASSES = "ALL_MASSES"

class State:
    def __init__(self,x_position=0.0, y_position=0.0, x_velocity=0.0, y_velocity = 0.0):
        self.x_position = x_position
        self.y_position = y_position
        self.x_velocity = x_velocity
        self.y_velocity= y_velocity

class Params:
    def __init__(self, mass = 1.0 ,gravity=0.00000000006674 ):
        self.mass = mass
        self.gravity=gravity


def C(x, hs):
    return True


def F(x, x_dot, sys):
    point_masses=sys.u()
    x_force_total = 0
    y_force_total = 0

    for point_mass in point_masses:
        # define other point mass state as y
        y = point_mass.x()
        distance = math.sqrt((x.x_position - y.x_position) * (x.x_position - y.x_position)
                             + (x.y_position - y.y_position) * (x.y_position - y.y_position));

        x_distance = y.x_position - x.x_position;
        y_distance = y.y_position - x.y_position;
        angle = math.atan2(y_distance, x_distance);
        if distance < 50: distance = 50.0
        force = sys.params.gravity * (sys.params.mass * point_mass.params.mass) / math.pow(distance, 2)
        x_force = force * math.cos(angle);
        y_force = force * math.sin(angle);
        x_force_total = x_force_total + x_force
        y_force_total = y_force_total + y_force

    x_dot.x_velocity = x_force_total / sys.params.mass
    x_dot.y_velocity = y_force_total / sys.params.mass
    x_dot.x_position = x.x_velocity
    x_dot.y_position = x.y_velocity
   # print("envtime="+str(osdt.get_environment_time())+" "+str(x.__dict__))

def CEarth(x, sys):
    system = sys.all_masses[0]
    earth = system.x()
    dist = compute_distance(x, earth)
    if dist < 6361000:# and x.y_velocity==0.0:
        return False
    else:
        return True


def D(x,sys):
    system=sys.all_masses[0]
    earth=system.x()
    dist=compute_distance(x,earth)
    if dist < 6361000 and x.y_velocity>0:
        return True
    else:
        return False


def G(x,x_plus,sys):
    system=sys.all_masses[0]
    earth=system.x()
    dist=compute_distance(x,earth)
    #if dist < 6361000:
    print("jump")
    x_plus.x_velocity=0.0
    x_plus.y_velocity=0.0
    x_plus.x_position=x.x_position*.98
    x_plus.y_position =x.y_position*.98


def U(x, sys, *args, **argmap):
    # get all other point masses
    point_masses = sys.all_masses
    return point_masses




def compute_distance(x,y):
    distance = math.sqrt((x.x_position - y.x_position) * (x.x_position - y.x_position)
                         + (x.y_position - y.y_position) * (x.y_position - y.y_position));
    return distance


def connect_all_masses():
    all_point_masses = []
    for system in osdt.get_systems().values():
        system: osdt.system.System=system
        if type(system.state) == State:
            all_point_masses.append(system)
    for pointmass in all_point_masses:
        other_masses = []
        for other_mass in all_point_masses:
            if other_mass != pointmass:
                other_masses.append(other_mass)
        pointmass.all_masses=other_masses


def FDrag(x,x_dot,sys):
    point_masses = sys.u()
    x_force_total = 0
    y_force_total = 0
    system = sys.all_masses[0]
    earth = system.x()
    dist = compute_distance(x, earth)
   # if dist >= 6350000:
    for point_mass in point_masses:
        # define other point mass state as y
        y = point_mass.x()
        distance = math.sqrt((x.x_position - y.x_position) * (x.x_position - y.x_position)
                             + (x.y_position - y.y_position) * (x.y_position - y.y_position));

        x_distance = y.x_position - x.x_position;
        y_distance = y.y_position - x.y_position;
        angle = math.atan2(y_distance, x_distance);
        if distance < 5: distance = 5
        force = sys.params.gravity * (sys.params.mass * point_mass.params.mass) / math.pow(distance, 2)
        x_force = force * math.cos(angle);
        y_force = force * math.sin(angle);
        x_force_total = x_force_total + x_force
        y_force_total = y_force_total + y_force

    x_force_total = x_force_total
    y_force_total = y_force_total



    x_dot.x_velocity = (x_force_total) / sys.params.mass
    x_dot.y_velocity = y_force_total / sys.params.mass
    x_dot.x_position = x.x_velocity
    x_dot.y_position = x.y_velocity


def create(x_position=1000.0, y_position=1000.0, x_velocity=0.0,
                      y_velocity=0.0, mass=1000.0, id="pointmass"):
    state = State(x_position, y_position, x_velocity, y_velocity)
    params = Params(mass)
    system = osdt.create_system(x=state, c=C, f=F, u=U, vars={Params: params}, id=id)
    return system


def create(x=State(),params=Params(),c=C,f=F,d=D,g=G,u=U,y=None,initialize=None,routine=None): # create a new system
    return osdt.create_system(x=x,vars={Params: params},c=c,f=f,d=d,g=g,u=u,y=y,initialize=initialize,routine=routine)

