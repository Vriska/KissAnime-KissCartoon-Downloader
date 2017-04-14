import requests
import sys
import time
import os
def download(x,z,y): #downloads episode from URL
        URL = x
        r = requests.get(URL,stream=True)
        k = (r.headers.get('content-length'))
        k = float(k)
        c = round(k/(1024*1024),3)
        t1 = 1
        with open ( str(z) +'\\' + str(y) +'.mp4', 'wb') as file :
            for chunk in r.iter_content(chunk_size=1024*1024):
                    file.write(chunk)
                    rate = round(1/(time.clock()-t1),3)
                    print ('RATE = ' +str(rate) +' MB/s')
                    t1 = time.clock()
                    size = round(float(os.path.getsize(str(z)+'\\'+ str(y) +'.mp4'))/(1024*1024),3)
                    print ('DOWNLOADED = ' + str(size) + ' of '+ str(c) + '\n Percentage = ' + str(round((size/c)*100,3))+' \n ETA: ' + str(round(((c - size)/rate)/60,3))+ ' Mins')



