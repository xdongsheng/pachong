import json

# 将python对象转换为json字符串

persons = [
    {
        'username':'李四',
        'age':'23',
        'country':'china'

    },
    {
        'username':'张三',
        'age':'2',
        'country':'china'
    }

]

json_str = json.dumps(persons)
print(type(json_str))
print(json_str)
# with open('person.json','w')as fp:
#     fp.write(json_str)
# 写入到文件中不用这么麻烦了，可以直接用json中的dunp，而不是dumps
with open('json_str.json','w',encoding='utf-8')as fp:
    json.dump(persons,fp,ensure_ascii=False)