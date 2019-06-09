# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import sys
import qtawesome as qta
from weigh2 import *
import re
from vocabulary2 import Word


class MainUi(QMainWindow):
    def __init__(self):
        super().__init__()

        # 一、声明窗口主部件及其布局
        self.main_widget = QWidget()
        self.main_layout = QGridLayout()

        # 二、声明窗口左侧部件及其布局
        self.left_widget = QWidget()
        self.left_layout = QGridLayout()
        # 左侧菜单栏（多UI共用）：left_ui
        self.left_label_1 = QLabel("功能选项")
        self.left_button_1 = QPushButton(qta.icon("fa5s.flag", color="white"), "标记")
        self.left_button_2 = QPushButton(qta.icon("fa5s.book", color="white"), "背诵")
        self.left_button_3 = QPushButton(qta.icon("fa5s.search", color="white"), "查询")

        self.left_label_2 = QLabel("输出设置与帮助")
        self.left_button_4 = QPushButton(qta.icon("fa5s.cog", color="white"), "设置")
        self.left_button_5 = QPushButton(qta.icon("fa5s.question", color="white"), "帮助")

        # 三、声明窗口右侧部件及其布局
        self.right_widget = QWidget()
        self.right_layout = QGridLayout()

        # 窗口右侧部件分为多个UI实现
        # 3.1 "标记"页面：mark_ui
        # 3.2 "背诵"页面：recite_ui
        # 3.3 "查询"页面：look_up_ui
        self.look_up_widget = QWidget()
        self.look_up_layout = QGridLayout()
        # 右侧顶部搜索框
        self.right_bar_widget = QWidget()
        self.right_bar_layout = QGridLayout()

        # 搜索标签（图标及文字）
        self.search_button = QPushButton(qta.icon("fa5s.search"), "搜索")
        # 搜索框
        self.search_line_edit = QLineEdit()

        # 单词框
        self.right_word_widget = QWidget()
        self.right_word_layout = QGridLayout()

        self.word_label = QTextEdit("Word")
        self.phonetic_symbol_label = QTextEdit("Phonetic Symbol")
        self.context_label = QTextEdit("Context")
        self.english_label = QTextEdit("English Interpretation")
        self.chinese_label = QTextEdit("Chinese Interpretation")

        # 3.4 "设置"页面：settings_ui
        self.settings_text_browser = QTextBrowser()
        # 3.5 "帮助"页面：help_ui
        self.contact_text_browser = QTextBrowser()
        self.left_ui()
        self.look_up_ui()
        self.help_ui()

    def left_ui(self):
        self.setFixedSize(960, 700)
        # 一、设置窗口主部件布局
        self.main_widget.setLayout(self.main_layout)

        # 二、设置窗口左侧部件布局
        self.left_widget.setObjectName('left_widget')
        self.left_widget.setLayout(self.left_layout)

        # 2.1 左侧菜单栏属性设置
        self.left_label_1.setObjectName("left_label")
        self.left_button_1.setObjectName("left_button")
        self.left_button_2.setObjectName("left_button")
        self.left_button_3.setObjectName("left_button")

        self.left_label_2.setObjectName("left_label")
        self.left_button_4.setObjectName("left_button")
        self.left_button_5.setObjectName("left_button")

        # 左侧菜单栏点击事件设置
        self.left_button_1.clicked.connect(self.mark_ui)
        self.left_button_2.clicked.connect(self.recite_ui)
        self.left_button_3.clicked.connect(self.look_up_show())
        self.left_button_4.clicked.connect(self.settings_ui)
        self.left_button_5.clicked.connect(self.help_show())

        self.left_add_to_window()
        self.left_beautify()

    def left_add_to_window(self):
        # 向窗口主部件分别添加左侧部件和右侧部件
        # 左侧部件在第0行第0列，占12行2列
        self.main_layout.addWidget(self.left_widget, 0, 0, 12, 2)
        # 右侧部件在第0行第3列，占12行10列
        self.main_layout.addWidget(self.right_widget, 0, 2, 12, 10)
        # 设置窗口主部件
        self.setCentralWidget(self.main_widget)

        # 向左侧部件添加标签及按钮
        self.left_layout.addWidget(self.left_label_1, 0, 0, 2, 3)
        self.left_layout.addWidget(self.left_button_1, 2, 0, 2, 3)
        self.left_layout.addWidget(self.left_button_2, 4, 0, 2, 3)
        self.left_layout.addWidget(self.left_button_3, 6, 0, 2, 3)

        self.left_layout.addWidget(self.left_label_2, 8, 0, 2, 3)
        self.left_layout.addWidget(self.left_button_4, 10, 0, 2, 3)
        self.left_layout.addWidget(self.left_button_5, 12, 0, 2, 3)

    def left_beautify(self):
        self.left_widget.setStyleSheet('''
            QPushButton{border:none;color:white;}
            QLabel#left_label{
                border:none;
                color:white;
                border-bottom:1px solid white;
                font-size:18px;
                font-weight:700;
                font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
            }
            QPushButton#left_button:hover{border-left:4px solid red;font-weight:700;}
            QWidget#left_widget{
            background:gray;
            border-top:1px solid white;
            border-bottom:1px solid white;
            border-left:1px solid white;
            border-top-left-radius:10px;
            border-bottom-left-radius:10px;
            }
        ''')

        self.setWindowOpacity(0.95)  # 设置窗口透明度
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)  # 设置窗口背景透明
        self.main_layout.setSpacing(0)

    def mark_ui(self):
        pass

    def mark_add_to_window(self):
        pass

    def mark_beautify(self):
        pass

    def recite_ui(self):
        pass

    def recite_add_to_window(self):
        pass

    def recite_beautify(self):
        pass

    def look_up_ui(self):
        # 三、设置窗口右侧部件布局
        self.right_widget.setObjectName('right_widget')
        self.right_widget.setLayout(self.right_layout)
        # 3.1 搜索模块
        self.right_bar_widget.setLayout(self.right_bar_layout)
        self.search_line_edit.setPlaceholderText("输入单词后按回车进行查询")
        # 实现在搜索输入框中按回车进行搜索
        self.search_line_edit.returnPressed.connect(self.look_up_search)
        # 设置搜索按钮的点击事件
        self.search_button.clicked.connect(self.look_up_search)

        # 3.2 单词模块
        self.right_word_widget.setObjectName("right_word_widget")
        self.right_word_widget.setLayout(self.right_word_layout)

        self.look_up_add_to_window()
        self.look_up_beautify()
        self.look_up_hide()

    def look_up_hide(self):
        self.right_bar_widget.hide()
        self.right_word_widget.hide()

    # 搜索按钮点击事件
    def look_up_search(self):
        text = self.search_line_edit.text()
        word = Word(text)
        self.word_label.setText(word.get_name())
        self.phonetic_symbol_label.setText(word.get_yb())
        self.context_label.setText(word.get_context())
        self.english_label.setText(word.get_en_interpretation())
        self.chinese_label.setText(word.get_ch_interpretation())

    # 将各个部件添加到窗口
    def look_up_add_to_window(self):
        # 向搜索模块添加搜索Label和搜索框LineEdit
        self.right_bar_layout.addWidget(self.search_line_edit, 0, 0, 1, 8)
        self.right_bar_layout.addWidget(self.search_button, 0, 9, 1, 1)

        self.right_layout.addWidget(self.right_bar_widget, 0, 0, 1, 9)

        # 向单词模块添加单词Label、音标Label、语境Label、英解Label、中解Label
        self.right_word_layout.addWidget(self.word_label, 0, 0, 3, 10)
        self.right_word_layout.addWidget(self.phonetic_symbol_label, 3, 0, 1, 10)
        self.right_word_layout.addWidget(self.context_label, 4, 0, 2, 10)
        self.right_word_layout.addWidget(self.english_label, 6, 0, 3, 10)
        self.right_word_layout.addWidget(self.chinese_label, 9, 0, 3, 10)

        self.right_layout.addWidget(self.right_word_widget, 1, 0, 11, 10)

    # 美化各种控件显示样式（QSS）
    def look_up_beautify(self):
        self.right_widget.setStyleSheet('''
            QWidget#right_widget{
                color:#232C51;
                background:white;
                border-top:1px solid darkGray;
                border-bottom:1px solid darkGray;
                border-right:1px solid darkGray;
                border-top-right-radius:10px;
                border-bottom-right-radius:10px;
            }
            QLabel#right_label{
                border:none;
                font-size:16px;
                font-weight:700;
                font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
            }
        ''')

        self.search_line_edit.setStyleSheet(
            '''QLineEdit{
                    border:1px solid gray;
                    width:300px;
                    border-radius:10px;
                    padding:2px 4px;
            }''')

        self.search_button.setStyleSheet(
            '''
            QPushButton{border:none;color:black;}
            '''
        )

    def look_up_hide(self):
        self.right_bar_widget.hide()
        self.right_word_widget.hide()

    def look_up_show(self):
        self.right_bar_widget.show()
        self.right_word_widget.show()

    def settings_ui(self):
        pass

    def settings_add_to_window(self):
        pass

    def settings_beautify(self):
        pass

    def help_ui(self):
        self.contact_text_browser.setText("如遇到使用上的问题或者开发建议，欢迎联系开发者：\n"
                                          "yuanyufei1999@gmail.com\n"
                                          "zhaonanfeng@foxmail.com")

        self.help_add_to_window()
        self.help_beautify()
        self.help_hide()

    def help_add_to_window(self):
        self.look_up_hide()
        # self.right_layout = QGridLayout()
        # self.right_widget.setLayout(self.right_layout)
        self.right_layout.addWidget(self.contact_text_browser, 0, 0,)

    def help_beautify(self):
        pass

    def help_hide(self):
        self.contact_text_browser.hide()

    def help_show(self):
        self.contact_text_browser.show()


def main():
    app = QApplication(sys.argv)
    gui = MainUi()
    gui.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
