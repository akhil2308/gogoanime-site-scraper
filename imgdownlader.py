from bs4 import BeautifulSoup
import requests
import time
start_time = time.time()
num=1
print("process now begining")
for itak in range(1,2):
    url1='https://www09.gogoanimes.tv/anime-list.html?page='+str(itak)
    source1=requests.get(url1).text
    soup1= BeautifulSoup(source1,'lxml')

    lastep1=soup1.find('div',class_="anime_list_body").ul
    for link in lastep1.find_all('li'):
        x=link.a
     
      
        
        #in the website link
        url='https://www09.gogoanimes.tv/'+x['href']
        source=requests.get(url).text
        soup= BeautifulSoup(source,'lxml')
        lastep=soup.find('div',class_="anime_info_body_bg")
        
        #anime image link
        image_url =lastep.img["src"]
        
        #image name
        name=str(num)+'.png'
        num=num+1
        r = requests.get(image_url) 
          
        with open(name,'wb') as f: 

            f.write(r.content) 
        
print("--- %s seconds ---" % (time.time() - start_time))
