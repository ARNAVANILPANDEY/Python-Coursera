import urllib.request, urllib.parse, urllib.error

'''fhand=urllib.request.urlopen('http://data.pr4e.org/romeo.txt')

for line in fhand:
    print(line.decode().strip())'''


from bs4 import BeautifulSoup

url='https://en.wikipedia.org/wiki/Ramsey_theory'

html=urllib.request.urlopen(url).read()
soup=BeautifulSoup(html,'html.parser')

print(soup)
