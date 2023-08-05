#!/usr/bin/env python
# This is a script to test the iCR module
# Assumes that you have a BIG-IP available - set the IP address, username and password below on line 6
from iCR import iCR
# Connect to BIG-IP
bigip = iCR("172.16.1.129","admin","admin")
# Give me a hash
print ("--- Create Hash: " + bigip.create_hash("MyHashName"))

# List nodes
print ("--- Listing nodes:")
nodes = bigip.get("ltm/node")
print("Name\tAddress")
print("-------------")
for node in nodes['items']:
  print (node['name'] + "\t" + node['address'])
print("---")

# Create a new node
print("--- Creating a new node:")
data = { "name": "myTestNode", "address": "2.3.4.5" }
newnode = bigip.create("ltm/node",data)
print(str(newnode))


# Modify the node we just created
print("--- Modifying myTestNode")
data = { "address": "1.2.3.5" }
modifynode = bigip.modify("ltm/node/myTestNode",data)
print (str(modifynode))

# Delete the node we just modified
print("--- Deleting myTestNode")
deletenode = bigip.delete("ltm/node/myTestNode")
print (str(deletenode))

print("--- Creating a transaction")
transaction = bigip.create_transaction()
print("Transaction ID: " + str(transaction))
# Create two new nodes
print("--- Creating testNode-1:")
data = { "name": "testNode-1", "address": "1.1.1.1" }
newnode1 = bigip.create("ltm/node",data)
print("--- Creating testNode-2:")
data = { "name": "testNode-2", "address": "1.1.1.2" }
newnode2 = bigip.create("ltm/node",data)
print("--- Committing transaction")
print(str(bigip.commit_transaction()))


# Run a bash command to say hello
print("--- Running command to print Hello World!")
command = bigip.command('echo \"Hello World!\"')
# Check the status code directly rather than checking the returned status
if bigip.code < 300:
  print (command)
