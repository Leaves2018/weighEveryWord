# 生成单词表word_list、定制样式等
import codecs
import markdown
import os


def get_desktop_path():
    return os.path.join(os.path.expanduser("~"), 'Desktop')


# 输入：txt文件名（以MarkDown进行标记）
# 输出：html文件名
def generate_word_list(words, filename):
    # TODO 定制CSS样式
    css1 = '''
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
    <style type="text/css">
    <!-- 此处省略掉markdown的css样式，因为太长了 -->
    body{
    margin: 0 auto;
    font-family: "ubuntu", "Tahoma", "Microsoft YaHei", arial,sans-serif;
    color: #444444;
    line-height: 1;
    padding: 30px;
    }
    
    img {
        max-width: 100%;
    }
    @media screen and (min-width: 1000px) {
        body {
            width: 842px;
            margin: 10px auto;
        }
    
    
    }
    h1, h2, h3, h4 {
        color: #111111;
        font-weight: 400;
        margin-top: 1em;
    }
    
    h1, h2, h3, h4, h5 {
        font-family: Georgia, Palatino, serif;
    }
    h1, h2, h3, h4, h5, dl{
        margin-bottom: 16px;
        padding: 0;
    }
    
    p {
        margin-top: 8px;
        margin-bottom: 3px;
    }
    h1 {
        font-size: 48px;
        line-height: 54px;
    }
    h2 {
        font-size: 36px;
        line-height: 42px;
    }
    h1, h2 {
        border-bottom: 1px solid #EFEAEA;
        padding-bottom: 10px;
    }
    h3 {
        font-size: 24px;
        line-height: 30px;
    }
    h4 {
        font-size: 21px;
        line-height: 26px;
    }
    h5 {
        font-size: 18px;
        line-height: 23px;
    }
    a {
        color: #0099ff;
        margin: 0 2px;
        padding: 0;
        vertical-align: baseline;
        text-decoration: none;
    }
    a:hover {
        text-decoration: none;
        color: #ff6600;
    }
    a:visited {
        /*color: purple;*/
    }
    ul, ol {
        padding: 0;
        padding-left: 18px;
        margin: 0;
    }
    li {
        line-height: 24px;
    }
    p, ul, ol {
        font-size: 16px;
        line-height: 24px;
    }
    
    ol ol, ul ol {
        list-style-type: lower-roman;
    }
    
    code, pre {
        font-family: Consolas, Monaco, Andale Mono, monospace;
        background-color:#f7f7f7;
        color: inherit;
    }
    
    code {
        font-family: Consolas, Monaco, Andale Mono, monospace;
        margin: 0 2px;
    }
    
    pre {
        font-family: Consolas, Monaco, Andale Mono, monospace;
        line-height: 1.7em;
        overflow: auto;
        padding: 6px 10px;
        border-left: 5px solid #6CE26C;
    }
    
    pre > code {
        font-family: Consolas, Monaco, Andale Mono, monospace;
        border: 0;
        display: inline;
        max-width: initial;
        padding: 0;
        margin: 0;
        overflow: initial;
        line-height: 1.6em;
        font-size: .95em;
        white-space: pre;
        background: 0 0;
    
    }
    
    code {
        color: #666555;
    }
    
    aside {
        display: block;
        float: right;
        width: 390px;
    }
    blockquote {
        border-left:.5em solid #eee;
        padding: 0 0 0 2em;
        margin-left:0;
    }
    blockquote  cite {
        font-size:14px;
        line-height:20px;
        color:#bfbfbf;
    }
    blockquote cite:before {
        content: '\2014 \00A0';
    }
    
    blockquote p {
        color: #666;
    }
    hr {
        text-align: left;
        color: #999;
        height: 2px;
        padding: 0;
        margin: 16px 0;
        background-color: #e7e7e7;
        border: 0 none;
    }
    
    dl {
        padding: 0;
    }
    
    dl dt {
        padding: 10px 0;
        margin-top: 16px;
        font-size: 1em;
        font-style: italic;
        font-weight: bold;
    }
    
    dl dd {
        padding: 0 16px;
        margin-bottom: 16px;
    }
    
    dd {
        margin-left: 0;
    }
    
    table {
        *border-collapse: collapse; /* IE7 and lower */
        border-spacing: 0;
        width: 100%;
    }
    table {
        border: solid #ccc 1px;
    }
    
    table thead {
        background: #f7f7f7;
    }
    
    table thead tr:hover {
        background: #f7f7f7
    }
    table tr:hover {
        background: #fbf8e9;
        -o-transition: all 0.1s ease-in-out;
        -webkit-transition: all 0.1s ease-in-out;
        -moz-transition: all 0.1s ease-in-out;
        -ms-transition: all 0.1s ease-in-out;
        transition: all 0.1s ease-in-out;
    }
    table td, .table th {
        border-left: 1px solid #ccc;
        border-top: 1px solid #ccc;
        padding: 10px;
        text-align: left;
    }
    
    table th {
        border-top: none;
        text-shadow: 0 1px 0 rgba(255,255,255,.5);
        padding: 5px;
        border-left: 1px solid #ccc;
    }
    
    table td:first-child, table th:first-child {
        border-left: none;
    }
    

    </style>
    '''

    css2 = '''
    /* RESET
=============================================================================*/

html, body, div, span, applet, object, iframe, h1, h2, h3, h4, h5, h6, p, blockquote, pre, a, abbr, acronym, address, big, cite, code, del, dfn, em, img, ins, kbd, q, s, samp, small, strike, strong, sub, sup, tt, var, b, u, i, center, dl, dt, dd, ol, ul, li, fieldset, form, label, legend, table, caption, tbody, tfoot, thead, tr, th, td, article, aside, canvas, details, embed, figure, figcaption, footer, header, hgroup, menu, nav, output, ruby, section, summary, time, mark, audio, video {
  margin: 0;
  padding: 0;
  border: 0;
}

/* 设置滚动条的样式 */
::-webkit-scrollbar {
width:12px;
}
/* 滚动槽 */
::-webkit-scrollbar-track {
-webkit-box-shadow:inset006pxrgba(0,0,0,0.3);
border-radius:10px;
}
/* 滚动条滑块 */
::-webkit-scrollbar-thumb {
border-radius:10px;
background:rgba(0,0,0,0.1);
-webkit-box-shadow:inset006pxrgba(0,0,0,0.5);
}
::-webkit-scrollbar-thumb:window-inactive {
background:rgba(255,0,0,0.4);
}

/* BODY
=============================================================================*/

body {
  font-family: Helvetica, arial, freesans, clean, sans-serif;
  font-size: 14px;
  line-height: 1.6;
  color: #333;
  background-color: #FDF6E3;
  padding: 20px;
  max-width: 960px;
  margin: 0 auto;
}

body>*:first-child {
  margin-top: 0 !important;
}

body>*:last-child {
  margin-bottom: 0 !important;
}

/* BLOCKS
=============================================================================*/

p, blockquote, ul, ol, dl, table, pre {
  margin: 15px 0;
}

/* HEADERS
=============================================================================*/

h1, h2, h3, h4, h5, h6 {
  margin: 20px 0 10px;
  padding: 0;
  font-weight: bold;
  -webkit-font-smoothing: antialiased;
}

h1 tt, h1 code, h2 tt, h2 code, h3 tt, h3 code, h4 tt, h4 code, h5 tt, h5 code, h6 tt, h6 code {
  font-size: inherit;
}
h4,
h5,
h6 {
  color: #859900;
}
h1 {
  font-size: 2.8em;
  color: #d33682;
}
h2 {
  font-size: 2.4em;
  color: #9B31EA;

}
h3 {
  font-size: 1.8em;
  color: #338000;
}
h4 {
  font-size: 1.4em;
}
h5 {
  font-size: 1.3em;
}
h6 {
  font-size: 1.15em;
}

body>h2:first-child, body>h1:first-child, body>h1:first-child+h2, body>h3:first-child, body>h4:first-child, body>h5:first-child, body>h6:first-child {
  margin-top: 0;
  padding-top: 0;
}

a:first-child h1, a:first-child h2, a:first-child h3, a:first-child h4, a:first-child h5, a:first-child h6 {
  margin-top: 0;
  padding-top: 0;
}

h1+p, h2+p, h3+p, h4+p, h5+p, h6+p {
  margin-top: 10px;
}

/* LINKS
=============================================================================*/

a {
  color: #b58900;
  text-decoration: none;
}
a:focus {
  outline: thin dotted;
}
a:active,
a:hover {
  outline: 0;
}
a:hover {
  color: #cb4b16;
  text-decoration: underline;
}
a:visited {
  color: #cb4b16;
}

/* LISTS
=============================================================================*/

ul, ol {
  padding-left: 30px;
}

ul li > :first-child, 
ol li > :first-child, 
ul li ul:first-of-type, 
ol li ol:first-of-type, 
ul li ol:first-of-type, 
ol li ul:first-of-type {
  margin-top: 0px;
}

ul ul, ul ol, ol ol, ol ul {
  margin-bottom: 0;
}

dl {
  padding: 0;
}

dl dt {
  font-size: 14px;
  font-weight: bold;
  font-style: italic;
  padding: 0;
  margin: 15px 0 5px;
}

dl dt:first-child {
  padding: 0;
}

dl dt>:first-child {
  margin-top: 0px;
}

dl dt>:last-child {
  margin-bottom: 0px;
}

dl dd {
  margin: 0 0 15px;
  padding: 0 15px;
}

dl dd>:first-child {
  margin-top: 0px;
}

dl dd>:last-child {
  margin-bottom: 0px;
}

/* CODE
=============================================================================*/

pre, code, tt {
  font-size: 12px;
  font-family: Consolas, "Liberation Mono", Courier, monospace;
}

code, tt {
  margin: 0 0px;
  padding: 0px 0px;
  white-space: nowrap;
  border: 1px solid #eaeaea;
  background-color: #f8f8f8;
  border-radius: 3px;
}

pre>code {
  margin: 0;
  padding: 0;
  white-space: pre;
  color: #338000;
  border: none;
  background: transparent;
 
}

pre {
  background-color: #f8f8f8;
  border: 1px solid #ccc;
  font-size: 13px;
  line-height: 19px;
  overflow: auto;
  padding: 6px 10px;
  border-radius: 3px;
}

pre code, pre tt {
  background-color: transparent;
  border: none;
}
/* QUOTES
=============================================================================*/

blockquote {
  border-left: 4px solid #DDD;
  padding: 0 15px;
  color: #777;
}

blockquote>:first-child {
  margin-top: 0px;
}

blockquote>:last-child {
  margin-bottom: 0px;
}

/* HORIZONTAL RULES
=============================================================================*/

hr {
  clear: both;
  margin: 15px 0;
  height: 0px;
  overflow: hidden;
  border: none;
  background: transparent;
  border-bottom: 4px solid #ddd;
  padding: 0;
}

/* TABLES
=============================================================================*/
table{
  margin: 0 auto;
}
table th {
  font-weight: bold;
}

table th, table td {
  border: 1px solid #ccc;
  padding: 6px 13px;
}

table tr {
  border-top: 1px solid #ccc;
  background-color: #fff;
}

table tr:nth-child(2n) {
  background-color: #f8f8f8;
}

/* IMAGES
=============================================================================*/

img {
  max-width: 100%
}
/* P
=============================================================================*/
p{
    font-size:1.2em;
}


/*目录形成的范围*/
#outline-list {
    height: 325px;
    position: fixed;
    overflow-y:scroll;
    overflow-x:hidden;
    bottom: 80px;
    right: 15px;
    width: 220px;
}'''

    # css = '''
    # <html lang="zh-cn">
    # <head>
    # <meta content="text/html; charset=utf-8" http-equiv="content-type" />
    # <link href="github.css" rel="stylesheet">
    # </head>
    # <body>
    # %s
    # </body>
    # </html>
    # '''

    process(words, filename)
    # 读取 markdown 文本
    input_file = codecs.open("./md/Vocabulary of " + filename + ".md", mode="r+", encoding="UTF-8")
    text = input_file.read()
    input_file.close()
    # 转为 html 文本
    html = markdown.markdown(text)
    # 保存为文件
    output_file = codecs.open(get_desktop_path() + "/Vocabulary of " + filename + '.html', mode="w+", encoding="utf-8")
    output_file.write(css1 + html)
    output_file.close()


def process(words, filename):
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
                 + "    " + "**例句**：" + word.get_context() + "\n\n"
                 + "    " + "**英解**：" + word.get_str_en_interpretation() + "\n\n"
                 + "    " + "**汉解**：" + word.get_str_ch_interpretation() + "\n\n")
    md.close()
