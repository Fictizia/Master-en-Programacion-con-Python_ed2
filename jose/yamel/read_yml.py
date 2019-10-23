# -*- coding: utf-8 -*-
import yaml
import io

# Read YAML file
with open("data.yaml", 'r') as stream:
    data_loaded = yaml.safe_load(stream)

    print(data_loaded['a list'])
