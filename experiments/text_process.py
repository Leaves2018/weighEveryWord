import collections
import re


def contains_chinese(s):
    """
    :param s: 待处理字符串
    :return: 该字符串中是否包含中文（布尔值）
    """
    return any('\u4e00' <= char <= '\u9fff' for char in s)


def strip_symbol(s):
    """
    :param s: 待处理字符串
    :return: 去除标点符号后的字符串
    """
    return re.sub('[’!"#$%&\'()*+,./:;<=>?@[\\]^_`{|}~]+', ' ', s)


def strip_number(s):
    """
    :param s: 待处理字符串
    :return: 去除数字后的字符串
    """

    return re.sub('[0-9]+', '', s)


def count_word(filename):
    """
    统计filename文本文件中非中文词的出现频率
    :param filename:需要统计词频的文本文件
    """
    # 返回值为dict，会自动进行计数
    word_counter = collections.Counter()

    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            # 过滤中文
            if contains_chinese(line):
                continue
            # 去除英文标点符号
            line = strip_symbol(line)
            # 去除数字
            line = strip_number(line)
            # 全部转为小写
            line = line.lower()
            # 更新字典项
            word_counter.update([word for word in re.split('\s+', line) if word != ''])

    return dict(word_counter)


def get_top(filename, top_k=10):
    """获取出现频率最高的top_k个词

    :param filename:需要统计词频的文本文件
    :param top_k:需要返回的出现频率最高的前topk个词，默认为10个
    """

    # 统计filename文本中的词频信息，保存到dict中
    word_dict = count_word(filename)
    # 对word_dict根据出现的词频进行降序排序
    top_k_words = sorted(word_dict.items(), key=lambda x: x[1], reverse=True)
    return top_k_words[:top_k]


def get_lowest(filename, lowest_k=10):
    """
    :param filename: 文件名
    :param lowest_k: 搜寻频率最低的词的个数
    :return: 频率最低的lowest_k个词及其出现频次
    """

    word_dict = count_word(filename)

    lowest_k_words = sorted(word_dict.items(), key=lambda x: x[1], reverse=False)
    return lowest_k_words[:lowest_k]


def foo(filename, top_k, lowest_k):
    top_words = get_top(filename, top_k)
    lowest_words = get_lowest(filename, lowest_k)
    print('------------------------------------------')
    print('Top {} words in {}'.format(top_k, filename))
    for k, v in top_words:
        print(k, v)
    print('------------------------------------------')
    print('Lowest {} words in {}'.format(lowest_k, filename))
    for k, v in lowest_words:
        print(k, v)
    print('------------------------------------------')
