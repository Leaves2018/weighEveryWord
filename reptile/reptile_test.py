import requests
from bs4 import BeautifulSoup

a = []


def func(s):
    a = s.split("'")
    return a[1]


# 转换编码格式，获取网页
def get_page(url):
    a = requests.get(url)
    try:
        a.encoding = a.apparent_encoding
        b = a.text
        return b
    except:
        return ""

# 获取网页上的单词的英文解释
def deal_page_en(url):
    page = get_page(url)
    bs = BeautifulSoup(page, 'html.parser')
    try:
        span = bs.find_all('span', class_='def')
        if span is not None:
            for i in span:
                s = str(type(i))
                if func(s) == 'bs4.element.Tag':
                    a.append(i.contents[0])
        return a
    except:
        return "sss"

word = "find"
print(deal_page_en('http://dict.youdao.com/w/eng/' + word + '/#keyfrom=dict2.index'))


