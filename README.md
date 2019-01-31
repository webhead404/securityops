# securityops
A private repository to house all of the configurations I am using to augment Windows security. It contains Logstash configurations, installation requirements to make everything work with ROCK, and other additional helpful things. 

1. Install ROCK per the docs
2. Alter /etc/rocknsm/config.yml
Change "Rock_online_install" to true. This is an intial build and it will be a log collector. At this time it will be okay. 
3. Flip netmon related switches (Suricata, Bro, Stenographer, Docket, etc.)
4. Deploy Rock! 
sudo ./opt/rocknsm/rocknsm/bin/deploy_rock.sh
5. Need to install the logstash prune filter in order for our configurations to behave as expected. 
sudo ./usr/share/logstash/logstash-plugin install logstash-filter-prune
6. Copy configurations over to the Elastic Stack
Multiple ways to do this, I typically SSH into it and drop the files securely into home directory and copy them out from there. 
7. Add firewall rule for Kafka to communicate with our Windows server. 
sudo iptables -I INPUT -p tcp -s ip-address --dport 9092 -j ACCEPT



