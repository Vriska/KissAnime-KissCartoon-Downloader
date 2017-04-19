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

def get(x):             #Gets URL of source download page in episode page of kissanime/kisscartoon 
    FIRE =''
    path = r'C:\\Program Files\\PhantomJS\\phantomjs.exe'
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

    FIRE = soup.find('a', string=re.compile('mp4'))
    return FIRE.get('href')
