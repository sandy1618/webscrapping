#! python3
#comic.py - download every single comic form the websites.
#plan/design the program to whre the files will be saved and when the program should terminate.
import requests , os ,bs4

url='http://xkcd.com'
os.makedirs('xkcd',exist_ok=True) #store comic in ./xkcd directory in the current working folder or make a new folder named xkcd. exist_ok=true prevent errors if the folder already exists
while not url.endswith('#'):# string.endswith() is a method in string class to check the character ending in the string 
    # todo: download the page
    print('Downloading page%s...'%url)
    res=requests.get(url)
    res.raise_for_status()

    soup=bs4.BeautifulSoup(res.text,'html.parser')
    #todo : use beautiful soup to get the url of the comic image
    comicElem=soup.select('#comic img')#'#comic img will get me the correct <img> element from beautiful soup 
    if comicElem==[]:
        print('could not find comic image')
    else:
            try:
                comicUrl='http:'+comicElem[0].get('src')
    #todo  : download the image using requests module
                print('Downloading image %s....'%comicUrl)
                res=requests.get(comicUrl)
                res.raise_for_status()
                # if you are not abole to download the image and if res.raise_for_status raises an exception , then the next lines does the following #exception handling
            except requests.exceptions.MissingSchema:
                #skip this comic
                prevLink=soup.select('a[rel="prev"]')[0] #this is used to get the first tag of element with id rel="prev"and identifies and returns the tag   
                url='http://xkcd.com'+prevLink.get('href')
                continue
                                     
    #todo: save the image to ./xkcd.
    imageFile=open(os.path.join('xkcd',os.path.basename(comicUrl)),'wb')# os.path.join - joins xkcd & Baseurl file name from the url tags. it should l
    for chunk in res.iter_content(100000):
            imageFile.write(chunk)
    imageFile.close()
                
    #todo: get the previous button url and update the link and download this page also , basically download the image 
    prevLink=soup.select('a[rel="prev"]')[0]
    url='http://xkcd.com'+prevLink.get('href')
            
print('done.')
