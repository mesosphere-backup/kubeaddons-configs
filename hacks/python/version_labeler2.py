from os import listdir
from os.path import isfile, join
import argparse
import ruamel.yaml.util

yaml = ruamel.yaml.YAML()

parser = argparse.ArgumentParser(description='Append Version annotation to addons.')
parser.add_argument('-p', '--path', required=True, help='path where template files should be found')
parser.add_argument('--remove', action='store_true', help='remove version from annotations')
args = parser.parse_args()

CONST_METADATA_KEY = "metadata"
CONST_LABEL_KEY = "labels"
CONST_VERSION_LABEL = "kubeaddons.mesosphere.io/repository-name"

addonFiles = [f for f in listdir(args.path) if isfile(join(args.path, f))]

for file in addonFiles:
    addon = open(args.path + file, "r+")
    addonyaml = yaml.load(addon)
    yaml.indent(mapping=2, sequence=4, offset=2)

    if args.remove:
        try:
            del addonyaml[CONST_METADATA_KEY][CONST_LABEL_KEY][CONST_VERSION_LABEL]
        except KeyError:
            print("key not found in file {}, found error {}".format(file, KeyError))
    else:
        addonyaml[CONST_METADATA_KEY][CONST_LABEL_KEY][CONST_VERSION_LABEL] = "kubeaddons-configs"
        addon.seek(0)
        addon.write("---\n")
        yaml.dump(addonyaml, addon)
