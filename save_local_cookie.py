from urllib import request
from http.cookiejar import MozillaCookieJar
from urllib import parse

cookiejar = MozillaCookieJar("cookie.txt")
cookiejar.load(ignore_discard=True)
handler = request.HTTPCookieProcessor(cookiejar)
opener = request.build_opener(handler)

resp = opener.open('http://www.baidu.com')
# 设置ignore参数就是即使是过期的cookie信息也保存下来
#cookiejar.save(ignore_discard=True)
for cookie in cookiejar:
    print(cookie)