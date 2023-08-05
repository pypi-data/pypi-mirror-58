#!/usr/bin/env python
from iCR import iCR
s = iCR("172.24.9.132","admin","admin")
t = iCR("10.128.1.245","admin","admin")

pools = s.get("ltm/pool?expandSubcollections=true")['items']
for pool in pools:
    t.delete("ltm/pool/" + pool['name'])
