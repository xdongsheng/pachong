import json

with open('json_str.json','r',encoding='utf-8')as fp:
    persons = json.load(fp)
    for person in persons:
        print(person)