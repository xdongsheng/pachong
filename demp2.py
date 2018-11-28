from urllib import parse

# urlparse和urlsplit的用法，都是用来分割拿到的一个url
# urlparse和urlsplit的用法基本上是一样的，就是urlsplit里面没有params参数，用起来的时候他们两个用哪个都行

url = 'http://avtt2018v108.com/yazhouqingse/130086.html'

result = parse.urlparse(url)
print(result)
print('scheme:',result.scheme)
print('netloc:',result.netloc)
print('path:',result.path)
print('params:',result.params)
print('fragment:',result.fragment)