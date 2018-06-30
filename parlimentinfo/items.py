# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Member(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    party = scrapy.Field()
    dob = scrapy.Field()
    civil_status = scrapy.Field()
    religion = scrapy.Field()
    occupation = scrapy.Field()
    political_carrer = scrapy.Field()

class CurrentMember(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    party = scrapy.Field()
    dob = scrapy.Field()
    civil_status = scrapy.Field()
    religion = scrapy.Field()
    occupation = scrapy.Field()
    district = scrapy.Field()
    portfolio = scrapy.Field()
    mobile = scrapy.Field()
    home_address = scrapy.Field()
    email = scrapy.Field()
    office_phone = scrapy.Field()
    office_address = scrapy.Field()
    pass

class Article(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    date = scrapy.Field()
    content = scrapy.Field()