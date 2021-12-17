import os

from setuptools import setup
import sys
# dev: python .\setup.py develop
# regular python .\setup.py install[
# uninstall: python setup.py develop --uninstall


if __name__ == "__main__":
    library_path = os.path.abspath(sys.argv[1])
    library_package = os.path.basename(library_path)
    sys.argv[1]="develop"
    sys.argv.append("--uninstall")
    os.chdir(os.path.dirname(os.path.abspath(library_path)))
    print("current dir = "+os.getcwd())
    print("package name = "+str(library_package))
    print("sysargv[1]="+str(sys.argv[1]))
    if True:
        setup(
            name=library_package,
            version='1.0',
            long_description=__doc__,
            packages=[library_package],
            include_package_data=True,
            zip_safe=False
        )