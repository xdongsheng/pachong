import os
import requests
from lxml import etree
from urllib import request
import re
from queue import Queue
import threading

# 生产者（获取表情url）获取到每一个表情的url
# 消费者（下载表情）

class Producer(threading.Thread):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
    }
    # *args代表任意未知参数，**kwargs代表任意无关参数
    def __init__(self,page_queue,img_queue,*args,**kwargs):
        super(Producer,self).__init__(*args,**kwargs)
        self.page_queue = page_queue
        self.img_queue = img_queue
    def run(self):
        while True:
            if self.page_queue.empty():
                break
            url = self.page_queue.get()
            self.parse_page(url)


    def parse_page(self,url):
        response = requests.get(url,self.headers)
        text = response.text
        html = etree.HTML(text)
        imgs = html.xpath("//div[@class='col-sm-9']//img[@class!='gif']")
        for img in imgs:
            img_url = img.get('data-original')
            alt = img.get('alt')
            alt = re.sub(r'[\?\？\.\*，。-]','',alt)
            suffix = os.path.splitext(img_url)[1]
            filename = alt+suffix
            # print(filename)
            # request.urlretrieve(img_url,'images/'+filename)
            self.img_queue.put((img_url,filename))

# 消费者
class Consumer(threading.Thread):
    # *args代表任意未知参数，**kwargs代表任意无关参数
    def __init__(self, page_queue, img_queue, *args, **kwargs):
        super(Consumer, self).__init__(*args, **kwargs)
        self.page_queue = page_queue
        self.img_queue = img_queue
    def run(self):
        while True:
            if self.img_queue.empty() and self.page_queue.empty():
                break
            img_url,filename = self.img_queue.get()
            request.urlretrieve(img_url,'images/'+filename)
            print(filename+'下载完成')


def main():
    page_queue = Queue(100)
    img_queue = Queue(1000)


    for x in range(1,101):
        url = 'http://www.doutula.com/article/list/?page=%d'%x
        page_queue.put(url)

    for x in range(5):
        t =Producer(page_queue,img_queue)
        t.start()
    for x in range(5):
        t = Consumer(page_queue,img_queue)
        t.start()

if __name__ == '__main__':
    main()
