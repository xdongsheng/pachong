from urllib import request

# 这是没有使用代理的
url = 'http://www.httpbin.org/ip'
# resp =request.urlopen(url)
# result = resp.read()
# print(result)

# 这是使用代理的
# 使用ProxyHandler传入代理构建一个handler
handler = request.ProxyHandler({"http":"106.12.3.84:80"})
# 使用上面创建的handler构建opener
opener = request.build_opener(handler)
# 使用opener去发送一个请求
resp = opener.open(url)

print(resp.read())
