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
        choice = bool(input("?????????????????????????????????\n"))
        if choice:
            new_words.append(word)
            print("??????")
        else:
            old_words.append(word)
            print("??????")
        size -= 1
        print("=====??????{}?????????=====".format(size))
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

if __name__ == '__main__':
    text = """Cats know their names???why it's harder for them than dogs
New research in Japan's cat cafes reveals our pet felines are more attuned to us than we thought.
By Carrie Arnold
Cats know many things: how to catch mice, what the sound of the can opener means, and even how to take over the internet.
But the one question cat expert Atsuko Saito always gets is whether cats recognize their own names, an ability that's well known in dogs.
In a new study in the journal Scientific Reports, the psychologist at Tokyo???s Sophia University showed that they do know their names???even when called by a stranger.
Cats are Saito???s favorite animal, and after studying primate cognition in graduate school, she set her research sights on the oft-misunderstood pets. (Is everything you think about cats wrong?)
???I love cats. They???re so cute and so selfish. When they want to be touched, they???ll come by me, but when they want to be left alone, they???ll just leave,??? she says, laughing.
Her past experiments have revealed cats can interpret human gestures to find hidden food, recognize their owner???s voice, and beg for food from a person who looks at them and calls their name???all of which suggested that felines know their names"""
    uf1, uk1 = first(text)
    print("unfamiliar_words")
    for i in uf1:
        print(i.get_name())
    print("unknown_words")
    for i in uk1:
        print(i.get_name())

if __name__ == '__main__':
    text = """Cats know their names???why it's harder for them than dogs
New research in Japan's cat cafes reveals our pet felines are more attuned to us than we thought.
By Carrie Arnold
Cats know many things: how to catch mice, what the sound of the can opener means, and even how to take over the internet.
But the one question cat expert Atsuko Saito always gets is whether cats recognize their own names, an ability that's well known in dogs.
In a new study in the journal Scientific Reports, the psychologist at Tokyo???s Sophia University showed that they do know their names???even when called by a stranger.
Cats are Saito???s favorite animal, and after studying primate cognition in graduate school, she set her research sights on the oft-misunderstood pets. (Is everything you think about cats wrong?)
???I love cats. They???re so cute and so selfish. When they want to be touched, they???ll come by me, but when they want to be left alone, they???ll just leave,??? she says, laughing.
Her past experiments have revealed cats can interpret human gestures to find hidden food, recognize their owner???s voice, and beg for food from a person who looks at them and calls their name???all of which suggested that felines know their names"""
    uf1, uk1 = first(text)
    print("unfamiliar_words")
    for i in uf1:
        print(i.get_name())
    print("unknown_words")
    for i in uk1:
        print(i.get_name())