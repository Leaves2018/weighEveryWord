import re
from vocabulary import Word
from process_raw_text import decorate_raw_text
from wordlist import generate_word_list
from update import *


def first(raw_text):
    familiar_words = []
    with open("./familiar/familiar_words.txt", mode='r+', encoding='UTF-8') as fw:
        for line in fw.readlines():
            familiar_words.append(line.strip().lower())

    vocabulary_words = []
    with open("./vocabulary/vocabulary_words.txt", mode='r+', encoding='UTF-8') as vw:
        for line in vw.readlines():
            text = line.lower().split('-')
            vocabulary_words.append(text[0])

    unfamiliar_words = []
    unknown_words = []
    temp = []
    for sentence in sentences(raw_text):
        words = re.split('[^a-zA-Z\']+', sentence)
        for word in words:
            if word is "" or word in temp:
                continue
            new_word = Word(name=word, context=re.sub(word, '*'+word+'*', sentence.strip()))
            if word.lower() in familiar_words:
                continue
            elif word.lower() in vocabulary_words:
                unfamiliar_words.append(new_word)
            else:
                unknown_words.append(new_word)
                temp.append(word)
    return unfamiliar_words, unknown_words


def second(unknown_words):
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

