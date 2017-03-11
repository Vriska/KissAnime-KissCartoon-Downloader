import requests
from bs4 import BeautifulSoup
import cfscrape
import re
import VRSKacq
import VRSKd
import os
import js2py 


def  get(x):
    list = []
    scraper = cfscrape.create_scraper()
    r = scraper.get(x)
    s = str(r.content,encoding='utf-8')
    soup = BeautifulSoup(s,'html.parser')
    for link in soup.find_all('a',string=re.compile('Episode')):
        list.append(link.get('href'))
    list.reverse()
    new_list = ['http://www.kisscartoon.me/' + x for x in list]
    return new_list

k = str(input('INSERT ANIME LIST URL '))
k = k.strip()
print(k)
m = input('DIRECTORY: ')
m = m.replace("\\","\\\\")
m = m.strip()
p = input('DESIGNATE NAME: ')
q = int(input('START FROM ? 1 = FIRST EPISODE '))
L = get(str(k))
c = q
L = L[q-1:]

print (L)
for links in L:
    links=str(links)
    print(links)
    source = VRSKacq.get(links)
    while True :
        try :
            VRSKd.download(source,str(m),str(p) +' Episode ' +str(c))
        except :
            continue
        c = c + 1
        os.system('cls')
        break
    
input("Press Enter to continue...")
