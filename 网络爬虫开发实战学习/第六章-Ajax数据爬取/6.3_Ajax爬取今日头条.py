# Ajax爬取今日头条图片
import requests
from urllib.parse import urlencode

from asn1crypto._ffi import null
from bs4 import BeautifulSoup

# 获取url
def Html_url():
    had = {'offset': '20',
           'format': 'json',
           'keyword': '街拍',
           'autoload': 'true',
           'count': '20',
           'cur_tab': '1',
           'from': 'search_tab',
           'pd': 'synthesis', }
    url = 'https://www.toutiao.com/search_content/?'+urlencode(had)
    try:
        respone = requests.get(url)
        if respone.status_code == 200:
            return respone.json()
    except requests.ConnectionError:
        return None


def Html_Neirong():
    resption = Html_url()
    for res in resption.get('data'):
        if  res.get('cell_type') is not None:
            continue
        title = res.get('title')
        images = res.get('image_list')
        for re in res.get('image_list'):
            yield {
                'image': 'https:' + re.get('url'),
                'title': title
            }






if __name__ == '__main__':
    Html_Neirong()
