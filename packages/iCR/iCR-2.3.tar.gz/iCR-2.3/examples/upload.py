#!/usr/bin/env python
# This is an example script which uses transactions to create nodes
from iCR import iCR
bigip = iCR("172.16.1.129","admin","admin")
bigip.debug = True
u = bigip.upload('testfile.txt')
if not u:
  print("Failed:" + str(bigip.error))
else:
  print ("Success")
