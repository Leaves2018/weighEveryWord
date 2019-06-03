# 生成单词表word_list、定制样式等
import codecs
import markdown


# 输入：txt文件名（以MarkDown进行标记）
# 输出：html文件名
def generate_word_list(words, filename):
    # TODO 定制CSS样式
    css = '''
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
    <style type="text/css">
    <!-- 此处省略掉markdown的css样式，因为太长了 -->
    </style>
    '''
    process(words, filename)
    # 读取 markdown 文本
    input_file = codecs.open("/md/Vocabulary of " + filename + ".md", mode="r+", encoding="UTF-8")
    text = input_file.read()
    input_file.close()
    # 转为 html 文本
    html = markdown.markdown(text)
    # 保存为文件
    output_file = codecs.open("/output/Vocabulary of " + filename + '.html', mode="w+", encoding="utf-8")
    output_file.write(css + html)
    output_file.close()


def process(words, filename):
    md = open("/md/Vocabulary of " + filename + ".md", mode="w+", encoding="UTF-8")
    md.write("# Vocabulary\n\n")
    md.write("## " + filename + "\n\n")
    for i in range(len(words)):
        word = words[i]
        md.write(str(i) + ". **" + word.get_name() + "**:" + "\n\n"
                 + "    " + "> " + word.get_context() + "\n\n"
                 + "    " + "- " + word.get_eng_interpretation() + "\n\n"
                 + "    " + "- " + word.get_ch_interpretation() + "\n\n")
    md.close()
