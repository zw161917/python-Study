from bs4 import BeautifulSoup
import re
'''
#解析器
soup = BeautifulSoup('<p>Hello<p>','lxml')
print(soup.p.string)
'''
html = """
<html>
    <head>
        <title>The Dormouse's story</title>
    </head>
    <body>
        <p class="story">
            Once upon a time there were three little sisters; and their names were
            <a href="http://example.com/elsie" class="sister" id="link1">
                <span>Elsie</span>
            </a>
            <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> 
            and
            <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>
            and they lived at the bottom of a well.
        </p>
        <p class="story">...</p>
"""
#BeautifulSoup的基本用法,prettify()方法把解析的字符串以标准的格式输出
'''
soup = BeautifulSoup(html,'lxml')
print(soup.prettify())
print(soup.title.string)
'''
#选择元素,type()获取类型
'''
soup = BeautifulSoup(html, 'lxml')
print(soup.title)
print(type(soup.title))
print(soup.title.string)
print(soup.head)
print(soup.p)
'''
#获取属性
'''
soup = BeautifulSoup(html, 'lxml')
print(soup.p.attrs)
print(soup.p.attrs['name'])
print(soup.p['name'])
print(soup.p['class'])
#获取内容
print(soup.p.string)
#嵌套选择
print(type(soup.head.title))
print(soup.head.title.string)
'''
#关联选择，contents属性返回所有直接子节点
'''
soup = BeautifulSoup(html, 'lxml')
print(soup.p.contents)
#children属性可以得到相同的内容，不过children返回的是生成器类型需要进行循环输出
print(soup.p.children)
for i,child in enumerate(soup.p.children):
    print(i,child)
#descendants属性可以得到所有子孙节点
print(soup.p.descendants)
for i,child in enumerate(soup.p.descendants):
    print(i,child)
'''
#parent属性可以获取某个节点的父节点,parents获取所有祖先节点parents返回的是生成器类型
'''
soup = BeautifulSoup(html, 'lxml')
print(soup.a.parent)
print(soup.a.parents)
print(list(enumerate(soup.a.parents)))
'''
htmls = """
<html>
    <body>
        <p class="story">
            Once upon a time there were three little sisters; and their names were
            <a href="http://example.com/elsie" class="sister" id="link1">
                <span>Elsie</span>
            </a>
            Hello
            <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> 
            and
            <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>
            and they lived at the bottom of a well.
        </p>
"""
#获取同级节点
'''
soup = BeautifulSoup(htmls, 'lxml')
print('next_sibling(下一个节点元素):',soup.a.next_sibling)
print('previous_sibling(上一个节点元素)：',soup.a.previous_sibling)
print('next_siblings(返回后面节点元素):',list(enumerate(soup.a.next_siblings)))
print('previous_siblings(返回前面节点元素)：',list(enumerate(soup.a.previous_siblings)))
'''
#提取信息
htmlss = """
<html>
    <body>
        <p class="story">
            Once upon a time there were three little sisters; and their names were
            <a href="http://example.com/elsie" class="sister" id="link1">Bob</a><a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> 
        </p>
"""
'''
soup = BeautifulSoup(htmlss, 'lxml')
print('Next sibling:')
print(type(soup.a.next_sibling))
print(soup.a.next_sibling)
print(soup.a.next_sibling.string)
print('Parent:')
print(type(soup.a.parents))
print(list(soup.a.parents)[0])
print(list(soup.a.parents)[0].attrs['class'])
'''
htmlsss='''
<div class="panel">
    <div class="panel-heading">
        <h4>Hello</h4>
    </div>
    <div class="panel-body">
        <ul class="list" id="list-1" name="elements">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
            <li class="element">Jay</li>
        </ul>
        <ul class="list list-small" id="list-2">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
        </ul>
    </div>
</div>
'''
'''
#方法选择器
#find_all():查询符合条件的元素
soup = BeautifulSoup(htmlsss, 'lxml')
print(soup.find_all(name='ul'))
print(type(soup.find_all(name='ul')[0]))
#嵌套查询
for ul in soup.find_all(name='ul'):
    print(ul.find_all(name='li'))
    for li in ul.find_all(name='li'):
        print(li.string)
#attrs传入属性查询
print(soup.find_all(attrs={'id':'list-1'}))
print(soup.find_all(attrs={'name':'elements'}))
#直接传入属性查询
print(soup.find_all(id = 'list-1'))
print(soup.find_all(class_='element'))
#text参数用来匹配节点的文本
'''
html='''
<div class="panel">
    <div class="panel-body">
        <a>Hello, this is a link</a>
        <a>Hello, this is a link, too</a>
    </div>
</div>
'''
'''
from bs4 import BeautifulSoup
soup = BeautifulSoup(html, 'lxml')
print(soup.find_all(text=re.compile('link')))
'''
#find()返回第一个匹配的元素，返回值并不是数组
html='''
<div class="panel">
    <div class="panel-heading">
        <h4>Hello</h4>
    </div>
    <div class="panel-body">
        <ul class="list" id="list-1">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
            <li class="element">Jay</li>
        </ul>
        <ul class="list list-small" id="list-2">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
        </ul>
    </div>
</div>
'''
'''
soup = BeautifulSoup(html, 'lxml')
print(soup.find(name='ul'))
print(type(soup.find(name='ul')))
print(soup.find(class_='list'))
'''
'''
find_parents()和find_parent()：前者返回所有祖先节点，后者返回直接父节点。
find_next_siblings()和find_next_sibling()：前者返回后面所有的兄弟节点，后者返回后面第一个兄弟节点。
find_previous_siblings()和find_previous_sibling()：前者返回前面所有的兄弟节点，后者返回前面第一个兄弟节点。
find_all_next()和find_next()：前者返回节点后所有符合条件的节点，后者返回第一个符合条件的节点。
find_all_previous()和find_previous()：前者返回节点后所有符合条件的节点，后者返回第一个符合条件的节点
'''
#css选择器，调用select()方法
html='''
<div class="panel">
    <div class="panel-heading">
        <h4>Hello</h4>
    </div>
    <div class="panel-body">
        <ul class="list" id="list-1">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
            <li class="element">Jay</li>
        </ul>
        <ul class="list list-small" id="list-2">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
        </ul>
    </div>
</div>
'''
'''
soup = BeautifulSoup(html, 'lxml')
print(soup.select('.panel .panel-heading'))
print(soup.select('ul li'))
print(soup.select('#list-2 .element'))
print(type(soup.select('ul')[0]))
'''
#嵌套选择
soup = BeautifulSoup(html, 'lxml')
for ul in soup.select('ul'):
    print(ul.select('li'))
#获取属性
for ul in soup.select('ul'):
    print(ul['id'])
    print(ul.attrs['id'])
#获取文本get_text()与string效果一样
for li in soup.select('li'):
    print('get_text:',li.get_text())
    print('string:',li.string)











































