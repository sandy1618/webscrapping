#! python 3
#downloading webpages and files form internet
#requests module helps in downloading foles form the internet .

import requests
r=requests.get('https://automatetheboringstuff.com/files/rj.txt')   #Takes a string of url to download . It returns a responst object.
type(r)                                                              # request.models.Response . r is a response type object. It contains the response the webserver gave to request
r.raise_for_status()                                                #raise_for_status raises exception if error downloading the file
play=open('shakespear.txt','wb')                                    # open file in write binary mode 'wb' for unicode encoding 
for chunck in r.iter_content(100000):                                #iter_content method returns "chuncks" of the content on each iteration.Chunck is of byte datatype
    play.write(chunck)                                              #write method writes the chunck data in the file created in open()                     

play.close()
