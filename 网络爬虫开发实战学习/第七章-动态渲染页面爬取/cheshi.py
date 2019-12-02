from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains
import time
from pyquery import PyQuery as pq
from bs4 import BeautifulSoup
brower = webdriver.Chrome()
try:
    brower.get('http://www.njitt.edu.cn/')
    html = brower.page_source
    #print(html)
    soup = BeautifulSoup(html,'lxml')
    usr_li = soup.select('.kstd li')
    for li in usr_li:
        usr_a = li.select('a')
        for u_a in usr_a:
            print(u_a)
            print(u_a.attrs['href'])
        break
finally:
    brower.close()