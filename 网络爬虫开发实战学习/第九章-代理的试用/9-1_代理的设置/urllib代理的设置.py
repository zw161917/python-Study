from urllib.error import URLError
from urllib.request import ProxyHandler,build_opener

#基础的urllib的代理设置方法
def urllib_jichu():
    proxy= '127.0.0.1:9743'
    proxy_handler = ProxyHandler({
         'http':'http://'+proxy,
        'https':'https://'+proxy
    })
    opener = build_opener(proxy_handler)
    try:
        print(123)
        response = opener.open('http://httpbin.org/get')
        print(response.read().decode('utf-8'))
    except URLError as e:
        print(1234)
        print(e.reason)
#需要认证的代理时
def urllib_renzheng():
    proxy = 'username:password@127.0.0.1:9743'
    proxy_handler = ProxyHandler({
        'http': 'http://' + proxy,
        'https': 'https://' + proxy
    })
    opener = build_opener(proxy_handler)
    try:
        print(123)
        response = opener.open('http://httpbin.org/get')
        print(response.read().decode('utf-8'))
    except URLError as e:
        print(12345)
        print(e.reason)

def urllib_socks5():
    import socks
    import socket
    from urllib import request
    from urllib.error import URLError
    socks.set_default_proxy(socks.SOCKS5,'127.0.0.1',9742)
    socket.socket = socks.socksocket
    try:
        print(123)
        response = request.urlopen('http://httpbin.org/get')
        print(response.read().decode('utf-8'))
    except URLError as e:
        print(12345)
        print(e.reason)
#requests代理设置
def requests_daili():
    import requests
    proxy = '127.0.0.1:9743'
    proxy_handler = ProxyHandler({
        'http': 'http://' + proxy,
        'https': 'https://' + proxy
    })

    try:
        respones = requests.get('http://httpbin.org/get')
        print(respones.text)
    except requests.exceptions.ConnectionError as e:
        print('Error',e.args)

#requests使用COCKS5代理
def requesrts_socks():
    import requests
    proxy = '127.0.0.1:9743'
    proxies = {
        'http':'socks5://'+proxy,
        'https':'socks5://'+proxy
    }
    try:
        respones = requests.get('http://httpbin.org/get')
        print(respones.text)
    except requests.exceptions.ConnectionError as e:
        print('Error',e.args)

#requests使用socks模块
def requests_socksmo():
    import requests
    import socks
    import socket
    socks.set_default_proxy(socks.SOCKS5,'127.0,0,1',9742)
    socket.socket = socks.socksocket
    try:
        respones = requests.get('http://httpbin.org/get')
        print(respones.text)
    except requests.exceptions.ConnectionError as e:
        print('Error',e.args)
#selenium设置代理
def selenium_chrome():
    from selenium import webdriver
    proxy = '127.0.0.1:9743'
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--proxy-server=http://'+proxy)
    browser = webdriver.Chrome(chrome_options=chrome_options)
    browser.get('http://httpbin.org/get')

#selenium认证代理
def selenium_ren():
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
    import zipfile
    ip = '127.0.0.1'
    port = 9743
    username = 'foo'
    password = 'bar'
    manifest_json = """
        {"version":"1.0.0",
        "manifest_version":"2",
        "name":"Chrome Proxy",
        "permissions":[
            "proxy",
        "tab s",
        "unlimitedStorage",
        "storage",
        "<all_urls>",
        "webRequest",
        "webRequestBlocking"],
        "background":{
        "scripts":["background.js "]
        }
        }
    """
    background_js = """
        var config =  {
            mode:"fixed",
            rules:{
                singleProxy:{
                    scheme:"http",
                    host:"%(ip)s",
                    port:%(prot)s
                }
            }
        }
        chrome.proxy.settings.set({value:config,scope:"regular"},function(){});
        function callbackFn(){
            return{
                authCredentials:{
                    username:"%(username)s",
                    password:"%(password)s"
                }
            }
        }
        chrome.webRequest.onAuthRequired.addListener(
            callbackFu,
            {urls:["<all_urls>"]},
            {'blocking'}
        )
    """% {'ip': ip, 'port': port, 'username': username, 'password': password}
    plugin_file = 'proxy_auth_plugin.zip'
    with zipfile.ZipFile(plugin_file,'w') as zp:
        zp.writestr("manifest.json",manifest_json)
        zp.writestr("background.js",background_js)
        chrome_options = Options()
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_extension(plugin_file)
        browser = webdriver.Chrome(chrome_options = chrome_options)
        browser.get('http://httpbin.org/get')
#selenium认证代理2
def selenium_ren2():
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
    import zipfile

    ip = '127.0.0.1'
    port = 9743
    username = 'foo'
    password = 'bar'

    manifest_json = """
    {
        "version": "1.0.0",
        "manifest_version": 2,
        "name": "Chrome Proxy",
        "permissions": [
            "proxy",
            "tabs",
            "unlimitedStorage",
            "storage",
            "<all_urls>",
            "webRequest",
            "webRequestBlocking"
        ],
        "background": {
            "scripts": ["background.js"]
        }
    }
    """

    background_js = """
    var config = {
            mode: "fixed_servers",
            rules: {
              singleProxy: {
                scheme: "http",
                host: "%(ip)s",
                port: %(port)s
              }
            }
          }
    chrome.proxy.settings.set({value: config, scope: "regular"}, function() {});
    function callbackFn(details) {
        return {
            authCredentials: {
                username: "%(username)s",
                password: "%(password)s"
            }
        }
    }
    chrome.webRequest.onAuthRequired.addListener(
                callbackFn,
                {urls: ["<all_urls>"]},
                ['blocking']
    )
    """ % {'ip': ip, 'port': port, 'username': username, 'password': password}

    plugin_file = 'proxy_auth_plugin.zip'
    with zipfile.ZipFile(plugin_file, 'w') as zp:
        zp.writestr("manifest.json", manifest_json)
        zp.writestr("background.js", background_js)
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_extension(plugin_file)
    browser = webdriver.Chrome(chrome_options=chrome_options)
    browser.get('http://httpbin.org/get')



if __name__ == '__main__':
    selenium_ren2()