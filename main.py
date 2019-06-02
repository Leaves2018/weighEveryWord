from queue import Queue
from format_conversion.txt2html.txt2html import process_raw_text
from wordlist import generate_word_list
from update import update_vocabulary_words, update_familiar_words
from vocabulary import Word

# 打开待处理文本，划分单词
with open(r'Cats know their names.txt', encoding='UTF-8') as raw_text:
    words = raw_text.read().lower().split()


# 去重（考虑是否有更高效率的实现方式）
temp = []
for word in words:
    if word not in temp:
        temp.append(word)
words = temp


# 打开熟词本，按行取单词
# TODO 将熟词本存储数据由字符串变为对象；读取时用'-'作为分隔符，生成对象
with open("familiar_words.txt", 'r', encoding='UTF-8') as fw:
    # familiar_words = [line.strip('\n').split('-') for line in fw.readlines()]
    familiar_words = dict()
    for line in fw.readlines():
        text = line.strip('\n').split('_')
        familiar_words[text[0]] = Word(*text)


# 打开生词本，按行取单词
# TODO 将生词本存储数据由字符串变为对象；读取时用'-'作为分隔符，生成对象
with open("vocabulary_words.txt", 'r', encoding='UTF-8') as vw:
    # vocabulary_words = [line.strip('\n').split('-') for line in vw.readlines()]
    vocabulary_words = dict()
    for line in vw.readlines():
        text = line.strip('\n').split('_')
        vocabulary_words[text[0]] = Word(*text)


# 待处理队列
to_be_processed = Queue()
# 未知词队列（既不在生词本中，又不是熟词本中，需要用户决断）
unknown = Queue()

# 遍历待处理文本所有单词，进行熟词、生词、未知词分类
for word in words:
    # 如果是熟词，过滤
    if word in familiar_words.keys():
        continue
    # 如果是生词，加入待处理队列
    elif word in vocabulary_words.keys():
        to_be_processed.put(Word(name=word))
    # 否则认为是未知词，加入未知词队列
    else:
        unknown.put(Word(name=word))

old_words = []
# 处理未知词队列：由用户决断属于熟词还是生词
while not unknown.empty():
    word = unknown.get()
    # 打印该单词名称、语境、英解、中解
    print("-----------------------------")
    print(word.name)
    print(word.get_eng_interpretation())
    print(word.get_ch_interpretation())
    print("-----------------------------")
    choice = bool(input("生词还是熟词？(输入任意字符表示生词，直接敲回车表示熟词)"))
    if choice:
        to_be_processed.put(word)
        print("生词")
    else:
        old_words.append(word)
        print("熟词")
    print("=============================")


# 未知词中被认为是生词的单词列表
new_words = []

# 处理待处理单词队列：
# （1）在原文中标记该单词（HTML标签）
# （2）生成单词列表
while not to_be_processed.empty():
    word = to_be_processed.get()
    new_words.append(word)
    # 处理原始文本：为生词添加HTML标签以突出显示
    process_raw_text()
    # 生成单词表：单词名称、语境、英解、中解
    generate_word_list()

# 更新生词本：将新增生词加入生词本
update_vocabulary_words(new_words)
update_familiar_words(old_words)
