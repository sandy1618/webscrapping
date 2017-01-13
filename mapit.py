#! python 3
import webbrowser ,sys, pyperclip
if len(sys.argv)>1:
    address=''.join(sys.argv[1:])
   
else:
	
	#pget address from clipboard
	address=pyperclip.paste()

webbrowser.open('https://google.com/maps/place/'+ address)
print(sys.argv)  
print(len(sys.argv))
print(address);
