#! python3
import requests, bs4
res=requests.get('http://nostarch.com')
res.raise_for_status()
nostarchsoup=bs4.BeautifulSoup(res.text,"html.parser")
print(type(nostarchsoup))

ex=open('example.html')
example=bs4.BeautifulSoup(ex,"html.parser")
elems=example.select('#author')
print(type(elems))
print(len(elems))
print(elems[0])
s=elems[0].getText()
print(type(s))
