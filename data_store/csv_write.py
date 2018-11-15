import csv

def write_csv_demo1():
    headers = ['username', 'age', 'height']
    values = [
        {
            '张三', '18', '180'
        },
        {'张s', '17', '180'},
        {'张5', '186', '1800'}
    ]
    # newline如果不指定为空那么是一个换行符\n
    with open('classroom.csv', 'w', encoding='utf-8', newline='')as fp:
        writer = csv.writer(fp)
        writer.writerow(headers)
        writer.writerows(values)

# 使用字典的方式把数据写入进去，这时候就需要使用DictWriter了，示例代码如下：
def write_csv_demo2():
    headers = ['username', 'age', 'height']
    values = [
        {
            'username':'张三','age': '18','height': '180'
        },
        {'username':'张s','age': '17', 'height':'180'},
        {'username':'张5', 'age':'186', 'height':'1800'}
    ]
    with open('classroom1.csv','w',encoding='utf-8',newline='')as fp:
        writer = csv.DictWriter(fp,headers)
        # 需要调用一下这个writeheader才能把表头写入进去
        writer.writeheader()
        writer.writerows(values)

if __name__ == '__main__':
    write_csv_demo2()