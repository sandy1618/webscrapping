#!python 3
import requests , sys , pyperclip
#if len(sys.argv())>1:
#        address=''.join(sys.argv[1:])
#else:
address=pyperclip.paste()
print(address)

req=requests.get(address)

file=open('name.txt','wb')
for chunk in req.iter_content(100000):
        file.write(chunk)

file.close()
