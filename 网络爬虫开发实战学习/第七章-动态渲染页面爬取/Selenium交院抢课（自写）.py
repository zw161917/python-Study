from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains
import time
from bs4 import BeautifulSoup
#首页查找数字校园
def ShouYe():
    brower = webdriver.Chrome()
    try:
        brower.get('http://www.njitt.edu.cn/')
        html = brower.page_source
        soup = BeautifulSoup(html, 'lxml')
        usr_li = soup.select('.kstd li')
        for li in usr_li:
            usr_a = li.select('a')
            for u_a in usr_a:
                print(u_a)
                href = u_a.attrs['href']
            break
    finally:
        brower.close()
    DengLu(href)
#用户登录
def DengLu(dl_url):
    #dl_url = 'http://my.njitt.edu.cn/'
    brower = webdriver.Chrome()
    try:
        brower.get(dl_url)
        #抓捕用户名文本框
        input_name = brower.find_element_by_id("u")
        input_pass = brower.find_element_by_id("p")
        input_que = brower.find_element_by_id("login_btn")
        #time.sleep(2)
        input_name.clear()
        input_name.send_keys('174041222')
        #time.sleep(2)
        input_pass.clear()
        input_pass.send_keys('161917')
        #time.sleep(2)
        input_que.click()
        #time.sleep(2)
        MenHu(brower)
    finally:
        brower.close()


#跳转到教务管理系统
def MenHu(brower):
    #wait = WebDriverWait(brower, 10)
    #获取当前页面句柄
    cur_window = brower.current_window_handle
    html = brower.page_source

    soup = BeautifulSoup(html,'lxml')
    jiaowu = soup.select('.mulservicesView .mulservices_title a')
#遍历
    for jw in jiaowu:
        if jw !=[]:
            brower.find_element_by_link_text(u'教务管理').click()
            #time.sleep(3)
            #获取跳转页面句柄
            cur_hand = brower.window_handles
            for handle in cur_hand:  # 轮流得出标签页的句柄 切换窗口 因为只有两个标签页实际是假for循环
                if handle != cur_window:
                    brower.switch_to_window(handle)
                    XuanKe(brower)
            break

#点击选课
def XuanKe(brower):
    html = brower.page_source
    soup = BeautifulSoup(html,'lxml')

    #ul = brower.find_element_by_id('ext-gen45')
    wait = WebDriverWait(brower, 10)
    gonggong = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#ext-gen34 > div > li:nth-child(3) > div > a > span')))
    gonggong.click()
    time.sleep(2)
    #print(brower.page_source)
    tobe = soup.select('109')
    for to in tobe:
        print(to)
    ele_id = "#ext-gen43 > li > div > a > span"

    param = (By.ID, ele_id)
    WebDriverWait(brower, 10).until(EC.visibility_of_element_located(param))
    brower.find_element_by_id(ele_id).click()
    # chaozuo = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#ext-gen45 > li > div > a > span')))
    # chaozuo.click()
    # xuanxiu = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#ext-gen48 > li:nth-child(1) > div > a')))
    # xuanxiu.click()
    time.sleep(3)



if __name__=="__main__":
    ShouYe()
