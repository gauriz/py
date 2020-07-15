import urllib
import re

url = "http://checkip.dyndns.org"

request = urllib.urlopen(url).read()

theIP = request[request.index(':') + 2: request.index('</body>')]

print('Your Public IP is : ' + theIP)