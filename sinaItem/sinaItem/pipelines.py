# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
class SinaitemPipeline(object):

    def process_item(self, item, spider):
        sonUrl = item['sonUrl']
        # 文件名为子链接url中间部分，并将 / 替换为 _，保存为 .txt格式
        filename = sonUrl[7:-6].replace('/', '_')
        filename += ".txt"
        file = open(item['subPath'] + '/' + filename,'w')
        file.write(item['content'])
        file.close()
        return item
