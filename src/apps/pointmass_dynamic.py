import osdt #as dt

from osdt_examples.models import point_mass as pm

def figure():
    xyfig = osdt.create_fig(layout=[[1]], title="Point Mass Interaction", dpi=130)
    xyfig.plot(1, x="x_position", y="y_position")


def setup(app):
    pm.connect_all_masses()
    osdt.get_config().integrator.max_step=100.0
    osdt.get_config().run.time=10000.0


def create_masses(app):
    for mass_num in range(0,app.num_masses):
        print(mass_num)
        state=pm.State(
            x_position=osdt.random(-app.position_range,app.position_range),
            y_position=osdt.random(-app.position_range, app.position_range),
            x_velocity = osdt.random(-app.velocity_range, app.velocity_range),
            y_velocity=osdt.random(-app.velocity_range, app.velocity_range)
        )
        print(state.__dict__)
        params=pm.Params(mass=osdt.random(app.min_mass,app.max_mass))
        new_mass = osdt.create_sys(pm,id="mass_{}".format(mass_num),x=state)#,params=params,**app.model)
        app.set(new_mass.get_id(),new_mass)

@osdt.app_def
def pointmass_app():
    app=osdt.app(
        num_masses=10,
        velocity=0.1,
        min_mass=5e9, max_mass=5e10,
        position_range=10000.0,
        velocity_range=10.0,
        fig = figure()
    )
    app.add_setup(create_masses,setup)
    return app

if __name__ == "__main__":
    app = pointmass_app()
    app.run(True)
