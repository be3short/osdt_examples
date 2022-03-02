import osdt
from osdt_examples.models import point_mass

sun_mass = 1.989 * pow(10,30)
planet_masses = {
"jupiter": 1.8986*pow(10,27),
"saturn": 5.6846*pow(10,26),
"neptune": 10.243*pow(10,25),
"uranus": 8.6810 *pow(10,25),
"earth": 5.9736 *pow(10,24),
"venus": 4.8685 *pow(10,24),
"mars": 6.4185 *pow(10,23),
"mercury": 3.3022 *pow(10,23)
}

planet_distances = {
"mercury": 57900000000.0,
"venus": 108200000000.0,
"earth": 149600000000.0,
"mars": 227900000000.0,
"jupiter": 778600000000.0,
"saturn": 1433500000000.0,
"uranus": 2872500000000.0,
"neptune": 4495100000000.0,
}

planet_velocities = {
"mercury":	47900.0,
"venus":	35000.0,
"earth":	29800.0,
"mars":	    24100.0,
"jupiter":	13100.0,
"saturn":	9700.0,
"uranus":	6800.0,
"neptune":	5400.0
}



def defaults():
    osdt.set_configuration(time=10000000.0, jumps=10)
    osdt.set_integrator(osdt.get_configuration().integrator_type, max_step=100.0)

def main():
    sun = point_mass.create(x_position=0.1, y_position=0.1, x_velocity=0.0, y_velocity =0.0, mass=sun_mass, id="sun")
    for planet in planet_masses:
        print(planet_masses)
        planet = point_mass.create(x_position=planet_distances[planet], y_position=0.1, x_velocity=0.0,
                                y_velocity=planet_velocities[planet], mass=float(planet_masses[planet]), id=planet)

    point_mass.connect_all_masses()
    osdt.run()
    xyfig = osdt.create_figure(width=1200, height=800, layout=[[1]], title="Point Mass Interaction",dpi=100 )
    xyfig.plot(1,x="x_position",y="y_position",max_points=2000)
    xyfig.export("xy_figure",format="png")
    #xyfig.plot(1,"y_position")

    osdt.display()
