from urllib import request

url = 'http://avtt2018v108.com/yazhouqingse/130086.html'

headers = {
'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
}
req = request.Request(url,headers=headers)
resp = request.urlopen(url)
print(resp.read())