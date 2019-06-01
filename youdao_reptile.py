import requests
from bs4 import BeautifulSoup

def func(s):
    a = s.split("'")
    return a[1]

def get_page(url):
    a = requests.get(url)
    try:
        a.encoding = a.apparent_encoding
        b = a.text
        return b
    except:
        return ''

def deal_page_ch(url):
    page = get_page(url)
    bs = BeautifulSoup(page, 'html.parser')
    div = bs.find('div', class_="trans-container").children
    # try:
    for i in div:
        s = str(type(i))
        if func(s) == 'bs4.element.Tag':
            t = i.find('li')
            if t!=None:
                return t.contents[0]
            else:
                return None

def deal_page_en(url):
    page = get_page(url)
    bs = BeautifulSoup(page, 'html.parser')
    span = bs.find('span', class_='def')
    if span != None:
        return span.contents[0]
    else:
        return None

def ch_mean(word):
    return deal_page_ch('http://dict.youdao.com/w/eng/' + word + '/#keyfrom=dict2.index')

def en_mean(word):
    return deal_page_en('http://dict.youdao.com/w/eng/' + word + '/#keyfrom=dict2.index')
