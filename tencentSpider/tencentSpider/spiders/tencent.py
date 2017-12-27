# -*- coding: utf-8 -*-
import scrapy
from tencentSpider.items import TencentspiderItem

class TencentSpider(scrapy.Spider):
    name = 'tencent'
    allowed_domains = ['hr.tencent.com']
    url = "http://hr.tencent.com/position.php?&start="
    offset = 0
    start_urls = [url + str(offset)]

    def parse(self, response):

        for each in response.xpath("//tr[@class='even'] | //tr[@class='odd']"):
            item = TencentspiderItem()
            # 职位名称
            positionName = each.xpath("td[1]/a/text()").extract()[0]
            # 职位链接
            positionHref = each.xpath("td[1]/a/@href").extract()[0]
            positionInfo = each.xpath('./td[2]/text()').extract()[0]
            # 招聘人数
            pepleNum = each.xpath("td[3]/text()").extract()[0]
            #     工作地点
            location = each.xpath("td[4]/text()").extract()[0]
            # 发布日期
            publicTime = each.xpath("td[5]/text()").extract()[0]
            # 存储数据
            item['positionName'] = positionName
            item['positionHref'] = positionHref
            item['positionInfo'] = positionInfo
            item['pepleNum'] = pepleNum
            item['location'] = location
            item['publicTime'] = publicTime
            #     每页去玩取下一页
            if self.offset < 2710:
                self.offset += 10
            # 发给调度器
            yield scrapy.Request(self.url + str(self.offset), callback=self.parse)
            yield item


