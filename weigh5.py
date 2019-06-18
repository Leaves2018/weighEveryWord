from pytrie import *

import re
from vocabulary2 import Word
from process_raw_text import decorate_raw_text
from wordlist import generate_word_list
from update import *


def first(raw_text):
    # 建立熟词字典树
    familiar_words = Trie()
    # 读取熟词本文件，将熟词本中单词插入熟词字典树
    with open("./familiar/familiar_words.txt", mode='r+', encoding='UTF-8') as fw:
        for line in fw.readlines():
            familiar_words.insert(line.strip().lower())

    # 建立生词字典树
    vocabulary_words_trie = Trie()
    # 建立生词字典
    vocabulary_words_dict = dict()
    # 读取生词本文件，将生词本中单词插入生词字典树，单词的其余属性以Word对象的形式添加到生词字典
    with open("./vocabulary/vocabulary_words.txt", "r+", encoding="UTF-8") as f:
        for sentence in f.readlines():
            # 如果不是字母开头，则视为非单词（如空行），跳过
            if not sentence[0].isalpha():
                continue
            # 以"----"作为分隔符，将字符串划分为列表
            text = sentence.split("----")
            # 以单词名、音标、语境初始化单词对象
            word = Word(name=text[0], yb=text[1], context=text[2])
            # 设置单词中文解释（以")""("及数字作为分隔符，获取列表，再作为参数）
            word.set_en_interpretation(re.split("[)(1-9]+", text[3])[1:])
            word.set_ch_interpretation(re.split("[)(1-9]+", text[4])[1:])
            # 将生词名称插入生词字典树
            vocabulary_words_trie.insert(word.name)
            # 将生词对象加入字典
            vocabulary_words_dict[word.name] = word

    # 建立"语境"字典
    context = dict()
    # 建立"未知词"集合
    unknown_words = []
    # 建立待返回"不熟悉词"列表
    uf = []
    # 建立待返回"未知词"列表
    uk = []
    # 以"句"为单位，遍历输入文本
    for sentence in sentences(raw_text):
        # 将该句以所有非字母字符作为分隔符进行分割，生成列表，并转为集合类型以去重
        temp_words = re.split('[^a-zA-Z]+', sentence)
        words = []
        for word in temp_words:
            if word not in words:
                words.append(word)
        # 遍历集合中所有单词
        for word in words:
            # 如果为空，则跳过
            if word is "":
                continue
            # 在该句中，在单词word出现位置前后各加一个"*"以作标记；将该句添加到语境字典中，以单词word为键
            context[word] = re.sub(word, '*' + word + '*', sentence.strip())
            # 模糊过滤规则
            i = 0
            # 如果单词长度小于6，则忽视最后一位进行过滤
            if len(word) < 6:
                i = 1
            # 如果单词长度大于等于6，小于8，则忽视最后两位进行过滤
            elif len(word) < 8:
                i = 2
            # 依此类推
            elif len(word) < 10:
                i = 3
            elif len(word) < 14:
                i = 4
            elif len(word) < 20:
                i = 5
            # 过滤熟词：如果熟词字典树中存在该单词忽视尾部i个字符的前缀，则跳过
            if familiar_words.starts_with(word.lower()[:-i]):
                continue
            # 过滤生词：如果生词字典树中存在该单词忽视尾部i个字符的前缀，则：
            elif vocabulary_words_trie.starts_with(word.lower()[:-i]):
                # 从生词字典中取出该单词
                temp_word = vocabulary_words_dict.get(vocabulary_words_trie.get_start(word.lower()[:-i])[0])
                # 更新该单词语境为本文语境
                temp_word.context = context.get(word)
                # 将该单词视为"不熟悉词"，加入到uf列表中
                uf.append(temp_word)
            # 添加未知词：既不在熟词本又不在生词本中的单词，视为未知词，需要用户判断
            else:
                unknown_words.append(word)

    # 从未知词列表中依次取出str类型单词，并取出用户输入文本中该单词所在的句子，初始化单词对象并添加给uk列表
    for w in unknown_words:
        uk.append(Word(name=w, context=context.get(w)))
    # 用户输入文本已过滤到"不熟悉词"及"未知词"，返回，交由下一步处理（进入"生熟词判断"）
    return uf, uk


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


# 生成器：输入str类型的文本，每次调用时返回该文本中的一句话
def sentences(text):
    # 将换行符置换为英文句号"."
    text = re.sub("\n", ".", text)
    # 以英文结束一句话的字符".""!""?"作为分隔符，分割为列表；列表的每一项是一个句子
    s = re.split("[.!?]+", text)
    # 遍历句子列表，每次调用该函数时返回一句
    for sentence in s:
        yield sentence


if __name__ == '__main__':
    text = """Cats know their names—why it's harder for them than dogs
New research in Japan's cat cafes reveals our pet felines are more attuned to us than we thought.
By Carrie Arnold
Cats know many things: how to catch mice, what the sound of the can opener means, and even how to take over the internet.
But the one question cat expert Atsuko Saito always gets is whether cats recognize their own names, an ability that's well known in dogs.
In a new study in the journal Scientific Reports, the psychologist at Tokyo’s Sophia University showed that they do know their names—even when called by a stranger.
Cats are Saito’s favorite animal, and after studying primate cognition in graduate school, she set her research sights on the oft-misunderstood pets. (Is everything you think about cats wrong?)
“I love cats. They’re so cute and so selfish. When they want to be touched, they’ll come by me, but when they want to be left alone, they’ll just leave,” she says, laughing.
Her past experiments have revealed cats can interpret human gestures to find hidden food, recognize their owner’s voice, and beg for food from a person who looks at them and calls their name—all of which suggested that felines know their names"""
    uf1, uk1 = first(text)
    print("-----unfamiliar_words-----")
    for i in uf1:
        print(i.get_name())

    print()

    print("-----unknown_words-----")
    for i in uk1:
        print(i.get_name())
