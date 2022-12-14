import markdown
import codecs
from util import *
from vocabulary2 import *
import os


def get_desktop_path():
    return os.path.join(os.path.expanduser("~"), 'Desktop')


def decorate_raw_text(words, filename):
    # TODO 定制CSS样式
    css = open("./css/css.txt", "r+", encoding="UTF-8").read()
    process(words, filename)
    # 读取 markdown 文本
    input_file = codecs.open("./md/" + filename + ".md", mode="r+", encoding="UTF-8")
    text = input_file.read()
    input_file.close()
    # 转为 html 文本
    html = markdown.markdown(text)
    # 保存为文件
    output_file = codecs.open(get_desktop_path() + "/" + filename + '.html', mode="w+", encoding="utf-8")
    output_file.write(css + html)
    output_file.close()


def process(words, filename):
    f = open("./input/" + filename + ".txt", mode="r+", encoding="UTF-8")
    text = f.read()
    f.close()
    for word in words:
        if isinstance(word, Word):
            text = re.sub(word.get_name(), ' **' + word.get_name() + '** ', text)

    md = open("./md/" + filename + ".md", mode="w+", encoding="UTF-8")
    md.write("# " + filename + "\n\n")
    md.write(text)
    md.close()
