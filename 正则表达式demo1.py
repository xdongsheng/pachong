import re

#   这个主要是匹配单个字符


# 1.匹配某个字符串
#text = '+hello'
# ret = re.match('he',text)
# 只去匹配前面的字符，如果前面的字符不匹配的话，后面的也不会去匹配
# print(ret.group())

# 2. . ：匹配任意的字符,只要是个字符就可以匹配出来,但是不能匹配换行符
# ret = re.match('.',text)
# print(ret.group())

#  \d:匹配的是数字（0-9）
# \D:匹配的是任意的非数字
# \s:匹配空白字符（\n,\t,\r,空格）
# \w 匹配的是a-z和A-Z，下划线和数字
# \W 与小写的w匹配项相反

# []组合的方式：只要满足中括号中的字符，就可以匹配
# text = "0438-2832385ddddd"
# ret = re.match('[\d\-]+',text)
# +号的作用是匹配多个字符串
# print(ret.group())


# 中括号的形式代替\d
text = '14234hgfh_'
ret = re.match('[a-zA-Z0-9_]+',text)
print(ret.group())

