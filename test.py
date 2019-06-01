import codecs
import markdown

css = '''
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<style type="text/css">
<!-- 此处省略掉markdown的css样式，因为太长了 -->
</style>
'''

# 读取 markdown 文本
input_file = codecs.open("Vocabulary of The Dusty Drawer.md", mode="r", encoding="utf-8")
text = input_file.read()

# 转为 html 文本
html = markdown.markdown(text)

# 保存为文件
output_file = codecs.open("Vocabulary of The Dusty Drawer.html", mode="w", encoding="utf-8")
output_file.write(css + html)
