import osdt,sys

#if len(sys.argv)>2:

 #   osdt.utils.create_script_argfile(sys.argv[1],sys.argv[2])
#else:
if sys.argv[1] == "make":
    osdt.utils.create_script_argfile(sys.argv[2], sys.argv[3])
else:
    dat=osdt.utils.run_script(*sys.argv[1:])
print(dat)