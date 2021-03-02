import yaml
from pprint import pprint

yml_example = open("change_host_name.yaml").read()
# pprint(yml_example)

yaml_python = yaml.load(yml_example, Loader=yaml.FullLoader)
print(yaml.dump(yaml_python))
