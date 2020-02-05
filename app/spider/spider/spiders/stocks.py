# -*- coding: utf-8 -*-
import scrapy
from scrapy import Selector
from ..items import StocksItem


class StocksSpider(scrapy.Spider):
    name = 'stocks'
    allowed_domains = ['histock.tw']
    start_urls = ['https://histock.tw/stock/rank.aspx']

    def parse(self, response):
        item = StocksItem()
        for tr in response.css('.gvTB tr'):
            item["code"] = tr.css("td:first-child *::text").get()
            item['name'] = tr.css("td:nth-child(2) a *::text").get()
            yield item

        next_page = None
        for a in response.css('div.school-index div.pager a'):
            t = a.css("*::text").get()
            if -1 != t.find("下一頁"):
                next_page = self.start_urls[0] + a.css("::attr(href)").get()

        if next_page is not None:
            new = scrapy.http.response.urljoin(response.url, next_page)
            yield scrapy.Request(new, callback=self.parse, dont_filter=True)
        else:
            raise scrapy.exceptions.CloseSpider("no next page, close stocks spider")
