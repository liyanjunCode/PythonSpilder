# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanitemItem(scrapy.Item):
    # define the fields for your item here like:
    # 电影名称
    title = scrapy.Field()
    # 电影分数
    score = scrapy.Field()
    # 电影信息
    content = scrapy.Field()
    # 电影分数
    info = scrapy.Field()
