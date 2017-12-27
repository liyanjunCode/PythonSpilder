# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TencentspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # 职位名称
    positionName = scrapy.Field()
    # 职位链接
    positionHref = scrapy.Field()
    # 职位类别
    positionInfo = scrapy.Field()
    #招聘人数
    pepleNum = scrapy.Field()
#     工作地点
    location = scrapy.Field()
    # 发布日期
    publicTime = scrapy.Field()

