from bs4 import BeautifulSoup
import requests
import json
import pymongo

#信息处理
def __str__(soup_h1,soup_div,soup_lian,soup_dizhi):

    return "标题：{}  类别：{}    联系人：{}   地址：{}".format(soup_h1,soup_div,soup_lian,soup_dizhi)

#获取内容
def Get_url(url):
    head = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'
    }
    respoen = requests.get(url,headers=head)
    html = respoen.content.decode("utf-8")
    return html
#一级爬取内容
def get_Html(url):
    html = Get_url(url)
    soup = BeautifulSoup(html,'lxml')
    soup_zu = soup.select("#local a")
    i=1
    for soup_a in soup_zu:
        if soup_a.has_attr('class'):
            continue
        soup_text = soup_a.text
        soup_href = soup_a.attrs['href']
        print(soup_text)
        print(soup_href)
        Get_fen(soup_text,soup_href)
        break



#分地区爬去
def Get_fen(name,html):
    url = "https://nj.58.com"+html
    html = Get_url(url)
    soup = BeautifulSoup(html,'lxml')
    soup_dy = soup.select('#jingzhun tr .tdiv a')
    a=1
    for soup_tr in soup_dy:
        if a==2:
            a=1
            continue
        href = soup_tr.attrs['href']
        print(href)
        Get_san(name,href)
        a=2

#三级爬取
def Get_san(name,url):
    html = Get_url(url)
    soup = BeautifulSoup(html, 'lxml')
    #标题
    soup_h1 = soup.select('.detail-title h1')[0].text
    print(soup_h1)
    #类别
    soup_div = soup.select('.infocard__container .infocard__container__item__main ')
    soup_a = soup_div[0].text
    print(soup_a)
    #服务地区
    soup_diqu = soup.select('.infocard__container .infocard__container__item__main a')
    s = 0
    for soup_di in soup_diqu:
        if soup_di.has_attr('class'):
            continue
        s = s + 1
    d = 0
    list = []
    for soup_di in soup_diqu:
        if soup_di.has_attr('class'):
            continue
        list.append(soup_di.text)
        print(list[d])
        d = d + 1
        if d == s - 2:
            break
    get_list(list)
    #联系人
    soup_lian = soup.select('.infocard__container   .infocard__container__item--contact .infocard__container__item__main')[0].text
    print(soup_lian)
    #地址
    soup_dizhi = soup.select( '.infocard__container .infocard__container__item--shopaddress .infocard__container__item__main a')[0].text
    print(soup_dizhi)
    houseList = []
    #houseinfo = __str__(soup_h1,soup_a,soup_lian,soup_dizhi)
    # houseList.append(houseinfo)
    # #fuwu = get_list()
    get_cun(name,soup_h1,soup_lian,soup_dizhi)


#列表处理
def get_list(list):
    s = ","
    a = 0
    for li in list:
        a = a + 1
    b = ""
    for la in range(0, a):
        b = b + list[la] + s
    fuwu = b
    return fuwu
list =[]
#文件处理
def get_cun(name,soup_h1,soup_lian,soup_dizhi):
    #str = get_wen()
    biao = soup_h1
    lian =soup_lian
    di = soup_dizhi
    na = name+'.json'
    join = {
        '标题':biao,
        '联系人':lian,
        '地址':di
    }
    with open(na,'a',encoding='utf-8') as file:
        # for house in houseList:
        #     file.write(house.__str__())
        #     file.write("\t")
        #     file.flush()
        file.write(json.dumps(join, indent=2, ensure_ascii=False))

#存储json

if __name__=="__main__":
    url = 'https://nj.58.com/zuche/?utm_source=sem-baidu-pc&spm=108825632753.26860626569&utm_campaign=sell&utm_medium=cpc'
    get_Html(url)