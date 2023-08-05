""" 
Version 2.1 17rh December 2019
  - Fixed various bugs
    - upload and download broken
    - Puke on incorrect password
Version 2.0 12th December 2019
  - refactored to use standard _request and _debug helper methods. 
  - Removed create_ssl_profile
  

Pete White
This is a Python module to simplify operations via F5 iControl REST interface. 
No support or liability is assumed
Installation - copy to your python library directory eg /lib/python2.7

Install using pip: pip install icr

https://devcentral.f5.com/codeshare/icr-python-module-for-icontrol-rest-1008

Example:
#!/usr/bin/env python
from iCR import iCR
# Connect to BIG-IP
bigip = iCR("172.24.9.132","admin","admin")
#Retrieve a list of Virtual Servers
virts = bigip.get("ltm/virtual")
if virts:
  for vs in virts['items']:
    print vs['name']

see README.rst and examples for more detail on usage

"""
###############################################################################
import os
import sys
import json
import requests
import hashlib
import base64
import time
# Disable warnings about insecure
#Python 3:
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
# Python 2:
#from requests.packages.urllib3.exceptions import InsecureRequestWarning
#requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

class iCR:
   
  def __init__(self,hostname,username,password,**kwargs):
    # Setup variables
    self.raw = ""
    self.code = ""
    self.error = ""   
    self.icr_link = ""
    self.headers = {'Content-Type': 'application/json'}
    self.hostname = hostname
    self.username = username
    self.password = password
    self.json = ""
    
    # manage keyword arguments
    self.timeout = kwargs.pop('timeout', 30)
    self.port = kwargs.pop('port', 443)
    self.icontrol_version = kwargs.pop('icontrol_version', '')
    self.folder = kwargs.pop('folder', '')
    self.token = kwargs.pop('token', False)
    self.debug = kwargs.pop('debug', False)
    self.stream = kwargs.pop('stream', False)
    self.transaction = kwargs.pop('transaction',False)
    # Create HTTP session
    icr_session = requests.session()
    # not going to validate the HTTPS certifcation of the iControl REST service
    icr_session.verify = False
    # Create session
    self.icr_session = icr_session
    self.icr_url = 'https://{0}:{1}/'.format(self.hostname,self.port)
    # Set auth
    self._set_auth()
     
  def _set_url(self,url):
    """
    Description
    -----------
    This function is a helper function to set the iControl URL correctly. If sent a URL which is correctly formatted
    and starts with https:// then it returns the string unchanged. If the URL starts with a / such as /mgmt/shared/ then it
    uses the whole string, if it does not have a preceding / then the url is appended to the base url + mgmt/tm/ eg ltm/virtual
    
    Parameters
    ----------
    url : string
    The url to be formatted
    
    Return is a string representing the formetted url
    """
    # If it is already of type http:// then return it as it is
    if url.startswith('https://'):
      return url
    # Method to create the URL based on leading /
    if url.startswith('/'):
      # The URL is fully specified eg /mgmt/tm/ltm/virtual
      u = self.icr_url + url
    else:
      # The URL is relative eg ltm/virtual
      u = self.icr_url + "mgmt/tm/" + url
      
    if self.icontrol_version:
      u = u + '?ver=' + self.icontrol_version
      
    return u
    
  # Set the authentication type to be either token or username/password
  def _set_auth(self):
    """
    Description
    -----------
    This method is a helper function to set the authentication method such as username/password or token. If elf.token is set
    then headers are updated to use the token and passwor auth is disabled. If not then vice-versa
    
    Parameters
    ----------
    None
    
    Return: none
    """
    if self.token:
      self.icr_session.headers.update({'X-F5-Auth-Token': self.token, 'Authorization': None, 'Content-Type': 'application/json'})
      self.icr_session.auth = None
      self._debug("Using token:" + str(self.token))
    else:
      self.icr_session.auth = (self.username, self.password)
      self.icr_session.headers.update({'Content-Type': 'application/json'})
      self._debug ( "Using username and password" )
      
  def _debug(self,msg):
    """
    Description
    -----------
    This method is a helper function to print debug messages to the console if debugging is turned on ie self.debug = True.
    DEBUG: is prepended to the string in output.
    
    Parameters
    ----------
    msg : string
      The message to be sent to the console
    
    Return: none
    """
    # Function to print debug messages
    if self.debug:
      print("DEBUG: " + msg)
      
  def _error(self,msg):
    """
    Description
    -----------
    This method is a helper function to print error messages to the console.
    ERROR: is prepended to the string in output.
    
    Parameters
    ----------
    msg : string
      The message to be sent to the console
    
    Return: none
    """
    print("ERROR: " + msg)
    
  # Retrieve objects - use GET method
  def get(self,uri,**kwargs):
    """
    Description
    -----------
    This method is used to retrieve configuration such as a list of virtual servers, statistics, etc
    eg:
    virtuals = bigip.get('ltm/virtual',select='name,destination',top=10,skip=2)

    If folder is set then only that partition will be checked. Note that iControl only implements
    $filter to select the partition but ASM fully implements the OData spec. You CAN shoot yourself in the foot
    with this if you use filter for non-ASM functions.
    
    Parameters
    ----------
    uri : string
      The URI to be requested eg ltm/virtual
    Keywords
    --------
    select : string
      The fields to be returned eg name, destination
    top : integer
      The number of records to return eg 10 to return the first 10 virtual servers
    skip : integer
      The number of records to skip
    filter : string
      An OData filter string to apply to retrieve only certain objects eg name+eq+myTestVs
    
    
    Return: if successful, returns a dict representing the returned data. If unsuccessful, returns False.
    """
    # Deal with keywords
    select = kwargs.pop('select', '')
    top = kwargs.pop('top', '')
    skip = kwargs.pop('skip', '')
    filterString = kwargs.pop('filter', '')

    # Set the URL
    url = self._set_url(uri)
    # Deal with URI and select, top, etc
    if "?" not in url:
      url_delimeter = "?"
    else:
      url_delimeter = "&"
    
    if select:
      url += url_delimeter + "$select=" + str(select)
      url_delimeter = "&"
    if top:
      url += url_delimeter + "$top=" + str(top)
      url_delimeter = "&"
    if skip:
      url += url_delimeter + "$skip=" + str(skip)
      url_delimeter = "&"
    if self.folder:
      url += url_delimeter +"$filter=partition+eq+" + self.folder
      url_delimeter = "&"
      if filterString:
        url += "+and+" + filterString
    elif filterString:
      url += url_delimeter + "$filter=" + filterString
      url_delimeter = "&"
      
    self._set_auth()
    self._request('get',url)
    if self.code < 400:
      return json.loads(self.raw)
    else:
      return False
  
  def getlarge(self,url,size=50,**kwargs):
    """
    Description
    -----------
    This method is used to retrieve large configuration such as a list of hundreds of virtual servers, statistics, etc
    eg:
    virtuals = bigip.get('ltm/virtual',select='name,destination')

    If folder is set then only that partition will be checked. Note that iControl only implements
    $filter to select the partition but ASM fully implements the OData spec. You CAN shoot yourself in the foot
    with this if you use filter for non-ASM functions.
    
    Parameters
    ----------
    uri : string
      The URI to be requested eg ltm/virtual
    size : integer
      The size of blocks to be retrieved in one block
    Keywords
    --------
    select : string
      The fields to be returned eg name, destination
    sleep : integer
      The time in seconds to sleep between iterations of retrieval. Along with the size, this setting controls
      the load put on the network and device
    
    Return: if successful, returns a dict representing the returned data. If unsuccessful, returns False.
    """
    selectValue = kwargs.pop('select', '')
    sleepValue = kwargs.pop('sleep',0.1)
    returnValue = {}
    self._debug( "getlarge select:" + selectValue + ", object size:" + size + ", sleepValue: " + sleepValue + "s" )
    skipValue = 0
    while True:
      if not selectValue == '':
        resp = self.get(url,top=size,skip=skipValue,select=selectValue)
      else:
        resp = self.get(url,top=size,skip=skipValue)
      # Check that the response hasn't failed
      if resp:
        if 'items' in resp:
        # There is a list of items - used for list of objects
        # Have to individually add to items otherwise they are overwritten
          for item in resp['items']:
            if 'items' in returnValue:
              returnValue['items'].append(item)
            else:
              returnValue['items'] = [item]
        elif 'entries' in resp:
          # There is a list of entries - used for stats
          for entry in resp['entries']:
            if not 'entries' in returnValue:
              returnValue['entries'] = {}
            returnValue['entries'][entry] = resp['entries'][entry]    
        else:
          # No 'items' field - could be a specific object
          returnValue.update(resp)        
      else:
          # resp failed
          return False
          
      # Increment the skipValue to grab the next block
      skipValue += size
      # Stop when there is no nextLink
      if not 'nextLink' in resp.keys():
        break
      # Sleep for a while to reduce load on BIG-IP
      time.sleep(sleepValue)
    return returnValue
    
  def create(self,uri,data):
    """
    Description
    -----------
    This method is used to send data to the BIG-IP such as creating objects, starting tasks etc
    
    Parameters
    ----------
    uri : string
      The URI to be requested eg ltm/virtual. This should be the collection, not a specific object ie net/vlan, NOT net/vlan/vlan-1
    data : a dict OR valid JSON data representing the data to send eg { "name": "myObjectName" }
    
    
    Return: if successful, returns a dict representing the returned data. If unsuccessful, returns False.
    """
    self._request('post',uri,data=data)
    if self.code < 400:
      return json.loads(self.raw)
    else:
      return False

  def post(self,uri,data):
    """
    This method is just a link to the create method

    """
    return self.create(uri,data)

  def modify(self,uri,data,**kwargs):
    """
    Description
    -----------
    This method is used to modify existing BIG-IP objects
    
    Parameters
    ----------
    uri : string
      The URI to be requested eg ltm/virtual/vs-1. Note that this is to be the specific object
    data : a dict OR valid JSON data representing the data to send eg { "address": "1.2.3.4" }
    
    Keywords
    --------
    patch : Boolean True or False. Determines whether the method used is PATCH. This is used to update only a subset of the 
    object data rather than to overwrite the whole object data.

    Return: if successful, returns a dict representing the returned data. If unsuccessful, returns False.
    """
    patch = kwargs.pop('patch', False)
    if patch:
      self._request('patch',uri,json.dumps(data))
    else:
      self._request('put',uri,json.dumps(data))
    if self.code < 400:
      return json.loads(self.raw)
    else:
      return False
    
  def delete(self,uri):
    """
    Description
    -----------
    This method is used to delete existing BIG-IP objects
    
    Parameters
    ----------
    uri : string
      The URI to be requested eg ltm/virtual/vs-1. Note that this is to be the specific object eg net/vlan/vlan-1     

    Return: If successful, returns True. If unsuccessful, returns False
    """
    return self._request('delete',uri)

  def _request(self,method,uri,data=False,**kwargs):
    """
    Description
    -----------
    This is a helper method to perform the request using the Python requests module
    
    Parameters
    ----------
    method : string
      The method to be performed, in lowercase. get/post/put/patch/delete
    uri : string
      The URI to be requested eg ltm/virtual/vs-1
    data : dict OR JSON text
      The data to be sent eg with a post request

    Return: If return code is < 400, returns True. If return code is >= 400, returns False
    self.code is set to the response code
    self.raw is set to the response text
    self.json is set to the returned data ie a dict
    self.error is set to be any returned error messages, from exceptions or returned errors

    """
    # Set the URL
    request_url = self._set_url(uri)
    self._debug( "--- Request Start ---")
    self._debug( "Method: " + method + " URL:" + request_url )
    self._debug( "Request Headers:" + str(self.headers) )
    self._set_auth()
    # Check whether data is valid JSON. If not, turn it into valid JSON
    if data != False:
      self._debug("Data:" + str(data))
      try:
        json.loads(data)
      except:
        self._debug("Invalid JSON data used, converting to valid JSON: " + json.dumps(data))
        data = json.dumps(data)
    try:
      if method == 'get':
        response = self.icr_session.get(request_url,headers = self.icr_session.headers,stream = self.stream,timeout = self.timeout)
      elif method == 'post':
        response = self.icr_session.post(request_url,data,headers = self.icr_session.headers,stream = self.stream,timeout = self.timeout)
      elif method == 'put':
        response = self.icr_session.put(request_url,data,headers = self.icr_session.headers,stream = self.stream,timeout = self.timeout)
      elif method == 'patch':
        response = self.icr_session.patch(request_url,data,headers = self.icr_session.headers,stream = self.stream,timeout = self.timeout)
      elif method == 'delete':
        response = self.icr_session.delete(request_url,timeout = self.timeout)
      else:
        response = self.icr_session.get(request_url,headers = self.icr_session.headers,stream = self.stream,timeout = self.timeout)
    except Exception as e:
      self.error = e
      self._debug('ERROR: ' + str(e))
      return False
    self.raw = response.text
    self.code = response.status_code
    self.headers = response.headers
    try:
      self.json = json.loads(response.text)
    except:
      self._debug("Response is not valid JSON")
    #
    self._debug( "Response Status Code:" + str(self.code) )
    self._debug( "Response Headers:" + str(response.headers) )
    self._debug( "Response Text:" + str(response.text) )
    self._debug( "--- Request End ---")
    
    if response.status_code < 400:
      self._debug("_request is returning True")
      return True
    elif response.status_code == 401:
      # This means the password is wrong
      self.error = "Authentication error: incorrect username and password"
      self._debug("Authentication error: incorrect username and password")
      self._debug("_request is returning False")
      return False
    else:
      self.error = str(response.text)
      self._debug('ERROR: ' + self.error)
      self._debug("_request is returning False")
      return False

  def upload(self,fp):
    """
    Description
    -----------
    This is a method to perform upload of a file from a host to the BIG-IP.
    Borrowed from https://devcentral.f5.com/articles/demystifying-icontrol-rest-part-5-transferring-files
    Works on TMOS >12.0, prior to that, create directory /var/config/rest/downloads/tmp
    Files uploaded to /var/config/rest/downloads
    
    Parameters
    ----------
    fp : string
      The full filepath of the file to be sent eg /var/tmp/myFile.txt

    Return: If successful, returns True. If unsuccessful, returns False
    """
    # Set the chunk size - default is 512 Bytes
    chunk_size = 512 * 1024
    # Open file and retrieve details
    try:
      fileobj = open(fp, 'rb')
    except IOError:
      self.error = "File ",fp," opening failed"
      return False
    filename = os.path.basename(fp)
    size = os.path.getsize(fp)
    # Set the URL according to the file type
    if os.path.splitext(filename)[-1] == '.iso':
      request_url = self._set_url('/mgmt/cm/autodeploy/software-image-uploads/{0}'.format(filename))
    else:
      request_url = self._set_url('/mgmt/shared/file-transfer/uploads/{0}'.format(filename))
    self._debug( "Upload URL:" + request_url )
    self._set_auth()
    start = 0
    while True:
      file_slice = fileobj.read(chunk_size)
      if not file_slice:
        break
      current_bytes = len(file_slice)
      if current_bytes < chunk_size:
        end = size
      else:
        end = start + current_bytes
    
      self.icr_session.headers['Content-Range'] = "%s-%s/%s" % (start, end - 1, size)
      response = self._request('post',request_url,file_slice)
      if not response:
        self._debug( "Upload error:" + str(self.error) )
        return False       
      start += current_bytes
    return True    
      
      
  def download(self,fp):
    """
    Description
    -----------
    This is a method to perform download of a file from a BIG-IP.
    Borrowed from https://devcentral.f5.com/articles/demystifying-icontrol-rest-part-5-transferring-files
    Files downloaded from /shared/images
    
    Parameters
    ----------
    fp : string
      The name of a file located in /shared/images

    Return: If successful, returns True. If unsuccessful, returns False
    """
    chunk_size = 512 * 1024
    headers = {
      'Content-Type': 'application/octet-stream'
    }
    filename = os.path.basename(fp)
    request_url = self._set_url('/mgmt/cm/autodeploy/software-image-downloads/{0}'.format(filename))
    self._debug( "DEBUG: Download URL:" + request_url )
    self._set_auth()
    with open(fp, 'wb') as f:
      start = 0
      end = chunk_size - 1
      size = 0
      current_bytes = 0

      while True:              
        headers['Content-Range'] = "%s-%s/%s" % (start, end, size)
        response = self.icr_session.get(request_url,headers=headers,stream=True,timeout = self.timeout)
        if not response:
          self._debug( "DEBUG: Upload requests error:" + str(self.error) )
          return False

        if response.status_code == 200:
          # If the size is zero, then this is the first time through the
          # loop and we don't want to write data because we haven't yet
          # figured out the total size of the file.
          if size > 0:
            current_bytes += chunk_size
            for chunk in response.iter_content(chunk_size):
              f.write(chunk)
          # Once we've downloaded the entire file, we can break out of the loop
          if end == size:
            break
        crange = response.headers['Content-Range']

        # Determine the total number of bytes to read
        if size == 0:
          size = int(crange.split('/')[-1]) - 1
          self._debug( "DEBUG: File size is " + str(size) + " Bytes" )

          # If the file is smaller than the chunk size, BIG-IP will
          # return an HTTP 400. So adjust the chunk_size down to the
          # total file size...
          if chunk_size > size:
            end = size
          # ...and pass on the rest of the code
          continue

        start += chunk_size
        if (current_bytes + chunk_size) > size:
          end = size
        else:
          end = start + chunk_size - 1
    return True
    
  def create_cert(self,files):
    """
    Description
    -----------
    This is a method to create SSL certs from local files
    
    Parameters
    ----------
    files : array of strings
      An array of the certificate and key files eg [ '/var/tmp/myCert.crt','/var/tmp/myCert.key' ]. Note that either 
      the certificate name should terminate with .crt OR they should be in the order certificate,key. In the case above, 
      myCert will become he name of the certificate object.

    Return: If successful, returns True. If unsuccessful, returns False
    """
    f1 = os.path.basename(files[0])
    f2 = os.path.basename(files[1])
    if f2.endswith('.crt'):
      certfilename = f2
      keyfilename = f1
    else:
      certfilename = f1
      keyfilename = f2
    # certname is the name of the certificates and will become the object name  
    certname = f1.split('.')[0]
    self._set_auth()
    # Upload the files to the device
    if not self.upload(files[0]):
      self._debug( "DEBUG: upload failed:" + str(self.error) )
      return False
    if not self.upload(files[1]):
      self._debug( "DEBUG: upload failed:" + str(self.error) )
      return False
    self._debug( "DEBUG: Cert & key uploaded" )
    
    # Create certificate
    payload = { 'command': 'install' }
    if self.folder:
      payload['name'] = "/" + self.folder + "/" + certname
    else:
      payload['name'] = certname
    payload['from-local-file'] = '/var/config/rest/downloads/%s' % certfilename
    response = self.create('sys/crypto/cert',payload)
    if not response:
      return False

    self._debug( "DEBUG: Cert " + certname + " created" )

    # Create key
    payload['from-local-file'] = '/var/config/rest/downloads/%s' % keyfilename
    response = self.create('sys/crypto/key',payload)
    if not response:
      return False
    return certname
  
  def get_asm_id(self,name):
    """
    Description
    -----------
    This is a method to return an ASM ID for a given name
    
    Parameters
    ----------
    name : string
      The name of the ASM policy to retrieve
      
    Return: If successful, returns an integer as the ID. If unsuccessful, returns False
    """
    policies = self.get("asm/policies",select="name,id")
    for item in policies['items']:
      if item['name'] == name:
        self._debug ( "Found policy " + name + " as ID " +item['id'] )
        return item['id']
    return False

  def create_hash(self,name):
    """
    Description
    -----------
    This is a method to return an hash such as is used by ASM and in other places
    Very simply, this is a base64-encoded version of the MD5 of the string.
    Note that this should include the partition eg /Common/testpolicy
    
    Parameters
    ----------
    name : string
      The string to encode to a hash
      
    Return: string denoting the encoded name string
    """
    algo = hashlib.md5() 
    algo.update(name)
    digest = base64.b64encode(algo.digest(),'-_').replace('=','')
    self._debug( "Create_hash: String:" + name + ", Digest:" + digest )
    return digest
      
  def get_token(self):
    """
    Description
    -----------
    This is a method to retrieve an authentication token and store it in self.token
    
    Parameters
    ----------
    None

    Return: string denoting the token
    """
    request_url = self._set_url('/mgmt/shared/authn/login')
    payload = { 'username': self.username, 'password': self.password, 'loginProviderName': 'tmos' }
    self._debug( "Current token:" + str(self.token) )
    response = self.create(request_url,data = json.dumps(payload))
    if not response:
      self._debug( "Token retrieval error:" + str(response.text) )
      return False
    self.token = response['token']['token']
    self._debug( "Token retrieved:" + self.token )
    self._set_auth()
    return self.token
    
  def delete_token(self):
    """
    Description
    -----------
    This is a method to delete the token in use ie self.token
    
    Parameters
    ----------
    None

    Return: If successful, returns True. If unsuccessful, returns False
    """
    if not self.token:
      self.error = "No token set to be able to delete"
      return False
    request_url = self._set_url('/mgmt/shared/authz/tokens/' + self.token)
    self._debug( "Deleting token " + self.token    )
    response = self.delete(request_url)
    if not response:
      self._debug( "Token delete error:" + str(self.error) )
      self.token = False
      return False
    self.token = False
    self._set_auth()
    return True
    
  def create_transaction(self):
    """
    Description
    -----------
    This is a method to create a transaction ID and update headers. All following requests will use this
    transaction, until commit_transaction is called.
    
    Parameters
    ----------
    None

    Return: If successful, returns the Transaction ID as a string. If unsuccessful, returns False
    """
    if not self.transaction:
      # If a transaction ID is not set then create one
      newTransaction = self.create("transaction",{})['transId']
      self._debug("self.transaction is not set, created new transaction:" + str(newTransaction))
      if newTransaction != False:
        self.transaction = str(newTransaction)
      else:
        self.error = "Cannot create new transaction: " + self.error
        return False
    if self.get("transaction/" + self.transaction)['state'] != 'STARTED':
      # Check the transaction is valid, if not then return False
      self._debug("transaction ID " + self.transaction + " is not of state STARTED, recreating it")
      self.transaction = False
      return False
    self.icr_session.headers.update({'X-F5-REST-Coordination-Id': self.transaction})
    self._debug("Using transaction ID:" + self.transaction)
    return self.transaction
  
  def commit_transaction(self):
    """
    Description
    -----------
    This is a method to commit a transaction as created by create_transaction
    
    Parameters
    ----------
    None

    Return: If successful, returns True. If unsuccessful, returns False
    """
    if not self.transaction:
      self.error("Run commit_transaction but there is no transaction ID")
      return False
    state = self.get("transaction/" + self.transaction)['state']
    self._debug("Transaction ID " + self.transaction + " state: " + str(state))
    if state != 'STARTING' and state != 'UPDATING':
      self.error("Transaction ID " + self.transaction + " is not in state STARTING or UPDATING")
      return False
    del(self.icr_session.headers['X-F5-REST-Coordination-Id'])
    update = self.modify("transaction/" + self.transaction,{"state":"VALIDATING"},patch=True)
    if not update:
      self.error("Could not commit transaction ID " + self.transaction)
      return False
    else:
      self.transaction = False
      return True     

  def command(self,cmdArgs = '',**kwargs):
    """
    Description
    -----------
    This is a method to run a command, by default bash
    
    Parameters
    ----------
    cmdArgs : string
      The command arguments to be sent to the command eg echo \"Hello World!\". These are relevant
      to the command which is run eg if running ping then '-c 5 10.20.30.40'
      Note:  Be sure to double-escape single quotes eg \\' and single escape double quotes eg \"

    Keywords
    --------
    cmd : string
      The name of the command to run. Choice of ping/save/load/restart/reboot

    Return: If successful, returns the output of the command where relevant, or True. If unsuccessful, returns False
    """ 
    # Command name
    cmd = kwargs.pop('cmd',False)

    # Allow specification of the command to run       
    if not cmd:
      data = { "command": "run", "utilCmdArgs": "-c '" + cmdArgs + "'" }
      uri = "util/bash"
      self._debug("Running command run with data:" + str(data))
    elif cmd == 'ping':
      data = { "command": "run", "utilCmdArgs": cmdArgs }
      uri = "util/ping"
      self._debug("Running command ping with data:" + str(data))
    elif cmd == 'save':
      data = { "command": "save", "options": [{ "file": cmdArgs }]}
      uri = "sys/config"
      self._debug("Running command save with data:" + str(data))
    elif cmd == 'load':
      data = { "command": "load", "name": cmdArgs }
      uri = "sys/config"
      self._debug("Running command load with data:" + str(data))
    elif cmd == 'restart':
      data = { "command": "restart", "name": cmdArgs}
      uri = "sys/service"
      self._debug("Running command restart with data:" + str(data))
    elif cmd == 'reboot':
      data = { "command": "reboot"}
      uri = "sys"
      self._debug("Running command reboot with data:" + str(data))
    else:
      self.error("The function " + cmd + " has not been implemented yet")
      return False

    response = self.create(uri,data)
    if not response:
      self._debug ( "Failure when running command " + cmd )
      return False
    self._debug("Response:" + str(self.raw))
    try:
      # Try to return the command result if it is available. If not, return True
      return json.loads(self.raw)['commandResult']
    except:
      return True
