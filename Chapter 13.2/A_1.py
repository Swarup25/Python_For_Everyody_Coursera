import urllib.request, urllib.parse, urllib.error
import json
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter location: ')
print('Retrieving', url)
uh = urllib.request.urlopen(url, context=ctx)
data=uh.read().decode()
print('Retrieved',len(data),'characters')
lst=json.loads(data)
print('Count: ',len(lst['comments']))
sums=0
for item in (lst['comments']):
    no=item['count']
    sums+=int(no)
print('Sum: ',sums)