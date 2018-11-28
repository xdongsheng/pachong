from lxml import etree

# 1.获取所有的tr标签
# 2. 获取第2个tr标签
# 3.获取所有class等于even的标签
# 4.获取所有a标签的href属性
# 5.获取所有的职位信息（纯文本）


# xpath函数返回的是一个列表



parser = etree.HTMLParser(encoding='utf-8')
html = etree.parse('liudehua.html',parser)

# print(etree.tostring(html,encoding='utf-8').decode('utf-8'))

# 1_   //tr
# xpath返回的是列表
# trs = html.xpath("//tr")
# for tr in trs:
#     print(tr)

# 2 获取第二个tr标签
# tr2 = html.xpath("//tr[2]")
# print(tr2)

# 3.获取所有class等于even的标签
# class_even = html.xpath("//tr[@class='even']")
# print(class_even)
#
# for i in class_even:
#     print(etree.tostring(class_even,encoding='utf-8').decode('utf-8'))


# 4.获取所有a标签的href属性
# a_list = html.xpath("//a/@href")
# for i in a_list:
#     print(a_list)

# 5.获取所有的职位信息（纯文本）
trs = html.xpath("//tr[position()>1]")
# 过滤掉第一个标签
for tr in trs:
     # print(tr.xpath(".//a/@href")[0])
     # 加上一个.是为了获取当前tr下的a，否则获取的是整个网页的a标签
     title = tr.xpath(".//a//text()")[0]
     print(title)
     break