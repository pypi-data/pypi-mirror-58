iCR
===

This is a python module to simplify using F5 Networks' iControl REST interface.

Install using pip:

``pip install iCR``

As simple as::

  #!/usr/bin/env python
  from iCR import iCR
  bigip = iCR("172.24.9.132","admin","admin")
  virtuals = bigip.get("ltm/virtual")
  for vs in virtuals['items']:
    print vs['name']

This prints out a list of Virtual Servers.

Supported methods:
==================

* init(hostname,username,password,[timeout,port,icontrol_version,folder,token,debug])

* get(url,[select,top,skip]) -> returns data or False. Note that the url has two formats - with slash and without. 
  With slash eg /mgmt/shared/blahblah means that this will be the full URI. Without slash eg ltm/virtual will be appended to /mgmt/tm
* getlarge(url,size,[select]) -> Used to retrieve large datasets in chunks. Returns data or False
* create(url,data) -> returns data or False.
* post -> an alias for create()
* modify(url,data,[patch=True]) -> returns data or False
* delete(url) -> returns True or False
* upload(file) -> file is a local file eg /var/tmp/test.txt, returns True or False
* download(file) -> files are located in /shared/images, returns True or False
* create_cert(files) -> files is an array containing paths to cert and key. Returns name of cert or False
* get_asm_id(name) -> name is the name of a policy. Returns an ID or False
* create_hash(name) -> name is the name of the partition and policy. eg /Common/test_policy. This reduces the need to 
  retrieve an array of hashes from the BIG-IP. Returns a string.
* get_token -> retrieve a token with current username and password and store in object.token. Update headers to use the token. 
  Returns True or False
* delete_token -> delete the token and go back to using username/password. Returns True or False
* create_transaction -> creates a transaction and returns the transaction number ID as a string, or False. Subsequent requests will be added to the 
  transaction until commit_transaction is called. Transaction ID is stored in object.transaction
* commit_transaction. Commits the transaction stored in object.transaction. Returns True or False
* command(args,[cmd]) -> Runs a command using the arguments string args. Returns the returned output or True on success or False on failure. 
  Note:  Be sure to double-escape single quotes eg \\' and single escape double quotes eg \"
  cmd options are ping/save/load/restart/reboot


Module Variables:
=================

* icr_session - the link to the requests session
* raw - the raw returned JSON
* code - the returned HTTP Status Code eg 200
* error - in the case of error, the exception error string
* headers - the response headers
* icontrol_version - set this to specify a specific version of iControl
* debug - boolean True or False to set debugging on or off
* port - set the port ( 443 by default )
* folder - set this to create in a specific partition
* token - use this to set a specific token in use
* select - use this with get to select the returned data
* top - use this with get to return a set number of records
* skip - use this to skip to a specific record number
* transaction - the transaction ID in use


Examples
========

Create a Virtual Server
-----------------------
::

  vs_config = {'name':'test_vs'}
  createvs = bigip.create("ltm/virtual",vs_config,timeout=5)

Retrieve the VS we just created
-------------------------------
::

  virt = bigip.get("ltm/virtual/test_vs",select="name")
  print "Virtual Server created: " + virt['name']

Retrieve all nodes in chunks of 10
----------------------------------
::

  nodes = bigip.getlarge("ltm/node",10,select="name")
  for node in nodes['items']:
    print "Node: " + node['name']

Set the timeout
---------------
::

  bigip.timeout = 20

Now delete the VS we just created
---------------------------------
::

  delvs = bigip.delete("ltm/virtual/test_vs")

Retrieve ASM policy to ID mapping
---------------------------------
::

  policies = bigip.get("asm/policies",select="name,id")

Print  a table of ASM policies with learning mode
-------------------------------------------------
::

  print
  print "Policy Name                  Learning Mode"
  print "------------------------------------------"
  for item in policies['items']:
    enabled = bigip.get("asm/policies/" + item['id'] + "/policy-builder",select="learningMode")
    print '{:32}'.format(item['name']) + enabled['learningMode']

File upload
-----------
::

  fp = "/home/pwhite/input.csv"
  if bigip.upload(fp):
    print "File " + fp + " uploaded"

File download
-------------
::

  file="BIGIP-12.1.2.0.0.249.iso"
  download = bigip.download(file)
  if not download:
    print "File " + file + " download error"

SSL Certificate creation
------------------------
::

  # In different folder
  bigip.folder = "TestFolder"
  files = ("TestCert.crt","TestCert.key")
  cert = bigip.create_cert(files)
  if cert:
    print "Certificate " + cert + " created" 

Turn on debugging
-----------------
::

  bigip.debug = True

Retrieve ASM policy IDs
-----------------------
::

  asm = bigip.get_asm_id("dummy_policy")
  print len(asm) + " IDs returned"
  print "ID: " + str(asm[0])

Convert an ASM policy name to hash
----------------------------------
::

  hash = bigip.create_hash("/Common/test-policy")
  enabled = bigip.get("asm/policies/" + hash + "/policy-builder",select="learningMode")
  print '{:32}'.format(item['name']) + enabled['learningMode']

Use transactions
----------------
::

  transaction = bigip.create_transaction()
  # Create two new nodes
  data = { "name": "testNode-1", "address": "1.1.1.1" }
  newnode1 = bigip.create("ltm/node",data)
  data = { "name": "testNode-2", "address": "1.1.1.2" }
  newnode2 = bigip.create("ltm/node",data)
  # Commit transaction
  bigip.commit_transaction()


Run a bash command to say hello
-------------------------------
::

  command = bigip.command('echo \"Hello World!\"')
  # Check the object.code instead of the returned value
  if bigip.code == 200:
    print (command)

More examples can be found in the examples folder