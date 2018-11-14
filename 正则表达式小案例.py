# 1.验证手机号码，
import re

# text = '17695705055'
# ret = re.match('1[34578]\d{9}',text)
# print(ret.group())

# 2.验证邮箱
# text = 'xdszyyx@163.com '
# ret = re.match('\w+@\w+\.[a-z]+',text)
# print(ret.group())

# 3.验证URL
# text = 'http://baidu.com'
# ret = re.match('(http|https|ftp)://[^\s]+',text)
# print(ret.group())

# 4. 验证身份证
# text = '220721199503170610'
# ret = re.match('\d{17}[\dxX]',text)
# print(ret.group())

# ^(脱字号):表示以...开始,如果放在中括号当中代表取反
# text = 'hello'
# ret = re.search('^l',text)
# print(ret.group())

# $:表示以...结尾
# text = 'xdszyys@163.com'
# ret = re.match('\w+@163.com$',text)
# print(ret.group())

# \:匹配多个字符串或者表达式
# text = 'http'
# ret = re.match('(http|https|ftp)$',text)
# print(ret.group())

# 贪婪与非贪婪模式
# text = '0123456'
# ret = re.match('\d+?',text)
# print(ret.group())
# text = '<h1>标题</h1>'
# ret = re.match('<.+?>',text)
# print(ret.group())

# 匹配0-100之间的数字
text = '77'
ret = re.match('([1-9]\d$)|100',text)
print(ret.group())

