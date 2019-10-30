from os import listdir
from os.path import isfile, join
from ruamel.yaml import YAML
import argparse

yaml = YAML()
yaml.preserve_quotes = True

parser = argparse.ArgumentParser(description='Place repository-name label to addons.')
parser.add_argument('-n', '--name', help='name of repository to use')
parser.add_argument('-p', '--path', required=True, help='path where addon files should be found')
parser.add_argument('--remove', action='store_true', help='remove repository-name label from addons')
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
        try:
            addonyaml[CONST_METADATA_KEY][CONST_LABEL_KEY][CONST_VERSION_LABEL] = args.name
            addon.seek(0)
            addon.write("---\n")
            yaml.dump(addonyaml, addon)
            addon.truncate()
        except Exception as Error:
            print("error found in file {}: {}".format(file, Error))
