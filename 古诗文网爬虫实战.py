import  requests
import re

def parse_page(url):
    headers = {
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
    }
    response = requests.get(url,headers)
    text = response.text
    # print(response.text)
    titles = re.findall(r'<div\sclass="cont">.*?<b>(.*?)</b>',text,re.DOTALL)
    # re.DOTALL代表这个点匹配所有字符
    # print(titles)
    chaodais = re.findall(r'<p\sclass="source">.*?<a.*?>(.*?)</a>',text,re.DOTALL)
    zuozhes = re.findall(r'p\sclass="source">.*?<a.*?<a.*?>(.*?)</a>',text,re.DOTALL)
    contents = re.findall(r'<div class="contson".*?>(.*?)</div>',text,re.DOTALL)
    # print(chaodais)
    # print(zuozhes)
    # print(contents)
    peoms = []
    for content in contents:
        x = re.sub(r'<.*?>',"",content)
        peoms.append(x.strip())
    true_peoms =[ ]
    for value in zip(titles,chaodais,zuozhes,peoms):
        title,dynasty,author,neirong = value
        porm = {
            'title':title,
            'dynasty':dynasty,
            'author':author,
            'neirong':neirong
        }
        true_peoms.append(porm)
    print(true_peoms)
def main():
    url = 'https://www.gushiwen.org/default_1.aspx'
    parse_page(url)

if __name__ == '__main__':
    main()