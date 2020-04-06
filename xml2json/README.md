#Suricata Rules Conversation
#
#First run the rule of choice through the xml_converter script. This will convert the XML to JSON which will make #it easier to parse and define sigma rules. In addition could use something like JQ to only the required fields. 
#Then user the python parse script to grab the required fields. The goal of this project is to automate the create #of multiple simple Sigma rules to tie in Suricata ID's for alerting in any system supported by the Sigma backends. 