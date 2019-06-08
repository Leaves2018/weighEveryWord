import requests
from bs4 import BeautifulSoup


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


# 获取网页上的单词的中文解释
def deal_page_ch(url):
    ch_list = []
    page = get_page(url)
    bs = BeautifulSoup(page, 'html.parser')
    try:
        div = bs.find('div', class_="trans-container")
        if div is not None:
            for i in div:
                s = str(type(i))
                if func(s) == 'bs4.element.Tag':
                    t = i.find_all('li')
                    for i in t:
                        if i is not None:
                            ch_list.append(i.contents[0])
                        else:
                            return None
        return ch_list
    except:
            return ""

word = "word"
print(deal_page_ch('http://dict.youdao.com/w/eng/' + word + '/#keyfrom=dict2.index'))

