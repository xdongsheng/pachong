import re

# text = 'aple price is $299'
# ret = re.search('\$\d+',text)
# print(ret.group())

# 正则表达式中原生字符串
# text = '\c'
# ret = re.search(r'\\c',text)
# print(ret.group())

# match 只在最前面找，serch 在全局中都找


# 分组
text = "apple's price is $99, orange's price is $10"
# ret = re.search('.*(\$\d+).*(\$\d+)',text)
# print(ret.group())
# print(ret.group(1))
# print(ret.group(2))
# print(ret.group(1,2))
# # 所有的子分组都拿出来
# print(ret.groups())

# find_all找出所有满足条件的，返回的是一个列表
# ret = re.findall('\$\d+',text)
# print(ret)

# sub用来替换字符串的
# ret = re.sub('\$\d+','$0',text,count=1)
# print(ret)

# 小案例剔除掉标签
# ret = re.sub('<.+?>',"",text)

# 使用正则表达式来分割字符串，split函数：
# text = "hello&world ni hao"
# # ret = re.split(' |&',text)
# ret = re.split('[^a-zA-Z]',text)
# print(ret)

# compile 对于一些经常要用到的正则表达式，可以使用compile进行编译，后期再使用的时候可以直接拿过来用，执行效率会更快。而且compile还可以指定flag=re.VERBOSE,在写正则表达式的时候可以做好注释。
text = "the number is 20.50"
# r = re.compile('\d+\.?\d*')
r = re.compile(r"""
\d+  #小数点前面的数字
\.?  #小数点本身
\d*  #小数点后面的数字
""",re.VERBOSE)
ret = re.search(r,text)
print(ret.group())
#测试github


