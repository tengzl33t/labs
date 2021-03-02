import yaml
import os

with open("yaml_data.yaml") as f:
    list_doc = yaml.load(f, Loader=yaml.FullLoader)

for sense in list_doc:
    if sense["name"] == "sense2":
        print(sense["type"])
        print(sense["value"])

