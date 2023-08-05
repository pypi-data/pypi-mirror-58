#!/usr/bin/env python
from iCR import iCR
bigip = iCR("172.24.9.132","admin","admin")
# Delete newnode
delnode = bigip.delete("ltm/node/newnode")
print (str(delnode))
