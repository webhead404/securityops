#!/usr/bin/env python3
import glob
import json
import yaml
import argparse
import os
import sys
import logging
# Initial description
text = "This script translates JSON rules to YAML rule files"
example_text = f'''examples:
 python3 {sys.argv[0]} -f example_rule.json -o folder/
 python3 {sys.argv[0]} -f detections/ -o folder/
 '''
# Initiate the parser
parser = argparse.ArgumentParser(description=text,epilog=example_text,formatter_class=argparse.RawDescriptionHelpFormatter)
# Add arguments (store_true means no argument needed)
parser.add_argument('-f', "--file-path", nargs='+', help="Path of JSON file(s) or folder(s) of JSON files", required=True)
parser.add_argument('-o', "--output-path", type=str , help="Folder path to output YAML files", required=False)
parser.add_argument("-d", "--debug", help="Print lots of debugging statements", action="store_const", dest="loglevel", const=logging.DEBUG, default=logging.WARNING)
parser.add_argument("-v", "--verbose", help="Be verbose", action="store_const", dest="loglevel", const=logging.INFO)
# **** Process arguments ****
args = parser.parse_args()
# **** Logging ****
logging.basicConfig(level=args.loglevel)
log = logging.getLogger(__name__)
# **** Aggregate files from Input Paths ****
input_paths = [os.path.abspath(path) for path in args.file_path]
# **** Handle input files ****
all_json_rules = []
for path in input_paths:
    if os.path.isfile(path):
        all_json_rules.append(path)
    elif os.path.isdir(path):
        all_json_rules = glob.glob(f"{path}/**/*.json", recursive=True)
    else:
        quit()
# **** Read all JSON files ****
for json_rule in all_json_rules:
    with open(json_rule) as f:    
        rule = json.load(f)
        # **** Create YAML Rule format ****
        ruleDict = {
            "title": rule['title'],
            "logsource": {
                "product": "suricata"
            },
            "detection": {
                "selection": {
                    "signature_id": (rule['signature_id']).split(",")
                }
            },       
        }

    # ******* Create yaml rule *************
    if args.output_path:
        rule_name = os.path.splitext(os.path.basename(json_rule))[0]
        #rule_name = rule['root']['directive'][0]['name']
        with open(f'{args.output_path}/{rule_name}.yml', 'w') as file:
            yaml.dump(ruleDict, file, sort_keys=False, indent=4)

    # ******* Hack to add condition to rule **********
            file.write("    condition: selection")
    else:
        print(yaml.dump(ruleDict, sort_keys=False))