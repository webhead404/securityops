#!/bin/bash


# Description: Uploads Detections to Elastic Deployment
# Author: Roberto Rodriguez (@Cyb3rWard0g) & Modified for Elastic Detections by Ivan Ninichuck
# License: GPL-3.0

rule_directory=/opt/sigma/rules-converted #The directory where the rules are stored
kibana=$ip:5601/s/central-siem #kibana URL: Add /s/spacename for specific kibana space

for rule in $rule_directory/*.json ; do
            echo "+++ Uploading Detections to Elastic Deployment +++"
            curl -X POST $kibana/api/detection_engine/rules -H 'kbn-xsrf: true' -H 'Content-Type: application/json' -u $user:$password --data-binary @/$rule
            done
