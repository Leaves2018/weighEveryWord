import markdown
import codecs
from util import *


def decorate_raw_text(words, filename):
    # TODO 定制CSS样式
    css = '''
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
    <style type="text/css">
    <!-- 此处省略掉markdown的css样式，因为太长了 -->
    </style>
    '''
    process(words, filename)
    # 读取 markdown 文本
    input_file = codecs.open("C:\\Users\\10513\\PycharmProjects\\weighEveryWord\\md\\" + filename + ".md", mode="r+", encoding="UTF-8")
    text = input_file.read()
    input_file.close()
    # 转为 html 文本
    html = markdown.markdown(text)
    # 保存为文件
    output_file = codecs.open("C:\\Users\\10513\\PycharmProjects\\weighEveryWord\\output\\" + filename + '.html', mode="w+", encoding="utf-8")
    output_file.write(css + html)
    output_file.close()


def process(words, filename):
    f = open("C:\\Users\\10513\\PycharmProjects\\weighEveryWord\\input\\" + filename + ".txt", mode="r+", encoding="UTF-8")
    text = f.read()
    f.close()
    for word in words:
        text = re.sub(word.get_name(), ' **' + word.get_name() + '** ', text)

    md = open("C:\\Users\\10513\\PycharmProjects\\weighEveryWord\\md\\" + filename + ".md", mode="w+", encoding="UTF-8")
    md.write("# " + filename + "\n\n")
    md.write(text)
    md.close()
