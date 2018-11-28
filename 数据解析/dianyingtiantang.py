from lxml import etree
import requests

BASE_URL = 'https://www.dytt8.net'
headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
    }




def get_detail_url(url):
    response = requests.get(url, headers)
    # 这里如果使用content自己的解码方式，很容易出现无法解码的地方，但是我们只是想要链接，所以不需要解码，就用自己的编码解码方式就行了
    # text = response.content.decode('GBK')
    # 如果真的想解析这个界面，然后可以先把这个text encode（‘utf-8’）,在解码成utf-8或者其他的编码解码方式
    # print(response.encoding)
    text = response.text
    html = etree.HTML(text)
    data_all = html.xpath("//table[@class='tbspan']//a/@href")

    for i in data_all:
        print(BASE_URL + i)

    detail_url = map(lambda url1:BASE_URL+url1,data_all)
    print(detail_url)
    return detail_url

def parse_detail_page(url):
    movie = {}
    response = requests.get(url,headers)
    text = response.content.decode('gbk')
    html = etree.HTML(text)
    data_head = html.xpath("//div[@class='title_all']//font[@color='#07519a']//text()")[0]
    #print(data_head)
    content = html.xpath("//div[@class='co_content8']")[0]
    images = content.xpath(".//img/@src")
    cover = images[0]
    #screenshot = images[1]
    movie['title'] = data_head
    movie['cover'] = cover
    #movie['screenshot'] = screenshot
    data_all = content.xpath(".//text()")

    for index,i in enumerate(data_all):
        # print(index)
        # print(i)
        # print("="*30)

        if i.startswith('◎译　　名'):
            i = parse_info_replace(i,'◎译　　名')
            movie['translate_name'] = i
        elif i.startswith('◎豆瓣评分'):
            i = parse_info_replace(i,'◎豆瓣评分')
            movie['remark'] = i

        elif i.startswith('◎片　　长'):
            i = parse_info_replace(i,'◎片　　长')
            movie['time'] = i


        # 主演这里是重点中的重点**********************
        elif i.startswith('◎主　　演'):
            info = parse_info_replace(i,'◎主　　演')
            actors = []
            actors.append(info)
            for x in range(index+1,len(data_all)):
                actor = data_all[x].strip()

                if actor.startswith('◎'):
                    break
                actors.append(actor)
            movie['actors']=actors
            #print(movie['actors'])
    download_href = html.xpath("//td[@bgcolor='#fdfddf']//a/@*")[0]
    #print('download_href:',download_href)
    movie['download_url'] = download_href
    return movie



def parse_info_replace(info,rule):
    # 这个.strip是剥去的意思，在这里面是去掉空格的
    return  info.replace(rule,'').strip()

def spider():
    base_url = 'https://www.dytt8.net/html/gndy/dyzz/list_23_{}.html'
    movies =[]
    for x in range(1,2):
        url = base_url.format(x)
        # 通过控制台打印来找错的方法：
        print("="*30)
        print(x)
        print("="*30)
        movie_urls =  get_detail_url(url)
        for movie_url in movie_urls:
            movie = parse_detail_page(movie_url)
            movies.append(movie)
    print(movies)
if __name__ == '__main__':
    spider()