#!/usr/bin/env python
from iCR import iCR
s = iCR("172.24.9.132","admin","admin")
fromIP = "3.3.3.3:80"
toIP = "4.4.4.4:80"
pools = s.get("ltm/pool?expandSubcollections=true")['items']
for pool in pools:
    for member in pool['membersReference']['items']:
        if member['name'] == fromIP:
            print (str(pool['name']) )
            newIPdata = { "name": toIP }
            #add = s.create("ltm/pool/" + pool['name'] + "/members",newIPdata)
            #if add:
            #    print("Added " + toIP + " to pool " + pool['name'])
            #delete = s.delete("ltm/pool/" + pool['name'] + "/members/" + fromIP)
            #if delete:
            #    print("Deleted " + fromIP + " from pool " + pool['name'])
