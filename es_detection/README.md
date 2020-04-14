# This is an outline of the steps necessary to enable the new detection engine in Elastic Stack 7.6.
All command will have to be run with root/admin privelege

First generate certificates. Elastic has a tool for this. 

```./bin/elasticsearch-certutil cert```

Set the filename to config/elastic-certificates.p12

# You will need to generate a CA and/or client certificates for each part of the cluster. 
That can be accomplished by something like the following:

Reference: https://www.elastic.co/blog/elasticsearch-security-configure-tls-ssl-pki-authentication

# CA
```openssl pkcs12 -in elastic-certificates.p12 -cacerts -nokeys -chain > client-ca.cer```

# private key:

```openssl pkcs12 -in elastic-certificates.p12 -nocerts -nodes > client.key```

# public cert

```openssl pkcs12 -in elastic-certificates.p12 -clcerts -nokeys  > client.cer```


# Second add or change/uncomment the following lines in elasticsearch.yml

```xpack.security.enabled: true```

```xpack.security.transport.ssl.enabled: true```

```xpack.security.transport.ssl.verification_mode: certificate```

```xpack.security.transport.ssl.keystore.path: /etc/elasticsearch/elastic-certificates.p12```

```xpack.security.transport.ssl.truststore.path: /etc/elasticsearch/elastic-certificates.p12```


Transport security is to enable the security indexes and set up RBAC. 
The HTTP security is primarily used to establish a secure connection for managing elasticsearch API's 
which is required for the SIEM Detection engine.

# Additionally make sure that the bind addresses for elasticsearch are not localhost. 

# Start elasticsearch

# Generate passwords for the users

```./bin/elasticsearch-setup-passwords auto```

# Elastic will automatically generate random passwords for the users that are needed to 
# establish connections which will be the elastic and kibana users respectively. 

Now add these lines to elasticsearch

```xpack.security.http.ssl.enabled: true```
```xpack.security.http.ssl.keystore.path: /etc/elasticsearch/elastic-certificates.p12```
```xpack.security.http.ssl.truststore.path: /etc/elasticsearch/elastic-certificates.p12```

# Copy the client certificate to Kibana and modify kibana.yml 
# Add or change/uncomment the following lines
Reference: https://www.elastic.co/blog/elasticsearch-security-configure-tls-ssl-pki-authentication

elasticsearch.url: "https://your-ip-here:9200" #ensure https not http
xpack.security.enabled: true
elasticsearch.username: "kibana"
elasticsearch.password: "your kibana password goes here"
elasticsearch.ssl.certificateAuthorities: config/certs/client-ca.cer
elasticsearch.ssl.verificationMode: certificate

# Add required 32 character persistent key for savedObjects in kibana.yml
# Each time Kibana starts it generates a new encryption key for saved objects such as dashboards, visualizations and searches. 
# This should be set manually for local Kibana deployments. 
Reference: https://www.elastic.co/guide/en/siem/guide/7.6/detection-engine-overview.html#detections-encryption-key

# Example 
# xpack.encryptedSavedObjects.encryptionKey: 'fhjskhsdhd678ehkdfdlliverpoolfcr'
xpack.encryptedSavedObjects.encryptionKey: '32 char alpha numberic'



# Kibana and index privileges required for Detections
Reference: https://www.elastic.co/guide/en/siem/guide/7.6/detection-engine-overview.html#detections-encryption-key
# Depending on your privileges and whether a .siem-signals-<space name> index has been created for the Kibana space, 
# you might see an error message when you try to open the Detections page.

# If you see this message, "Let’s set up your detection engine" a user with these privileges must open the 
# Detections page before you can view signals and rules:

# Permissions required: 

The manage_api_key cluster privilege (see Security privileges).
The create_index privilege for the Kibana space (see Indices privileges).
Kibana space All privileges for the SIEM feature (see Feature access based on user privileges).
