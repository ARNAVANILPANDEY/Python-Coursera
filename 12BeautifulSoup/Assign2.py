import urllib.request, urllib.parse, urllib.error

import re

from bs4 import BeautifulSoup

import ssl

ctx=ssl.create_default_context()
ctx.check_hostname=False
ctx.verify_mode=ssl.CERT_NONE

s=input("Enter URL : ")
m=int(input("\nEnter count : "))
n=int(input("\nEnter postion : ")) 
for i in range(0,m):
    url=s
    print("Retrieving:  ",s)
    html=urllib.request.urlopen(s,context=ctx).read()
    soup=BeautifulSoup(html,'html.parser')

    tags=soup('a')
    s=str(tags[n-1].get('href',None))


print("Retrieving:  ",s)
#print(re.findall('[_].*[_](.+)\.',str(s))[0])
