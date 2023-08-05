#!/usr/bin/env python
# This is an example script to connect to two different BIG-IPs and copy pools from source to target
from iCR import iCR
s = iCR("172.24.9.132","admin","admin")
t = iCR("10.128.1.245","admin","admin")

pools = s.get("ltm/pool?expandSubcollections=true")['items']
for pool in pools:
    # Remove state and session from membersReference => items
    for member in pool['membersReference']['items']:
        del member['state']
        del member['session']
    # POST to the target device
    if t.create("ltm/pool",pool):
        print ("Created " + pool['name'])
    else:
        print ()"Error creating " + pool['name'])
