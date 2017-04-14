from bs4 import BeautifulSoup
import requests
import cfscrape
import sys
import time
import VRSKd
import re

from selenium import webdriver

def __del__(self):
    type(self).count -= 1

def get(x):             #Gets list of indivdual episodes in kisscartoon/anime in kiss cartons 
    FIRE =''
    path = r'C:\\Program Files\\PhantomJS\\hlb.exe'
    browser = webdriver.PhantomJS(path)
    browser.set_window_size(1400, 1000)
    browser.get(x)
    time.sleep(10)
    k = browser.page_source
    try :
        browser.quit()
    except :
        pass


    soup = BeautifulSoup(k,'html.parser')

    for a in soup.find_all('a',string=re.compile('HERE')):
        FIRE = a.get('href')
    return FIRE
