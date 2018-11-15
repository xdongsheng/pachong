import csv

def read_csv_demo1():
    with open('classroom1.csv', 'r', encoding='utf-8')as fp:
        reader = csv.reader(fp)
        titles = next(reader)
        print(titles)
        for x in reader:
            print(x)

def read_csv_demo2():
    with open('classroom1.csv', 'r', encoding='utf-8')as fp:
        reader = csv.DictReader(fp)

        for x in reader:
            print(x)
            print(x['username'])

if __name__ == '__main__':
    read_csv_demo2()