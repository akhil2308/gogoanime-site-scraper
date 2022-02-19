from bs4 import BeautifulSoup
import requests
import csv
import json
import time
start_time = time.time()
img=[]
name=[]
animetype=[]
plot=[]
animegenre=[]
released=[]
starus=[]
k=[]
num=1
print("process now begining")
for itak in range(1,45):
    url1='https://www09.gogoanimes.tv/anime-list.html?page='+str(itak)
    source1=requests.get(url1).text
    soup1= BeautifulSoup(source1,'lxml')

    lastep1=soup1.find('div',class_="anime_list_body").ul
    for link in lastep1.find_all('li'):
        x=link.a
     
        k.append('https://www09.gogoanimes.tv/'+x['href'])
    
        
        #in the website link
        url='https://www09.gogoanimes.tv/'+x['href']
        source=requests.get(url).text
        soup= BeautifulSoup(source,'lxml')
        lastep=soup.find('div',class_="anime_info_body_bg")
        
        #anime image link
        image_url =lastep.img["src"]
        
        #image name
        name1=str(num)+'.png'
        num=num+1
        r = requests.get(image_url) 
          
        with open(name1,'wb') as f: 

            f.write(r.content)
        img.append(name1)
        
        #anime name
        name.append(lastep.h1.text)
        
        #in the anime information
        anime_detail_itterate=1
        for animedetails in lastep.find_all('p',class_="type"):
          #anime type
          if(anime_detail_itterate==1):
              animetype.append(animedetails.a["title"])
              
          # anime gener
          elif(anime_detail_itterate==3):
            #print(animedetails.span.text)
            i=1
            l=''
            for genre in lastep.find_all('a'):
                if i==1 or i==2:
                  ak=1
                else:
                  l=l+genre.text
                i=i+1
            animegenre.append(l)
            
          #anime plotsummary 
          elif(anime_detail_itterate==2):
              #print(animedetails.span.text)
               plot.append(animedetails.text)
               
          #anime released  
          elif(anime_detail_itterate==4):
            released.append(animedetails.text)
            
          #anime status
          else:
               starus.append(animedetails.text)
             
          anime_detail_itterate= anime_detail_itterate+1
    print('compleated',itak)

print("compleaed")
print("now begining creating file")
data = {}  
data['links'] = [] 
for i in range(0,len(k)):
 data['links'].append({
    'imglink':img[i],
    'name':name[i],
    'plot':plot[i],
    'type':animetype[i],
    'genre':animegenre[i],
    'released':released[i],
    'status':starus[i],
    'link':k[i]
 })

with open('data.json', 'w') as outfile:  
    json.dump(data, outfile, indent=4)
    outfile.write('\n')
print("compleaed process")
print("--- %s seconds ---" % (time.time() - start_time))
