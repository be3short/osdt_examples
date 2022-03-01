import argparse

import osdt
import yaml
from osdt_examples.models import ball,sensor,timer

def main(
        workspace="osdt_examples/applications/workspace/workspace.yaml"
    ):

    pac=osdt.utils.read_yaml_file(osdt.get_path(workspace))
    print(pac)

if __name__ == "__main__":
    main()

