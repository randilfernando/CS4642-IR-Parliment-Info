# -*- coding: utf-8 -*-
import scrapy
from scrapy.loader import ItemLoader
from parlimentinfo.items import CurrentMember
import json


class CurrentMembersSpider(scrapy.Spider):
    name = 'current-members'
    allowed_domains = ['parliament.lk']
    start_urls = [
        'http://parliament.lk/members-of-parliament/directory-of-members/index2.php?option=com_members&task=all&tmpl=component&letter=A&wordfilter=&search_district=']

    def parse(self, response):
        jsonresponse = json.loads(response.body_as_unicode())
        for r in jsonresponse:
            yield scrapy.Request("http://parliament.lk/en/members-of-parliament/directory-of-members/viewMember/%s" % r[
                'mem_intranet_id'], callback=self.parse_member)
        for i in range(65, 91):
            yield scrapy.Request(
                'http://parliament.lk/members-of-parliament/directory-of-members/index2.php?option=com_members&task=all&tmpl=component&letter=%s&wordfilter=&search_district=' % chr(
                    i))

    def parse_member(self, response):
        l = ItemLoader(item=CurrentMember(), response=response)
        l.add_xpath('name', '//div[@class="components-wrapper"]/h2/text()')
        l.add_xpath('party',
                    '//div[@class="top-mp-detail-1"]//div[@class="right-details"]//table[@class="mem_profile"]//tr/td//div[contains(.//text(),"Party")]/following-sibling::a/text()')
        l.add_xpath('dob',
                    '//div[@class="top-mp-detail-2"]//div[@class="left-wrap"]//table[@class="mem_profile"]//tr/td[contains(.//span, "Birth")]/text()')
        l.add_xpath('civil_status',
                    '//div[@class="top-mp-detail-2"]//div[@class="left-wrap"]//table[@class="mem_profile"]//tr/td[contains(.//span, "Civil")]/text()')
        l.add_xpath('religion',
                    '//div[@class="top-mp-detail-2"]//div[@class="left-wrap"]//table[@class="mem_profile"]//tr/td[contains(.//span, "Religion")]/text()')
        l.add_xpath('occupation',
                    '//div[@class="top-mp-detail-2"]//div[@class="left-wrap"]//table[@class="mem_profile"]//tr/td[contains(.//span, "Occupation")]/text()')
        l.add_xpath('email', '//a[@class="link7"]/text()')
        l.add_xpath('district',
                    '//div[@class="top-mp-detail-1"]//div[@class="right-details"]//table[@class="mem_profile"]//tr/td[contains(.//div, "District")]/text()')
        yield l.load_item()