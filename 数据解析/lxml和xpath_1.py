from lxml import etree


#def parse_text():
    #htmlelements = etree.HTML(text=)
    #print(etree.tostring(htmlelements,encoding='utf-8').decode('utf-8'))

parser = etree.HTMLParser(encoding='utf-8')
def parse_file():
    htmlelements = etree.parse("baidu.html",parser=parser)
    print(etree.tostring(htmlelements, encoding='utf-8').decode('utf-8'))

if __name__ == '__main__':
    parse_file()