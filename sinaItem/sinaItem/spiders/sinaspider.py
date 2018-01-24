# -*- coding: utf-8 -*-
import scrapy
from sinaItem.items import SinaitemItem
import os
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
class SinaspiderSpider(scrapy.Spider):
    name = 'sinaspider'
    allowed_domains = ['sina.com.cn']
    start_urls = ['http://news.sina.com.cn/guide/']

    def parse(self, response):

        items = []
        # 大标题
        parentName = response.xpath('////div[@id="tab01"]/div/h3/a/text()').extract()
        # 大标题链接
        parentLink = response.xpath('//div[@id="tab01"]/div/h3/a/@href').extract()

        # 小标题名
        subTitle = response.xpath('//div[@id="tab01"]/div/ul/li/a/text()').extract()
        # 小标题链接
        subLink = response.xpath('//div[@id="tab01"]/div/ul/li/a/@href').extract()

        # 循环每个大标题得到大标题的文件存储目录
        for i in range(0,len(parentName)):

            # 本地存储文件名
            parentPath = './Data/' + parentName[i]

            if(not os.path.exists(parentPath)):
                os.makedirs(parentPath)
            for j in range(0,len(subLink)):
                item = SinaitemItem()

                # 存储大类标题和链接
                item['parentName'] = parentName[i]
                item['parentLink'] = parentLink[i]

                if_belong = subLink[j].startswith(item['parentLink'])
                if(if_belong):
                    subPath = parentPath +'/' + subTitle[j]
                    if (not os.path.exists(subPath)):
                        os.makedirs(subPath)

                    # 存储子类标题和链接
                    item['subTitle'] = subTitle[j]
                    item['subLink'] = subLink[j]
                    item['subPath'] = subPath
                    items.append(item)
        for item in items:
            yield scrapy.Request(item['subLink'], meta = {'meta1':item},callback = self.parse_item)

    def parse_item(self, response):

        items = []
        meta1 = response.meta['meta1']
        # 提取子类中所有链接
        allLink = response.xpath('//a/@href').extract()

        for k in allLink:
            # 检查每个链接是否以大类url开头、以.shtml结尾，如果是返回True
            if_belong = k.endswith('.shtml') and k.startswith(meta1['parentLink'])
            if if_belong:
                item = SinaitemItem()
                # 存储子类内容链接
                item['sonUrl'] = k
                item['parentName'] = meta1['parentName']
                item['parentLink'] = meta1['parentLink']
                item['subTitle'] = meta1['subTitle']
                item['subLink'] = meta1['subLink']
                item['subPath'] = meta1['subPath']
                items.append(item)
        for item in items:
            yield scrapy.Request(item['sonUrl'], meta = {'meta2':item},callback=self.parse_content)

    def parse_content(self, response):

        item = response.meta['meta2']
        content = ''
        head = response.xpath('//h1/text()').extract()
        content_list = response.xpath('//div[@id="artibody"]/p/text()').extract()
        for content_one in content_list:
            content += content_one
        # 存储内容和标题
        item['head'] = head
        item['content'] = content
        yield item