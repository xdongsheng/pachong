from lxml import etree
import requests

BASE_URL = "https://hr.tencent.com/"
HEADERS = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36',
    'Referer': 'https://hr.tencent.com/position.php?lid=&tid=&keywords=python&start=10'

}


def get_detail_url(url):
    #注意这一定要写headers等于什么
    response = requests.get(url, headers=HEADERS)
    text = response.text
    html = etree.HTML(text)

    data_all = html.xpath("//td[@class='l square']/a/@href")
    detail_url = map(lambda url1:BASE_URL+url1,data_all)
    return detail_url

def parse_detail_url(url):
    info = {}
    yaoqiu=[]
    zhize=[]
    response = requests.get(url,headers=HEADERS)
    text = response.content.decode('utf-8')
    html = etree.HTML(text)

    position = html.xpath("//td[@class='l2 bold size16']/text()")[0]
    info['position'] = position

    address = html.xpath("//tr[@class='c bottomline']/td/text()")
    info['address'] = address[0]
    info['type'] = address[1]
    info['amount'] = address[2]

    renwu = html.xpath("//tr[@class='c']/td[@class='l2']/ul[@class='squareli']/li/text()")
    zhize.append(renwu[0])
    for i in range(1,len(renwu)):
        if renwu[i].startswith('1'):
            for a in range(i,len(renwu)):
                yaoqiu.append(renwu[a])
            break
        else:
            zhize.append(renwu[i])
    info['zhize'] = zhize
    info['yaoqiu'] = yaoqiu
    return info

def spider():
    url = 'position.php?lid=&tid=&keywords=python&start={}#a'
    infos = []
    for x in range(0, 4):
        x = x * 10
        url_true = url.format(x)
        detail_urls = get_detail_url(BASE_URL + url_true)
        for detail_url in detail_urls:
            info = parse_detail_url(detail_url)
            infos.append(info)
    print(infos)

if __name__ == '__main__':
    spider()
