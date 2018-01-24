# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ygItem.items import YgitemItem

class YgspiderSpider(CrawlSpider):
    name = 'ygspider'
    allowed_domains = ['wz.sun0769.com']
    start_urls = ['http://wz.sun0769.com/index.php/question/questionType?type=0&page=0']

    rules = [
        Rule(LinkExtractor(allow=r'type=0&page=\d+')),
        Rule(LinkExtractor(allow=r'html/question/\d+/\d+.shtml'), callback='parse_item', follow=True),
    ]

    def parse_item(self, response):

        item = YgitemItem()
        # 标题
        item['title'] = response.xpath('//div[@class="pagecenter p3"]//strong[@class="tgray14"]/text()').extract()[0]
        # 编号
        item['number'] = item['title'].split(' ')[-1].split(":")[-1]
        # 内容
        main = response.xpath('//div[@class="contentext"]/text()').extract()
        if len(main) == 0:
            contents = response.xpath('//div[@class="c1 text14_2"]/text()').extract()
            item['content'] = "".join(contents).strip()
        else:
            item['content'] = "".join(main).strip()

        # 网址
        item['url'] = response.url

        return item
