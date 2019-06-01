# 分离四六级考纲单词表中的四级单词和六级单词
# 以★ 打头的是六级单词
# TODO：由于对PDF内容复制容易出错，考虑用pdfminer3自动解析PDF

with open('/Users/leaves/PycharmProjects/weighEveryWord/familiar/CET.txt', 'r') as cet:
    cet4 = open('CET4.txt', 'w+')
    cet6 = open('CET6.txt', 'w+')
    for line in cet.readlines():
        if line.startswith('★'):
            cet6.write(line[2:])
        else:
            cet4.write(line)
