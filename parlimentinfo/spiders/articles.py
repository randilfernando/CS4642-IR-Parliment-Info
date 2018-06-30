# -*- coding: utf-8 -*-
import scrapy
from scrapy.loader import ItemLoader
from parlimentinfo.items import Article


class NewsSpider(scrapy.Spider):
    name = 'articles'
    allowed_domains = ['parliament.lk']
    start_urls = ['http://parliament.lk/en/news-en?view=news&category=6']

    title_xpath = '//table[@class="newsheader"]//td//h2[1]/text()'
    date_xpath = '//table[@class="newsheader"]//tr[1]/td[3]/text()'
    content_xpath = '//div[@class="inner-div newsarea"]/div[1]/p[string-length(text()) > 3]/text()'

    def parse(self, response):
        for news in response.xpath('//td[@width="82%"]/a/@href').extract():
            yield scrapy.Request(response.urljoin(news), callback=self.parseArticle)

        next_page_url = response.xpath('//li[@class="pagination-next"]/a/@href').extract_first()
        if next_page_url is not None:
            yield scrapy.Request(response.urljoin(next_page_url))

    def parseArticle(self, response):
        title = response.xpath(self.title_xpath).extract()
        parts = response.xpath(self.date_xpath).extract()[0].split('-')
        if len(parts) >= 3:
            date = parts[2] + '-' + parts[1] + '-' + parts[0] + 'T00:00:00Z'
            content = response.xpath(self.content_xpath).extract()
            item = Article(title=title, date=date, content=content)
        yield item
