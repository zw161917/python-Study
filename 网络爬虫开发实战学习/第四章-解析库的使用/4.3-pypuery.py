from pyquery import PyQuery as pq
html = '''
<div>
    <ul>
         <li class="item-0">first item</li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
         <li class="item-1 active"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a></li>
     </ul>
 </div>
 '''
'''
doc = pq(html)
print(doc('li'))
#url初始化
doc = pq(url='http://cuiqingcai.com')
print(doc('title'))
#文件的初始化
doc = pq(filename='test.html')
print(doc('li'))
'''
#基本css选择器
html = '''
<div class="wrap">
    <div id="container">
        <ul class="list">
             <li class="item-0">first item</li>
             <li class="item-1"><a href="link2.html">second item</a></li>
             <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
             <li class="item-1 active"><a href="link4.html">fourth item</a></li>
             <li class="item-0"><a href="link5.html">fifth item</a></li>
         </ul>
     </div>
 </div>
'''
'''
doc = pq(html)
print(doc('#container .list li'))
print(type(doc('#container .list li')))
'''
'''
#查找节点find()(包括所有的子孙节点)
doc = pq(html)
items = doc('.list')
print(items)
print(type(items))
lis = items.find('li')
print(lis)
print(type(lis))
#只查找子节点children()
lis = items.children()
print(type(lis))
print(lis)
print(type(lis))
lis = items.children('.active')
print(lis)
#获取父节点parent()
container = items.parent()
print(container)
print(type(container))
#查找祖先节点
parents = items.parents()
print(type(parents))
print(parents)
'''
'''
#筛选祖先节点
doc = pq(html)
items = doc('.list')
parent = items.parents('.wrap')
print(parent)
#兄弟节点
li = doc('.list .item-0.active')
print(li.siblings())
print(li.siblings('.active'))
#遍历
li = doc('.item-0.active')
print(li)
print(str(li))
lis = doc('li').items()
print(type(lis))
for li in lis:
    print(li,type(li))
'''
'''
#获取属性attr()
doc = pq(html)
a = doc('.item-0.active a')
print(a,type(a))
print(a.attr('href'))
#属性的遍历
a = doc('a')
for item in  a.items():
    print(item.attr('href'))
#节点操作
doc = pq(html)
li = doc('.item-0.active')
print(li)
li.removeClass('active')
print(li)
li.addClass('active')
print(li)
#可以用text()和html()方法来改变节点内部的内容
doc = pq(html)
li = doc('.item-0.active')
print(li)
li.attr('name', 'link')
print(li)
li.text('changed item')
print(li)
li.html('<span>changed item</span>')
print(li)
'''
#remove()方法就是移除
html = '''
<div class="wrap">
    Hello, World
    <p>This is a paragraph.</p>
 </div>
'''
doc = pq(html)
wrap = doc('.wrap')
print(wrap.text())
wrap.find('p').remove()
print(wrap.text())
#伪类选择器
html = '''
<div class="wrap">
    <div id="container">
        <ul class="list">
             <li class="item-0">first item</li>
             <li class="item-1"><a href="link2.html">second item</a></li>
             <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
             <li class="item-1 active"><a href="link4.html">fourth item</a></li>
             <li class="item-0"><a href="link5.html">fifth item</a></li>
         </ul>
     </div>
 </div>
'''
doc = pq(html)
#第一个节点
li = doc('li:first-child')
print(li)
#最后一个节点
li = doc('li:last-child')
print(li)
#第二个节点
li = doc('li:nth-child(2)')
print(li)
#第三个节点
li = doc('li:gt(2)')
print(li)
#第偶数个节点
li = doc('li:nth-child(2n)')
print(li)
#包含second文本的节点
li = doc('li:contains(second)')
