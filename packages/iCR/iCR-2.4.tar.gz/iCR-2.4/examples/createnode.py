#!/usr/bin/env python
# This is an example script which uses transactions to create nodes
from iCR import iCR
bigip = iCR("172.24.9.132","admin","admin")
# Create new node
createTransaction = bigip.create_transaction()
print (str(createTransaction))
# Create node 1
data = {'name': 'newnode-1','address': '2.3.4.5'}
newnode1 = bigip.create("ltm/node",data)
# Create node 2
data = {'name': 'newnode-2','address': '3.4.5.6'}
newnode2 = bigip.create("ltm/node",data)
# Commit transaction
commitTransaction = bigip.commit_transaction()
print (str(commitTransaction))
