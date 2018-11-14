#   匹配多个字符

import re

# *:可以匹配0或者任意多个字符
# text = 'aaa1231412aaa'
# ret = re.match('\d*',text)
# print(ret.group())

# +;匹配一个或者多个字符，最少要有一个
# ret = re.match('\d+',text)
# print(ret.group())

# ?;匹配1个或者0个（要么没有，要么就只有一个）
# text = 'abcd'
# ret = re.match('\w?',text)
# print(ret.group())

# {m}:匹配m个字符
# text = 'abcd'
# ret = re.match('\w{2}',text)
# print(ret.group())

# {m,n}:匹配m到n个字符
text = 'abc'
ret = re.match('\w{2,4}',text)
print(ret.group())
