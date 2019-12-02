import requests
from bs4 import BeautifulSoup

#获取数据
def DateHtml():
    url = 'https://read.qidian.com/chapter/CJ37WFuiFctwKI0S3HHgow2/aNgDOgvhRGuaGfXRMrUjdw2'
    head = {
        'User - Agent': 'Mozilla / 5.0(Windows NT 10.0; WOW64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 67.0 .3396.62Safari / 537.36'
    }
    repeses = requests.get(url,head)
    html = repeses.content.decode("utf8")
    getDateHtml(html)
#获取相关信息
def getDateHtml(html):
    soup = BeautifulSoup(html,"html.parser")
    liList = soup.select(".text-head .j_chapterName")[0].string
    liLists = soup.select(".main-text-wrap .read-content ")
    for li in liLists:
        liZhengWen = li.select("p")

        for lis in liZhengWen:

            lizheng = lis.select("p")[0].string
            if lizheng == []:
                continue
            print(lizheng)
        #print(liZhengWen)
    #print(liLists)

DateHtml()