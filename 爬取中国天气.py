import requests
from bs4 import BeautifulSoup

def parse_page(url):
    headers = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"
    }
    response = requests.get(url,headers)
    html = response.content.decode('utf-8')

    soup = BeautifulSoup(html,'html5lib')
    conMidtab = soup.find('div', attrs=('class','conMidtab'))
    tables = conMidtab.find_all('table')
    for table in tables:
        trs = table.find_all('tr')[2:]
        for index,tr in enumerate(trs):
            tds = tr.find_all('td')
            if index == 0:
                city_td = tds[1]
            else:
                city_td = tds[0]
            city = list(city_td.stripped_strings)[0]
            temp_td = tds[-2]
            min_temp = list(temp_td.stripped_strings)[0]

            print(city+":"+min_temp)


def main():
    url = "http://www.weather.com.cn/textFC/db.shtml"
    parse_page(url)


if __name__ == '__main__':
    main()