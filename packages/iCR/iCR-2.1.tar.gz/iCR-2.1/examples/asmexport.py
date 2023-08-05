#!/usr/bin/env python
# This is an example script to retrieve a list of policies and export them
from iCR import iCR
bigip = iCR("172.24.9.132","admin","admin")
# Retrieve a list of policies and IDs
policies = bigip.get("asm/policies",select="name,id")['items']

# Loop through policies and export
for policy in policies:
    # Create JSON
    data = { "filename": policy['name'] + '.xml.', "policyReference" : { "link": policy['selfLink'] } }
    export = bigip.create("asm/tasks/export-policy",data)
    file = bigip.get("asm/file-transfer/downloads/" + policy['name'] + '.xml.')
    print (str(file))
