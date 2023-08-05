#!/usr/bin/env python
from iCR import iCR
bigip = iCR("172.24.9.132","admin","admin")
data = { "name": "testnode", "address": "1.2.3.4" }
newnode = bigip.create("ltm/node",data)
print (str(newnode))
