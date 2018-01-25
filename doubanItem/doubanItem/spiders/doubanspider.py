# -*- coding: utf-8 -*-
import scrapy
from doubanItem.items import DoubanitemItem

class DoubanspiderSpider(scrapy.Spider):
    name = 'doubanspider'
    allowed_domains = ['movie.douban.com']
    url ='https://movie.douban.com/top250?start='
    offset = 0
    end = '&filter='
    start_urls = [url + str(offset) + end]

    def parse(self, response):

        item = DoubanitemItem()
        # 所有电影的全部内容
        all = response.xpath('//div[@class="info"]')

        for number in all:
            # 电影名称
            title = number.xpath('./div[@class="hd"]/a/span[1]/text()').extract()
            # 电影分数
            score = number.xpath('./div[@class="bd"]/div[@class="star"]/span[@class="rating_num"]/text()').extract()
            # 电影信息
            content = number.xpath('./div[@class="bd"]/p/text()').extract()
            # 电影分数
            info = number.xpath('./div[@class="bd"]/p[@class="quote"]/span/text()').extract()
            # 存入item
            item['title'] = title[0]
            item['score'] = score[0]
            item['content'] = ";".join(content)
            item['info'] = "".join(info)

            yield item
        if self.offset <= 225:
            self.offset += 25
            yield scrapy.Request(self.url +str(self.offset) + self.end, callback=self.parse)