#coding:utf-8
import scrapy

class ScrapySpider(scrapy.spiders.Spider):
    name = "xs84"

    allowed_domains = [
        "http://www.xs84.me/"
    ]

    start_urls = [
        "http://www.xs84.me/"
    ]
    def parse(self,response):
        result = response.xpath('//div[@id="newscontent"]/div[@class="l"]/ul/li/span[@class="s1"]')
        for li in result:
            print("********************")
            print(li.extract())
            print("********************")
        print(result)

