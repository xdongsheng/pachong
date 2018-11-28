#import urllib
from urllib import request
from urllib import parse

# urlopen函数是打开网页的
# resp=request.urlopen('http://www.baidu.com')
# print(resp.read())
# print(resp.getcode())


# urlretrieve函数是用来下载文件的
# request.urlretrieve('http://www.baidu.com','hehe.html')


# urlencode的用法  使用parse.urlencode(),解码使用parse_qs()方法
url = 'http://www.baidu.com/s'
name = {'wd':'刘德华'}
url_true = url+'?'+parse.urlencode(name)
a = parse.urlencode(name)
print(a)
b = parse.parse_qs(a)
print(b)
#resp = request.urlopen(url)
#request.urlretrieve(url_true,'liudehua.html')
#print(resp.read())

