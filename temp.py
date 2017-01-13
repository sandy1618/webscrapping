#! python 3
import requests,bs4, pyperclip
link=pyperclip.paste()
print(link)
re=requests.get(link)
file=open('example.html','r')
print(type(file))
weather=bs4.BeautifulSoup(re.text,'html.parser')
print(type(weather))
element=weather.select('span')
print(len(element))
i=0;
while (i < len(element)):
              print(element[i].getText());
              i+=1
              
    
