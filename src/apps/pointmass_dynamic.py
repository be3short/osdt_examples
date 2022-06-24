import osdt as dt #as dt

from dt_examples.models import point_mass as pm

def figure():
    xyfig = dt.create_fig(layout=[[1]], title="Point Mass Interaction", dpi=130)
    xyfig.plot(1, x="x_position", y="y_position")


def setup(app):
    pm.connect_all_masses()
    dt.get_config().integrator.max_step=100.0
    dt.get_config().run.time=10000.0


def create_masses(app):
    for mass_num in range(0,app.num_masses):
        print(mass_num)
        state=pm.State(
            x_position=dt.random(-app.position_range,app.position_range),
            y_position=dt.random(-app.position_range, app.position_range),
            x_velocity = dt.random(-app.velocity_range, app.velocity_range),
            y_velocity=dt.random(-app.velocity_range, app.velocity_range)
        )
        print(state.__dict__)
        params=pm.Params(mass=dt.random(app.min_mass,app.max_mass))
        new_mass = dt.system.create_sys(pm,id="mass_{}".format(mass_num),x=state,params=params,**app.model)
        app.set(new_mass.get_id(),new_mass)
        dt.add_systems(new_mass)

@dt.main
def pointmass_app():
    app=dt.app(
        num_masses=10,
        model=dt.create_sys(pm).properties.get_model(),
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
