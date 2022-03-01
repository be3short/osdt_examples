import argparse
import json

import osdt
import yaml
from osdt_examples.models import ball,sensor,timer

def main(
        workspace="osdt_examples/applications/workspace/workspace.yaml"
    ):

    pac=osdt.utils.read_yaml_file(osdt.get_path(workspace))
    print("Workspace: "+str(workspace)+"\n-----------------------------------")
    print(json.dumps(pac,indent=4))

if __name__ == "__main__":
    main()

