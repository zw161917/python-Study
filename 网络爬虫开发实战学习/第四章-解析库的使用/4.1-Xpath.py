from lxml import etree

text = '''
<div>
     <ul>
         <li class="item-0"><a href="link1.html"><span>first item</a></li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-inactive"><a href="link3.html">third item</a></li>
         <li class="item-1"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a></li>
     </ul>
</div>
'''
#初始化，构造解析对象
'''
html = etree.HTML(text)
result = etree.tostring(html)
#print(result.decode('utf-8'))
'''

#直接读取文本文件进行解析
'''
html = etree.parse('./test.html',etree.HTMLParser())
result = etree.tostring(html)
print(result)
'''
#选取所有节点
'''
html = etree.parse('./test.html',etree.HTMLParser())
result = html.xpath('//*')
print(result)
'''
#获取父节点
'''
html = etree.parse('./test.html',etree.HTMLParser())
result = html.xpath('//a[@href="link4.html"]/parent::*/@class')
print(result)
'''
#获取子节点文本
'''
html = etree.parse('./test.html',etree.HTMLParser())
result = html.xpath('//li[@class="item-0"]//text()')
print(result)
'''
#获取节点属性
'''
html = etree.parse('./test.html',etree.HTMLParser())
result = html.xpath('//li/a/@href')
print(result)
'''
#containd()函数用法
test = '''
<li class="li li-first" name="item"><a href="link.html">first item</a></li>
'''
#当class有两个属性值li li-first的时候可以用containd()函数用法
'''
html = etree.HTML(test)
result = html.xpath('//li[contains(@class,"li")]/a/text()')
print(result)
'''
#根据多个属性确定一个节点
'''
html = etree.HTML(test)
result = html.xpath('//li[contains(@class,"li") and @name="item"]/a/text()')
print(result)
'''

#按序选择
#last()：代表最后一个节点  position()：代表所有节点
'''
html = etree.HTML(text)
result1 = html.xpath('//li[1]/a/text()')
print(result1)
result2 = html.xpath('//li[last()]/a/text()')
print(result2)
result3 = html.xpath('//li[position()<3]/a/text()')
print(result3)
result4 = html.xpath('//li[last()-2]/a/text()')
print(result4)
'''
#节点轴选择
html = etree.HTML(text)
#调用ancestor轴可以获取所有祖先节点
result1 = html.xpath('//li[1]/ancestor::*')
print(result1)
#增加限制条件只显示div祖先节点
result2 = html.xpath('//li[1]/ancestor::div')
print(result2)
#调用了attribute轴可以获取所有属性值
result3 = html.xpath('//li[1]/attribute::*')
print(result3)
#调用child轴获取所有直接子节点
result4 = html.xpath('//li[1]/child::a[@href="link1.html"]')
print(result4)
#调用descendant轴 获取所有子孙节点，限定条件获取span节点
result5 = html.xpath('//li[1]/descendant::span')
print(result5)
#调用following轴，获取当前节点后的所有节点,限定条件只获取第二个后续节点
result6 = html.xpath('//li[1]/following::*[2]')
print(result6)
#调用following-sibling轴获取当前节点之后的所有同级借点
result7 = html.xpath('//li[1]/following-sibling::*')
print(result7)



