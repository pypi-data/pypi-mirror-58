#!/usr/bin/env python
from iCR import iCR
bigip = iCR("172.24.9.132","admin","admin")
# Retrieve the master key
key = bigip.command("f5mku -K")
print (str(key))

