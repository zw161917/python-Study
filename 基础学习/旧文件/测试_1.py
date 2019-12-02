import requests
import uuid
from bs4 import BeautifulSoup

response = requests.get(url='http://page.renren.com/register/regGuide/')
response.encoding = response.aparent_encoding
soup = BeautifulSoup(response.text, features='html.parser')
target = soup.find(id='bd-content clearfix')
list_li = target.find_all('li')
for i in list_li:
    a = i.find('a')
    if a:
        print(a.attrs.get('href'))
        txt = a.find('h3').text
        print(txt)
        img_url = a.find('img').attrs.get('src')

        print(img_url)