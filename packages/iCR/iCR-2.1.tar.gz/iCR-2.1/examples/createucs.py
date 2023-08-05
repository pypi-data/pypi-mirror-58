#!/usr/bin/env python
from iCR import iCR
bigip = iCR("172.16.1.129","admin","admin")
# List existing UCS files
ucslist = bigip.get("sys/ucs")
for ucs in ucslist['items']:
    print (ucs['apiRawValues']['filename'])
# Create new UCS
data = { "command": "save", "name": "myUCS" }
bigip.create("sys/ucs",data)
# Copy to /shared/images
data = { "command": "run", "utilCmdArgs": "-c 'mv /var/local/ucs/myUCS.ucs /shared/images'" }
bigip.create("util/bash",data)
bigip.download("myUCS.ucs")
