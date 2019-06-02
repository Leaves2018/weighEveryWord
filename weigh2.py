import re
from vocabulary import Word
from process_raw_text import decorate_raw_text
from wordlist import generate_word_list
from update import *


def first(raw_text):
    familiar_words = []
    with open("familiar/familiar_words.txt", mode='r+', encoding='UTF-8') as fw:
        for line in fw.readlines():
            familiar_words.append(line.strip().lower())

    vocabulary_words = dict()
    with open("vocabulary/vocabulary_words.txt", mode='r+', encoding='UTF-8') as vw:
        for line in vw.readlines():
            text = line.split('_')
            vocabulary_words[text[0]] = Word(*text)

    new_words = []
    unknown_words = []

    for sentence in sentences(raw_text):
        words = re.split('[^a-zA-Z]+', sentence)
        for word in words:
            if word is "":
                continue
            # 记录单词所在文章名、文章中所在句位置、句中所在单词位置
            if sentence.strip().index(word) == 0:
                word = word.lower()
            new_word = Word(name=word, context=re.sub(word, '*'+word+'*', sentence.strip()))
            if word in familiar_words:
                continue
            elif word in vocabulary_words.keys():
                new_words.append(new_word)
            else:
                unknown_words.append(new_word)
    return new_words, unknown_words


def second(new_words, unknown_words):
    old_words = []
    new_words = []
    size = len(unknown_words)
    for word in unknown_words:
        print('--------------------')
        print(word.get_name())
        print(word.get_context())
        print(word.get_eng_interpretation())
        print(word.get_ch_interpretation())
        print('--------------------')
        choice = bool(input("熟词敲回车，生词按空格\n"))
        if choice:
            new_words.append(word)
            print("生词")
        else:
            old_words.append(word)
            print("熟词")
        size -= 1
        print("=====剩余{}个单词=====".format(size))
    update_familiar_words(old_words)
    update_vocabulary_words(new_words)
    return new_words


def third(new_words, filename):
    decorate_raw_text(new_words, filename)
    generate_word_list(new_words, filename)


def sentences(text):
    s = re.split("[.!?]+", text)
    for sentence in s:
        yield sentence

