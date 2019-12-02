import requests
from bs4 import BeautifulSoup
#爬取51jop招聘信息

def __str__(zhiye2,gongshi,didian,xinshui):
    return "职业：{}  公司：{}   地点：{}   薪水：{}".format(zhiye2, gongshi, didian,xinshui)
#获取数据
def getHtml(can):
    url = 'https://search.51job.com/list/070200,000000,0000,00,9,99,python,2,{}.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare='.format(can)
    head = {
        'User - Agent': 'Mozilla / 5.0(Windows NT 10.0; WOW64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 67.0.3396.62Safari / 537.36'
    }
    repeses  = requests.get(url)
    html = repeses.content.decode('gbk')
    getDataHtml(html)
#获取相关信息
def getDataHtml(html):
    soup = BeautifulSoup(html,"html.parser")
    liList = soup.select(".el")

    houseList = []
    for li in liList:
        zhiye = li.select("p span a")
        if zhiye==[]:
            continue
        zhiye2 = li.select("p span a")[0].string
        gongshi = li.select(".t2")[0].string
        didian = li.select(".t3")[0].string
        xinshui = li.select(".t4")[0].string
        houseinfo = __str__(zhiye2,gongshi,didian,xinshui)
        houseList.append(houseinfo)

    getHtmlChunchu(houseList)
#数据的存储
def getHtmlChunchu(shuju):
    with open("shuju.txt", 'a', encoding="utf8") as f:
        for house in shuju:
            f.write(house.__str__())
            f.write("\n")
            f.flush()


if __name__=='__main__':
    for i in range(1,11):
        getHtml(i)


