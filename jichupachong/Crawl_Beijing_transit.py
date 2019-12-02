import  requests
from bs4 import BeautifulSoup
def zan1(zan):
    return zan
def html():
    usr = 'http://beijing.8684.cn/x_24f5dad9'
    reporion = requests.get(usr)
    html = reporion.content.decode('utf-8')
    soup = BeautifulSoup(html,'lxml')
    div = soup.select('.bus_line_content')
    for di in div:
        name = di.select('.bus_i_t1 h1')[0].string
        types = di.select('.bus_i_t1 a')[0].string
        time = di.select('.bus_i_t4')[0].string
        price = di.select('.bus_i_t4')[1].string
        company = di.select('.bus_i_t4 a')[0].string
        update = di.select('.bus_i_t4')[3].string
        mileage = di.select('.bus_label .bus_label_t2')[0].string
        totex = di.select('.bus_line_txt strong')[0].string
        site = di.select('.bus_site_layer')[0]
        a=0
        listzan =[]
        for sites in site:
            zan = site.select('div a')[a].string
            a = a+1
            zams = zan1(zan)
            listzan.append(zams)
#        with open('exp.txt', 'w', encoding='utf-8') as file:
 #           file.write('\n'.join([name, types, time,price,company,update,mileage,totex,listzan]))

html()