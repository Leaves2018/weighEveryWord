# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import sys
import qtawesome as qta
from weigh2 import *
import re
from vocabulary import Word


class MainUi(QMainWindow):
    def __init__(self):
        super().__init__()

        # 一、声明窗口主部件及其布局
        self.main_widget = QWidget()
        self.main_layout = QGridLayout()

        # 二、声明窗口左侧部件及其布局
        self.left_widget = QWidget()
        self.left_layout = QGridLayout()
        # 2.1 左侧菜单栏
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

        # 3.1 右侧顶部搜索框
        self.right_bar_widget = QWidget()
        self.right_bar_layout = QGridLayout()

        # 搜索标签（图标及文字）
        self.search_button = QPushButton(qta.icon("fa5s.search"), "搜索")
        # 搜索框
        self.search_line_edit = QLineEdit()

        # 3.2 单词框
        self.right_word_widget = QWidget()
        self.right_word_layout = QGridLayout()

        self.word_label = QTextEdit("Word")
        self.phonetic_symbol_label = QTextEdit("Phonetic Symbol")
        self.context_label = QTextEdit("Context")
        self.english_label = QTextEdit("English Interpretation")
        self.chinese_label = QTextEdit("Chinese Interpretation")

        self.init_ui()

    def init_ui(self):
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

        # 三、设置窗口右侧部件布局
        self.right_widget.setObjectName('right_widget')
        self.right_widget.setLayout(self.right_layout)
        # 3.1 搜索模块
        self.right_bar_widget.setLayout(self.right_bar_layout)
        self.search_line_edit.setPlaceholderText("输入单词后按回车进行查询")
        # 设置搜索按钮的点击事件
        self.search_button.setCheckable(True)
        self.search_button.clicked.connect(self.search)

        # 3.2 单词模块
        self.right_word_widget.setObjectName("right_word_widget")
        self.right_word_widget.setLayout(self.right_word_layout)

        self.add_to_window()
        self.beautify()

    # 搜索按钮点击事件
    def search(self):
        text = self.search_line_edit.text()
        word = Word(text)
        self.word_label.setText(word.get_name())
        self.phonetic_symbol_label.setText(word.get_yb())
        self.context_label.setText(word.get_context())
        self.english_label.setText(word.get_eng_interpretation())
        self.chinese_label.setText(word.get_ch_interpretation())

    # 将各个部件添加到窗口
    def add_to_window(self):
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
    def beautify(self):
        # 美化
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

        self.setWindowOpacity(0.95)  # 设置窗口透明度
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)  # 设置窗口背景透明
        self.main_layout.setSpacing(0)


def main():
    app = QApplication(sys.argv)
    gui = MainUi()
    gui.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
