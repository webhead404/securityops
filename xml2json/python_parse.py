#!/usr/bin/env python3
import glob
import json
import yaml
import argparse
import os
import sys
import logging

with open('/Users/kwright/Documents/suri-sigma/attacks.json') as json_file:
    data = json.load(json_file)

    ruleDict = {
            "rule": data['root']['directive']
    }
 
    rule_name = data['root']['directive'][0]['name']
    fileName = "/Users/kwright/Documents/suri-sigma/json_rules/%s.json" % name
    with open(fileName, 'w') as file:
        json.dump(ruleDict, file, sort_keys=False)