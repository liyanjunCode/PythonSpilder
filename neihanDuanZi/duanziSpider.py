#!\user\bin\env python
#*_*coding:utf-8*_*

import urllib
import urllib2
import re
class Spilder:
    """
        内涵段子爬虫主程序
    """
    def __init__(self):
        self.page = 1
        self.status = True
    def loadPage(self):
        """
            发送请求加载页面
        """
        if self.page == 1:
            pages = ""
        else:
            pages = "_" + str(self.page)
        url = "http://www.neihan8.com/article/index" + pages + ".html"
        headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3278.0 Safari/537.36"}
        request = urllib2.Request(url, headers=headers)
        response = urllib2.urlopen(request).read()
        # 调用处理每页的函数
        self.dealPage(response)

    def dealPage(self, response):
        """
            处理每页段子
        :param response: 传入的每页数据
        :return:
        """
        # 正则匹配每段段子
        pattern = re.compile(r'<div\s class="desc">(.*?)</div>', re.S)
        txts = pattern.findall(response)
        # 每段段子传入写文件函数
        for content in txts:
            print "正在保存,请稍后"
            contents = "{" + content + "}" + ","
            self.Write(contents)

    def Write(self, html):
        """
            写入文件
        """
        with open("duanzi.txt", "a") as f:
            f.write(html)

    def control(self):
        """
            控制程序是否执行
        """
        while self.status:
            self.loadPage()
            manage = raw_input("继续请按回车键，退出请输入quit")
            if manage == "quit":
                self.status = False
            self.page += 1


if __name__ == "__main__":
    Spilder = Spilder()
    Spilder.control()
    print "欢迎再次使用"