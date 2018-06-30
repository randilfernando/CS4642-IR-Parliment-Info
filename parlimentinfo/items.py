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
    political_career = scrapy.Field()

class CurrentMember(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    party = scrapy.Field()
    dob = scrapy.Field()
    civil_status = scrapy.Field()
    religion = scrapy.Field()
    occupation = scrapy.Field()
    district = scrapy.Field()
    email = scrapy.Field()

class Article(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    date = scrapy.Field()
    content = scrapy.Field()