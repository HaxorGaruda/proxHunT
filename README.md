[Proxy Hunter]
Automatic searching anonymous proxy - Beta Release

Installation :
 - sudo apt-get install chromedriver
 - sudo pip install selenium

usage : python proxHunT.py

Description :
this script is automation program to search HTTPS Proxy with level High Anonymous is mean remote host does not know your IP and has no direct proof of proxy usage (proxy-connection family header strings). If such hosts do not send additional header strings it may be considered as high-anonymous. If a high-anonymous proxy supports keep-alive you can consider it to be extremely-anonymous.

Output :
when execute this script, in current directory will add 2 new file :
- proxylist.txt  -> this is fresh list proxy before checking to know work or not. every this script execute, list of                      proxy will change to new list.
- working_proxy.txt -> This file contains a list of proxies that have been verified in online proxy checker.

So the schema of this script is to get a proxy from proxylist.net stored in a file called proxylist.txt then verify the proxy to the online proxy checker and save the result of the verification into a working_proxy.txt file.

Warning :
don't change banner of this script because it will make script not working 

**Tested On Kali Linux**

