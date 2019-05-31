from reptile import *
from vocabulary import Word

with open("inputtest.txt") as t:
    words = t.read().lower().split()

d = {}
for word in words:
    d[word] = Word(count=words.count(word))

if __name__ == '__main__':
    for word in words:
        d[word] = Word(ch_interpretation=youdao(word))

with open('outputtest.txt', 'a+') as wl:
    for key in d:
        wl.write(key+' '+d[key].ch_interpretation)