import json
from ruamel.yaml import YAML

in_file = "show_ip_int_br.yaml"
out_file = "show_ip_int_br.json"

yaml = YAML(typ="safe")

with open(in_file, "r") as i:
    data =yaml.load(i)

with open(out_file, "w") as o:
    json.dump(data, o, indent=4)