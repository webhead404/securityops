import glob
import json
import yaml
import argparse
import os
import sys
import logging

with open('/Users/kwright/Documents/suri-sigma/suricata_directives.json','r') as in_json_file:
    json_object_list = json.load(in_json_file)

    for json_obj in json_object_list:
        #directive=json_object_list['root']['directive'][0]['id']
        fileName=json_obj['title']+'.json'
        #rule_name = 
        with open(fileName, 'w') as out_json_file:
            json.dump(json_obj, out_json_file, sort_keys=True)


    #ruleDict = {
    #        "rule": data['root']['directive'][0]
    #}