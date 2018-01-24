# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class YgitemItem(scrapy.Item):
    # define the fields for your item here like:
    # 标题
    title = scrapy.Field()
    # 编号
    number = scrapy.Field()
    # 内容
    content = scrapy.Field()
    # 网址
    url = scrapy.Field()
