from urllib import request
from http.cookiejar import CookieJar
from urllib import parse


# 1登录
# 1.1 创建一个cookiejar的对象
cookiejar = CookieJar()
# 1.2 使用cookiejar创建一个HTTPcookieProcess对象
handler = request.HTTPCookieProcessor(cookiejar)
# 1.3 使用上一步的handler创建一个opener
opener = request.build_opener(handler)





# 2 使用opener发送登录请求（账号和密码）
header = { 'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'}
data={
    'username':'4244722',
    'password':'xds806lyb'}
logain_url = 'https://i.qq.com'


req = request.Request(logain_url,data=parse.urlencode(data).encode('utf-8'),headers=header)
opener.open(req)




# 3访问个人主页
url = 'https://user.qzone.qq.com/4244722'
reqq=request.Request(url,headers=header)
resp = opener.open(reqq)
with open('newqq.html','w',encoding='utf-8') as fp:
    fp.write(resp.read().decode('utf-8'))