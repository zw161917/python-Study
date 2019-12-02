import requests
from lxml import etree
class Housing():

    def __init__(self):
        pass

    def __str__(self):
        pass

    #获取responst对象
    def getHtmlurl(self,url):
        headres = {
            'User-Agent': 'Mozilla/5.0(Windows NT 10.0;WOW64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/67.0.3396.62Safari/537.36'
        }
        responts = requests.get(url,headers=headres)
        return responts

    #用正则解析数据
    def getHtmlRegular(self,responts):
        pass

    #用X-path解析数据
    def getHtmlLxml(self,responts):
        pass

    #文本数据存储
    def getHtmlText(self,item):
        pass

    #判断文本文件是否存在
    def getHtmlJudge(self,text):
        pass

    #主程序运行
    def main(self):
        url = 'https://nj.lianjia.com/ershoufang/'
        response = self.getHtmlurl(url)
        self.getHtmlRegular(response)

if __name__ == '__main__':
    c = Housing()
    c.main()

