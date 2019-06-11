# 生成单词表word_list、定制样式等
import codecs
import markdown
import os


def get_desktop_path():
    return os.path.join(os.path.expanduser("~"), 'Desktop')


# 输入：txt文件名（以MarkDown进行标记）
# 输出：html文件名
def generate_word_list(words, filename, show_context=False, show_english=False, show_chinese=False):
    # TODO 定制CSS样式
    css = open("./css/css.txt", "r+", encoding="UTF-8").read()

    process(words, filename, show_context, show_english, show_chinese)
    # 读取 markdown 文本
    input_file = codecs.open("./md/Vocabulary of " + filename + ".md", mode="r+", encoding="UTF-8")
    text = input_file.read()
    input_file.close()
    # 转为 html 文本
    html = markdown.markdown(text)
    # 保存为文件
    output_file = codecs.open(get_desktop_path() + "/Vocabulary of " + filename + '.html', mode="w+", encoding="utf-8")
    output_file.write(css + html)
    output_file.close()


def process(words, filename, show_context=False, show_english=False, show_chinese=False):
    md = open("./md/Vocabulary of " + filename + ".md", mode="w+", encoding="UTF-8")
    md.write("# Vocabulary\n\n")
    md.write("## " + filename + "\n\n")
    for i in range(len(words)):
        word = words[i]
        # md.write(str(i) + ". **" + word.get_name() + "**:" + "\n\n"
        #          + "    " + " > " + word.get_context() + "\n\n"
        #          + "    " + " - " + word.get_en_interpretation() + "\n\n"
        #          + "    " + " - " + word.get_ch_interpretation() + "\n\n")
        md.write(str(i) + ". **" + word.get_name() + "**:" + word.get_yb() + "\n\n"
                 # + "    " + word.get_str_context() + "\n\n"
                 + (("    " + "**例句**：" + word.get_context() + "\n\n") if show_context else "\n")
                 + (("    " + "**英解**：" + word.get_str_en_interpretation() + "\n\n") if show_english else "\n")
                 + (("    " + "**汉解**：" + word.get_str_ch_interpretation() + "\n\n") if show_chinese else "\n"))
    md.close()
