#!/usr/bin/env python
from iCR import iCR
bigip = iCR("172.24.9.132","admin","admin")
# Modify existing node called newnode
data = {'connectionLimit': '12345'}
# Note that we are using patch because we are only changing one configuration item
modifynode = bigip.modify("ltm/node/newnode",data, patch=True)
print (str(modifynode))
