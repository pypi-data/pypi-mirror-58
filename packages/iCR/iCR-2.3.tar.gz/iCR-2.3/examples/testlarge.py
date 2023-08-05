#!/usr/bin/env python
from iCR import iCR
bigip = iCR("10.154.14.13","admin","admin")
nodes = bigip.getlarge("ltm/node",100)
if nodes:
  print ("Nodes:" + str(len(nodes['items'])))
else:
  print ("Failed")
