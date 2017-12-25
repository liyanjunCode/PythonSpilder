#!/user/bin/env python
# _*_ coding:utf-8 _*_
import threading
import json
import requests
from lxml import etree
from Queue import Queue
import time


class ThreadCrawl(threading.Thread):
    """
        抓取网页内容
    """
    def __init__(self, treadName, pageQueue):
        super(ThreadCrawl, self).__init__()
        self.treadName = treadName
        self.pageQueue = pageQueue
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3278.0 Safari/537.36"}
    def run(self):
        while True:
            if self.pageQueue.empty():
                break
            try:
                pages = self.pageQueue.get(False)
                print "开始" + self.treadName
                url = "https://www.qiushibaike.com/8hr/page/" + str(pages)
                response = requests.get(url, headers=self.headers)
                html = etree.HTML(response.text)
                items = html.xpath('//div[contains(@id,"qiushi_tag")]')
                dataQueue.put(items)
            except:
                print "结束" + self.treadName

class Thread_Parser(threading.Thread):
    """
        存储网页内容
    """
    def __init__(self,threadID, dataQueue, fileName):
        super(Thread_Parser, self).__init__()
        self.threadID = threadID
        self.dataQueue = dataQueue
        self.f = fileName
    def run(self):
        global PARSE_EXIT
        while not PARSE_EXIT:
            try:
                print "开始" + self.threadID
                content = self.dataQueue.get(False)
                self.parseing(content)
            except:
                print "结束" + self.threadID

    def parseing(self, html):
        for item in html:
            imgUrl = item.xpath('.//img/@src')[0]
            title = item.xpath('.//h2')[0].text
            content = item.xpath('.//div[@class="content"]/span')[0].text.strip()
            vote = item.xpath('.//i')[0].text
            comments = item.xpath('.//i')[1].text
            result = {
                'imgUrl': imgUrl,
                'title': title,
                'content': content,
                'vote': vote,
                'comments': comments,
            }
            self.f.write(json.dumps(result, ensure_ascii=False).encode('utf-8') + "\n")

dataQueue = Queue()
PARSE_EXIT = False
def main(start, end):
    """
        主进程
    :param start: 开始页数
    :param end: 结束页数
    :return:
    """
    fileName = open("qiushi.json", "a")
    pageQueue = Queue()
    for page in range(start, end + 1):
        pageQueue.put(page)
    crawlList = ["爬虫线程-1", "爬虫线程-2", "爬虫线程-3"]
    threadCrawl = []

    # 爬虫线程
    for treadName in crawlList:
        thread = ThreadCrawl(treadName, pageQueue)
        thread.start()
        threadCrawl.append(thread)


     # 初始化解析线程parserList
    parserthreads = []
    parserList = ["解析线程-1", "解析线程-2", "解析线程-3"]
    # 分别启动parserList
    for threadID in parserList:
        thread = Thread_Parser(threadID, dataQueue, fileName)
        thread.start()
        parserthreads.append(thread)
    while not pageQueue.empty():
        pass

    for t in threadCrawl:
        t.join()

    while not dataQueue.empty():
        pass
    global PARSE_EXIT
    PARSE_EXIT = True
    for t in parserthreads:
        t.join()
    fileName.close()

if __name__ == "__main__":
    inputs = ""
    while True:
        if inputs == 'quit':
            break
        start = int(raw_input("开始页数"))
        end = int(raw_input("结束页数"))
        main(start, end)
        print "完成"
        inputs = raw_input("推出输入quit")
