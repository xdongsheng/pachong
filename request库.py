import requests


params = {"wd":"中国"}
header = {'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'}
response = requests.get("https://www.baidu.com/s",params=params,headers=header)
print(response.content.decode('utf-8'))
# print(type(response.content))
#print(response.content.decode('utf-8'))
# print(response.url)
# print(response.headers)
# print(response.encoding)
# print(response.status_code)

with open('zhongguo.html','w',encoding='utf-8') as pf:
    pf.write(response.content.decode('utf-8'))

# post请求在笔记里面，里面有data和header需要写的东西