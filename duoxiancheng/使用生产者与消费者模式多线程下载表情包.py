import os
import requests
from lxml import etree
from urllib import request
import re


def parse_page(url):
    headers={
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
    }
    response = requests.get(url,headers)
    text = response.text
    html = etree.HTML(text)
    imgs = html.xpath("//div[@class='col-sm-9']//img[@class!='gif']")
    for img in imgs:
        img_url = img.get('data-original')
        alt = img.get('alt')
        alt = re.sub(r'[\?\？\.，。-]','',alt)
        suffix = os.path.splitext(img_url)[1]
        filename = alt+suffix
        print(filename)
        request.urlretrieve(img_url,'images/'+filename)

def main():
    for x in range(1,101):
        url = 'http://www.doutula.com/article/list/?page=%d'%x
        parse_page(url)
        break

if __name__ == '__main__':
    main()
