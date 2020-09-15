import urllib.request, urllib.parse, urllib.error

import re

from bs4 import BeautifulSoup

import ssl

ctx=ssl.create_default_context()
ctx.check_hostname=False
ctx.verify_mode=ssl.CERT_NONE

url="http://py4e-data.dr-chuck.net/comments_736134.html"
html=urllib.request.urlopen(url,context=ctx).read()
soup=BeautifulSoup(html,'html.parser')

sum=0

tags=soup('span')

for tag in tags:
    if(tag.get('class',None)):
        sum=sum+int(re.findall('[0-9]+',str(tag))[0])

print(sum)



        
    
