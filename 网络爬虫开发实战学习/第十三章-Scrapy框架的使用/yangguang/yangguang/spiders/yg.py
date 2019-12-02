# -*- coding: utf-8 -*-
import scrapy


class YgSpider(scrapy.Spider):
    name = 'yg'
    allowed_domains = ['sun0769.com']
    start_urls = ['http://wz.sun0769.com/html/top/report.shtml']

    def parse(self, response):
        #分组
        pass

        

