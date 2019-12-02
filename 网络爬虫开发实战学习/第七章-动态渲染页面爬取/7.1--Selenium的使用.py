from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains
import time
'''
browser = webdriver.Chrome()
try:
    #browser.get('https//www.baidu.com')
    browser.get('https://www.baidu.com')
    #按id查找此元素的子元素
    input = browser.find_element_by_id('kw')
    #模拟要输入的值
    input.send_keys('python')
    #模拟键入回车
    input.send_keys(Keys.ENTER)
    #等待元素加载，第二个参数为可等待加载的时长
    wait = WebDriverWait(browser,10)
    #EC.presence_of_element_located表示判断元素存不存在这个页面
    wait.until(EC.presence_of_element_located((By.ID,'content_left')))
    #输出网址
    print(browser.current_url)
    #输出cookies
    print(browser.get_cookies())
    #输出网页源代码
    print(browser.page_source)
finally:
    browser.close()
'''
'''
#访问淘宝
browser = webdriver.Chrome()
browser.get('https://www.taobao.com')
#获取输入框
input_first = browser.find_element_by_id('q')
#输入内容
input_first.send_keys('iPhone')
time.sleep(1)
input_first.clear()
input_first.send_keys('iPad')
input_css = browser.find_element_by_css_selector('#q')
input_xpath = browser.find_element_by_xpath('//*[@id="q"]')
#获取主题商场
lis = browser.find_elements_by_css_selector('.service-bd li')
lis = browser.find_elements(By.CSS_SELECTOR,'.service-bd li')
#print(browser.page_source)
#print(input_first,input_css,input_xpath)
for li in lis:
    print(li)
browser.close()
'''
#节点交互
def SelJiaohu():
    browser = webdriver.Chrome()
    browser.get('https://www.taobao.com')
    #获取输入框
    input_first = browser.find_element_by_id('q')
    #输入内容
    input_first.send_keys('iPhone')
    time.sleep(1)
    input_first.clear()
    input_first.send_keys('iPad')
    button = browser.find_element_by_class_name('btn-search')
    button.click()
    browser.close()

#动作链
def SelLian():
    browser = webdriver.Chrome()
    browser.get('http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable')
    browser.switch_to.frame('iframeResult')
    source = browser.find_element_by_css_selector('#draggable')
    target = browser.find_element_by_css_selector('#droppable')
    actions = ActionChains(browser)
    actions.drag_and_drop(source, target)
    actions.perform()

#执行JavaScript下拉列表
def SelXiala():
    browser = webdriver.Chrome()
    browser.get('https://www.zhihu.com/explore')
    browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
    browser.execute_script('alert("To Bottom")')

#获取节点信息
def SelJiedian():
    #获取属性
    browser = webdriver.Chrome()
    url = 'https://www.zhihu.com/explore'
    browser.get(url)
    logo = browser.find_element_by_id('zh-top-link-logo')
    print(logo)
    print(logo.get_attribute('class'))
    #获取文本信息
    input = browser.find_element_by_class_name('zu-top-add-question')
    print(input.text)
    #获取id
    print(input.id)
    #位置
    print(input.location)
    #标签名
    print(input.tag_name)
    #大小
    print(input.size)
#切换Frame
from selenium.common.exceptions import NoSuchElementException
def SelFrame():
    url = 'http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
    browser = webdriver.Chrome()
    browser.get(url)
    browser.switch_to.frame('iframeResult')
    try:
        logo = browser.find_element_by_class_name('logo')
    except NoSuchElementException:
        print('No LOGO')
    browser.switch_to.parent_frame()
    logo = browser.find_element_by_class_name('logo')
    print(logo)
    print(logo.text)
#延时等待
def SelDengdaiyin():
    #隐性等待
    browser = webdriver.Chrome()
    browser.implicitly_wait(10)
    browser.get('https://www.zhihu.com/explore')
    input = browser.find_element_by_class_name('zu-top-add-question')
    print(input)
def SelDengdaixian():
    #显式等待
    browser = webdriver.Chrome()
    browser.get('https://www.taobao.com/')
    wait = WebDriverWait(browser, 10)
    input = wait.until(EC.presence_of_element_located((By.ID, 'q')))
    button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.btn-search')))
    print(input, button)

if __name__=="__main__":
    SelDengdaixian()