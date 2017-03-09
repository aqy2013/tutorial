# -*- coding: utf-8 -*-
import scrapy
from scrapy.shell import inspect_response
from ..items import TutorialItem


class MydomainSpider(scrapy.Spider):
    name = "dmoz"
    # allowed_domains = ["dmoz.org"]
    start_urls = [
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
        # "http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"
    ]

    # def parse(self, response):
    #     itemList = response.css('#site-list-content .site-item .site-title::text').extract()
    #     data = []
    #     for item in itemList:
    #         temp = TutorialItem()
    #         temp['title'] = item
    #         data.append(temp)
    #     # inspect_response(response,self)
    #     return data

    def parse(self, response):
        itemList = response.css('#site-list-content .site-item .title-and-desc > exit').extract()
        print itemList
        for item in itemList:
            yield scrapy.Request(item, callback=self.parseInfo)

    def parseInfo(self, response):
        inspect_response(response, self)
        title = response.css('body > h1::text').extract()
