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
        result = response.xpath('//div[@id="newscontent"]/div[@class="l"]/ul/li/span[@class="s1"]/text()')
        result_dict = {}
        for label in result:
            keys = label.extract()[1:-1]
            if keys in result_dict:
                result_dict[keys] +=1
            else:
                result_dict[keys] = 1
        self.log(result_dict)
