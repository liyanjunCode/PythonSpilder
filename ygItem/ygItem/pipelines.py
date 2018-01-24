# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import codecs
import json

class YgitemPipeline(object):
    def __init__(self):
        self.file = codecs.open("sun.json","w",encoding="utf-8")
    def process_item(self, item, spider):
        content = json.dumps(dict(item),ensure_ascii=False)
        self.file.write(content + "\n")

    def spider_closed(self, spider):
        self.file.close()
