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
        return self.name

    def set_name(self):
        self.get_context(True)
        self.get_ch_interpretation(True)
        self.get_en_interpretation(True)
        return self.name

    def get_yb(self, flag=False):
        if flag or not self.yb:
            self.yb = yb_mean(self.name)
        return self.yb

    def set_yb(self, yb):
        self.yb = yb

    # 获取语境（如果没有提供语境，将自动从有道词典获取例句）
    def get_context(self, flag=False):
        if flag or not self.context:
            text = example_mean(self.name)
            self.context = re.sub(self.name, " *" + self.name + "* ", text)
        return self.context

    # 设置语境（该词所在句或段）
    def set_context(self, context):
        self.context = context

    # 获取英解（如果还没有查询单词的英解，则先查询存储再返回）
    def get_en_interpretation(self, flag=False):
        s = ""
        if flag or not self.en_interpretation:
            text = en_mean(self.name)
            for i in range(len(text)):
                s += "~" + text[i] + "\n"
            self.en_interpretation = text
        return s

    def get_list_en_interpretation(self, flag=False):
        if flag or not self.en_interpretation:
            self.en_interpretation = en_mean(self.name)
        return self.en_interpretation

    def set_en_interpretation(self, eng_interpretation):
        self.en_interpretation = eng_interpretation

    # 获取中解（如果还没有查询单词的中解，则先查询存储再返回）
    def get_ch_interpretation(self, flag=False):
        s = ""
        if flag or not self.ch_interpretation:
            text = ch_mean(self.name)
            for i in range(len(text)):
                s += "~" + text[i] + "\n"
            self.ch_interpretation = text
        return s

    def set_ch_interpretation(self, ch_interpretation):
        self.ch_interpretation = ch_interpretation

    def to_string(self):
        return "{}_{}_{}_{}"\
            .format(self.name, self.context, self.get_en_interpretation(), self.get_ch_interpretation())

    def to_tuple(self):
        return self.name, self.context, self.en_interpretation, self.ch_interpretation, str(self.count)
