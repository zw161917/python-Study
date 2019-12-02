import urllib.parse
import requests
from lxml import etree
word = input('请输入您要查找的图书：')

headers={
    'User-Agent':'',
    'Referer':'http://www.dangdang.com/?_utm_sem_id=16365726&_ddclickunion=620-kw-%D7%DC%D5%CB%BB%A7-%C6%B7%C5%C6%B4%CA_%BA%CB%D0%C4-%CA%D7%D2%B3_%B5%B1%B5%B1%CD%F8%B9%D9%CD%F8%B9%BA%CA%E9%CA%D7%D2%B3|ad_type=0|sys_id=1',
}
url = 'http://search.dangdang.com/?'
data = {
    'key':word,
    'act':'input',
}
query_string = urllib.parse.urlencode(data)
url =url + query_string
response = requests.get(url = url,headers = headers).text
s = etree.HTML(response)
file2 = ''
for i in range(1,6):
    t = '//*[@class="line{0}"]/a/@title'.format(i)
    file = s.xpath(t)
    print(file)