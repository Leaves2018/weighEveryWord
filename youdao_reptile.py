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


# 获取网页上的单词的英式音标
def deal_page_yb(url):
    page = get_page(url)
    bs = BeautifulSoup(page, 'html.parser')
    try:
        span = bs.find('span', class_='phonetic')
        if span is not None:
         return span.contents[0]
    except:
        return ""


# 获取网页上的单词的中文解释
def deal_page_ch(url):
    page = get_page(url)
    bs = BeautifulSoup(page, 'html.parser')
    try:
        div = bs.find('div', class_="trans-container")
        if div is not None:
            for i in div:
                s = str(type(i))
                if func(s) == 'bs4.element.Tag':
                    t = i.find('li')
                    if t is not None:
                        return t.contents[0]
                    else:
                        return None
    except:
            return ""


def deal_page_example(url):
    page = get_page(url)
    bs = BeautifulSoup(page, 'html.parser')
    try:
        div = bs.find('div', id='authority')
        if div is not None:
            li = div.find('li')
            p = li.find('p')
            return p.get_text()
    except:
        return ""


# 获取网页上的单词的英文解释
def deal_page_en(url):
    en_list = []
    page = get_page(url)
    bs = BeautifulSoup(page, 'html.parser')
    try:
        span = bs.find_all('span', class_='def')
        if span is not None:
            for i in span:
                s = str(type(i))
                if func(s) == 'bs4.element.Tag':
                    en_list.append(i.contents[0])
        return en_list
    except:
        return ""


# 获取单词的中文意思
def ch_mean(word):
    if word:
        return deal_page_ch('http://dict.youdao.com/w/eng/' + word + '/#keyfrom=dict2.index')


# 获取单词的英文意思
def en_mean(word):
    if word:
        return deal_page_en('http://dict.youdao.com/w/eng/' + word + '/#keyfrom=dict2.index')


# 获取例句
def example_mean(word):
    return str(deal_page_example('http://dict.youdao.com/w/eng/' + word + '/#keyfrom=dict2.index')).strip()


# 获取音标
def yb_mean(word):
    if word:
        return deal_page_yb('http://dict.youdao.com/w/eng/' + word + '/#keyfrom=dict2.index')

