import urllib.request, urllib.parse, urllib.error
import ssl

ctx=ssl.create_default_context()
ctx.check_hostname=False
ctx.verify_mode=ssl.CERT_NONE

url=input("Enter URL:-")
uh=urllib.request.urlopen(url,context=ctx).read()
file=open('v.mp4','wb')
file.write(uh)
file.close()
