import osdt
new_configuration = osdt.configuration.GeneralConfiguration()

osdt.set_configuration(new_configuration)

osdt.set_configuration(jump_flow_priority=osdt.FLOW_PRIORITY)

osdt.set_integrator("vode", max_step = 0.1)

osdt.add_systems(system_1, system_2, system_n)

osdt.run(time=20.0, jumps=20)

osdt.save_environment("environment_file_directory")

environment = osdt.load_environment("environment_file_directory", set_global=True, load_configuration=True)

environment = osdt.get_environment()

osdt.get_time()

osdt.get_jumps()

osdt.set_environment(new_environment)


environment.save("environment_file_directory", overwrite=False)

environment.load_env()

osdt.get_systems()



osdt.get_systems()

osdt.get_system("system_id")

osdt.set("object_key", object_value)

osdt.get("object_key")

osdt.get_data(points=-1)