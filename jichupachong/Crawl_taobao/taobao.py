from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from urllib.parse import quote
from pyquery import PyQuery as pq
import pymongo
browser = webdriver.Chrome()
wait = WebDriverWait(browser,10)
KEYWORD = 'iPad'
#抓取列表页
def index_page(page):
    print('正在爬去第',page,'页')
    try:
        url = 'https://s.taobao.com/search?q='+quote(KEYWORD)
        browser.get(url)
        if page>1:
            #抓取文本框
            input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#mainsrp-pager div.form > input')))
            #抓取转页按钮
            submit = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#mainsrp-pager div.form > span.btn.J_Submit')))
            #清空文字
            input.clear()
            #写入页数
            input.send_keys(page)
            #点击按钮
            submit.click()
            #检查是否跳转到规定页面
        wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,'#mainsrp-pager li.item.active >span'),str(page)))
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'.m-itemlist .items .item ')))
        get_products()
    except:
        index_page(page)
#解析数据
def get_products():
    html = browser.page_source
    doc = pq(html)
    items = doc('#mainsrp-itemlist .grid  .items .item ').items()
    for item in items:
        #print(item.find('.price .span'))


        product = {
            'image': item.find('.pic .img').attr('data-src'),
            'price': item.find('.price').text(),
            'deal': item.find('.deal-cnt').text(),
            'title': item.find('.title').text(),
            'shop': item.find('.shop').text(),
            'location': item.find('.location').text()
        }
        print(product)
        save_to_mongo(product)

#保存到MongDB
mongo_url = 'localhost'
mongo_db = 'taobao'
mingo_coll = 'products'
client = pymongo.MongoClient(mongo_url)
db = client[mongo_db]
def save_to_mongo(result):
    try:
        if db[mingo_coll].insert(result):
            print('存储数据成功')
    except:
        print('存储数据失败')

#遍历页
def main():
    for i in range(1,101):
        index_page(i)

if __name__=="__main__":
    main()