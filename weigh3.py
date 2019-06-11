from pytrie import *

import re
from vocabulary2 import Word
from process_raw_text import decorate_raw_text
from wordlist import generate_word_list
from update import *


def first(raw_text):
    familiar_words = Trie()
    with open("./familiar/familiar_words.txt", mode='r+', encoding='UTF-8') as fw:
        for line in fw.readlines():
            familiar_words.insert(line.strip().lower())

    vocabulary_words = Trie()
    with open("./vocabulary/vocabulary_words.txt", mode='r+', encoding='UTF-8') as vw:
        for line in vw.readlines():
            text = line.lower().split('----')
            vocabulary_words.insert(text[0])

    unfamiliar_words = []
    unknown_words = []
    for sentence in sentences(raw_text):
        words = set(re.split('[^a-zA-Z]+', sentence))
        for word in words:
            if word is "":
                continue
            new_word = Word(name=word, context=re.sub(word, '*' + word + '*', sentence.strip()))
            i = 0
            if len(word) < 4:
                i = 1
            elif len(word) < 8:
                i = 2
            elif len(word) < 10:
                i = 3
            elif len(word) < 14:
                i = 4
            elif len(word) < 20:
                i = 5
            if familiar_words.starts_with(word.lower()[:-i]):
                continue
            elif vocabulary_words.starts_with(word.lower()[:-i]) and not vocabulary_words.search(word.lower()):
                vocabulary_words.insert(word.lower())
                unfamiliar_words.append(new_word)
            else:
                unknown_words.append(new_word)
    return unfamiliar_words, unknown_words


def second(unknown_words):
    old_words = []
    new_words = []
    size = len(unknown_words)
    for word in unknown_words:
        print('--------------------')
        print(word.get_name())
        print(word.get_context())
        print(word.get_en_interpretation())
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


def third(new_words, filename, show_context=False, show_english=False, show_chinese=False):
    decorate_raw_text(new_words, filename)
    generate_word_list(new_words, filename, show_context, show_english, show_chinese)


def sentences(text):
    text = re.sub("\n", ".", text)
    s = re.split("[.!?]+", text)
    for sentence in s:
        yield sentence