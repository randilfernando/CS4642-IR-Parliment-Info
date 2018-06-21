# -*- coding: utf-8 -*-
import scrapy
from scrapy.loader import ItemLoader
from parlimentinfo.items import Member
import json


class MembersSpider(scrapy.Spider):
    name = 'members'
    allowed_domains = ['parliament.lk']
    start_urls = [
        'http://parliament.lk/members-of-parliament/index2.php?option=com_members&task=past&tmpl=component&letter=A&wordfilter=&search_district=&search_legislature=']

    def parse(self, response):
        jsonresponse = json.loads(response.body_as_unicode())
        for r in jsonresponse:
            yield scrapy.Request(
                "http://parliament.lk/en/members-of-parliament/directory-of-past-members/viewMember/%s" % r[
                    'mem_intranet_id'], callback=self.parse_member)
        for i in range(65, 91):
            yield scrapy.Request(
                'http://parliament.lk/members-of-parliament/index2.php?option=com_members&task=past&tmpl=component&letter=%s&wordfilter=&search_district=&search_legislature=' % chr(
                    i))

    def parse_member(self, response):
        l = ItemLoader(item=Member(), response=response)
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
        l.add_xpath('political_carrer', '//pre/text()')
        yield l.load_item()
