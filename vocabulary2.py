from youdao_reptile import *
import re


# 单词类
class Word:
    # 四个基本属性：名称、语境、英解、中解、出现频次，默认值均为空字符串或0（如果设置为None，在转str时可能会报错）
    def __init__(self, name="", yb="", context="", en_interpretation=[], ch_interpretation=[], count=0):
        self.name = name
        self.yb = yb
        self.context = context
        self.en_interpretation = en_interpretation
        self.ch_interpretation = ch_interpretation
        self.count = count

    def get_name(self):
        return self.name if not isinstance(self.name, type(None)) else "None"

    def set_name(self, name):
        self.name = name
        self.get_context(True)
        self.get_yb(True)
        self.get_ch_interpretation(True)
        self.get_en_interpretation(True)

    # 获取音标
    def get_yb(self, flag=False):
        if flag or not self.yb:
            self.yb = yb_mean(self.name)
        return self.yb if not isinstance(self.yb, type(None)) else "None"

    def set_yb(self, yb):
        self.yb = yb

    # 获取语境（如果没有提供语境，将自动从有道词典获取例句）
    # def get_context(self, flag=False):
    #     if flag or not self.context:
    #         text = example_mean(self.name)
    #         temp = []
    #         if isinstance(text, str):
    #             temp.append(text)
    #             text = temp
    #         for i in range(len(text)):
    #             text[i] = re.sub(self.name, " *" + self.name + "* ", text[i])
    #         self.context = text
    #     return self.context

    # def get_str_context(self, flag=False):
    #     text = ""
    #     for sentence in self.get_context(flag):
    #         text += " > " + sentence + "\n"
    #     return text

    def get_context(self, flag=False):
        if flag or not self.context:
            text = example_mean(self.name)
            self.context = re.sub(self.name, " *" + self.name + "* ", text)
        return self.context if not isinstance(self.context, type(None)) else "None"

    # 设置语境（该词所在句或段）
    def set_context(self, context):
        context = re.sub(self.name, " *" + self.name + "* ", context)
        self.context = context

    # 获取英解（如果还没有查询单词的英解，则先查询存储再返回）
    def get_en_interpretation(self, flag=False):
        if flag or not self.en_interpretation:
            self.en_interpretation = en_mean(self.name)
        return self.en_interpretation if not isinstance(self.en_interpretation, type(None)) else "None"

    def get_str_en_interpretation(self, flag=False):
        text = ""
        count = 0
        for sentence in self.get_en_interpretation(flag):
            if sentence == "":
                continue
            count += 1
            text += "(" + str(count) + ")" + sentence
        return text if not isinstance(text, type(None)) else "None"

    def set_en_interpretation(self, eng_interpretation=[]):
        self.en_interpretation = eng_interpretation

    # 获取中解（如果还没有查询单词的中解，则先查询存储再返回）
    def get_ch_interpretation(self, flag=False):
        if flag or not self.ch_interpretation:
            self.ch_interpretation = ch_mean(self.name)
        return self.ch_interpretation if not isinstance(self.ch_interpretation, type(None)) else "None"

    def get_str_ch_interpretation(self, flag=False):
        text = ""
        count = 0
        for sentence in self.get_ch_interpretation(flag):
            if sentence == "":
                continue
            count += 1
            text += "(" + str(count) + ")" + sentence
        return text if not isinstance(text, type(None)) else "None"

    def set_ch_interpretation(self, ch_interpretation=[]):
        self.ch_interpretation = ch_interpretation

    def get_count(self):
        return self.count

    def set_count(self, count=0):
        self.count = count

    def count_plus(self, n=1):
        self.count += n

    def to_string(self):
        return "{}----{}----{}----{}----{}----{}"\
            .format(self.get_name(),
                    self.get_yb(),
                    self.get_context(),
                    self.get_str_en_interpretation(),
                    self.get_str_ch_interpretation(),
                    str(self.get_count()))
