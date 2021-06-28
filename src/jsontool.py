# -*- coding: utf-8 -*-

import json

def jprint(file_name,obj):
    data_file = open(file_name, "w")
    data_file.write(json.dumps(obj, indent=4, sort_keys=True))
    data_file.close()

def jload(file_name):
    with open(file_name) as f:
        jsondata = json.load(f)
    return jsondata
