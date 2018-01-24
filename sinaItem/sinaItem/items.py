# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SinaitemItem(scrapy.Item):
    # define the fields for your item here like:
    # 大标题
    parentName = scrapy.Field()
    # 大标题链接
    parentLink = scrapy.Field()

    # 小标题名
    subTitle = scrapy.Field()
    # 小标题链接
    subLink = scrapy.Field()

    # 小标题存放路径
    subPath = scrapy.Field()

    # 子类中的url
    sonUrl = scrapy.Field()

    # 文章标题和内容
    head = scrapy.Field()

    content = scrapy.Field()