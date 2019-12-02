#使用bs4爬取房产信息

import requests

import os
from bs4 import BeautifulSoup

class HouseInfo:
    def __init__(self,image,title,totalPrice,unitPrice):
        self.image = image
        self.title = title
        self.totalPrice = totalPrice
        self.unitPrice = unitPrice
        self.loclImage = ""

    def __str__(self):
        return "标题：{}  总价：{}万   单价：{}   图片：{}   本地路径：{}".format(self.title,self.totalPrice,self.unitPrice,self.image,self.loclImage)
#判断文件夹不存在，并创建文件夹
class spider:
    def __init__(self):
        self.currentPage = -1
        if not os.path.exists("Demo22"):  #判断文件夹是否存在

            os.makedirs("Demo22")   #创建文件夹


    # 判断文件不存在，并创建文件
    def setCurrentPage(self,page):
        self.currentPage = page
        path = "Demo22/{}".format(page)
        if not os.path.exists(path):
            os.makedirs(path)


    #获取html数据
    def getHtmlData(self,page):
        self.setCurrentPage(page)
        url = 'https://nj.lianjia .com/ershoufang/pg{}/'.format(page)
        head = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'

        }
        #发送请求
        response = requests.get(url,headers=head)
        #获取数据
        html = response.content.decode("utf8")
        self.getDataFromHtml(html)

    #解析html，获取相关信息
    def getDataFromHtml(self,html):
        soup = BeautifulSoup(html,"html.parser")
        liList = soup.select(".sellListContent li")
        houseList = []
        for li in liList:
            imgeUrl = li.select("img")[0]["data-original"]

            title = (li.select(".title a")[0]).string
            totalPrice = li.select(".priceInfo .totalPrice span")[0].string
            unitPrice = li.select(".priceInfo .unitPrice span")[0].string
            houseInfo = HouseInfo(imgeUrl,title,totalPrice,unitPrice)
            houseList.append(houseInfo)
        print(houseList)
        self.saveData(houseList)


    #存储数据
    def saveData(self,houseList):
        with open("Demo22/info.txt",'a',encoding="utf8") as f:
            for house in houseList:
                localPath = self.saveImageData(house.image)
                house.loclImage = localPath
                f.write(house.__str__())
                f.write("\n")
                f.flush()

        #开始爬虫
    def beginSpider(self,beginPage,size):
        for page in range(beginPage,beginPage+size):
            self.getHtmlData(page)

    #下载图片
    def saveImageData(self,imageURL):
        response = requests.get(imageURL)
        data = response.content
        nameList = imageURL.split("/")
        name = nameList[len(nameList)-1]
        path = "Demo22/{}/{}".format(self.currentPage,name)
        with open(path,"wb") as f:
            f.write(data)



if __name__ =="__main__":
    spider = spider()
    spider.beginSpider(1,3)