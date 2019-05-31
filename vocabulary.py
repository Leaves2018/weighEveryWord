# 单词类
class Word:
    # 四个基本属性：名称、语境、英解、中解、出现频次，默认值均为空
    def __init__(self, name=None, context=None, eng_interpretation=None, ch_interpretation=None, count=0):
        self.name = name
        self.context = context
        self.eng_interpretation = eng_interpretation
        self.ch_interpretation = ch_interpretation
        self.count = count

    # 设置语境（该词所在句或段）
    def set_context(self):
        pass

    # 获取英解（可考虑将爬虫代码放置于此）
    def get_eng_interpretation(self):
        pass

    # 获取中解（可考虑将爬虫代码放置于此）
    def get_ch_interpretation(self):
        pass

