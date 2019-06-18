# -*- coding: utf-8 -*-
import random

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
import sys
import qtawesome as qta
from weigh5 import *
import os


def get_desktop_path():
    return os.path.join(os.path.expanduser("~"), 'Desktop')


class MainUi(QMainWindow):
    def __init__(self):
        super().__init__()
        self.unfamiliar_words = []
        self.unknown_words = []
        self.s = ""
        self.dui = None
        self.rui = None
        self.word_count = 0
        self.shuci_count = 0
        self.sample = 1

        # self.temp_words = []

        # 一、声明窗口主部件及其布局
        self.main_widget = QWidget()
        self.main_layout = QGridLayout(self.main_widget)

        # 二、声明窗口左侧部件及其布局
        self.left_widget = QWidget()
        self.left_layout = QGridLayout(self.left_widget)

        # 左侧菜单栏（多UI共用）：left_ui
        self.left_label_1 = QLabel("功能选项")
        self.left_label_1.setAlignment(Qt.AlignCenter)
        self.left_button_1 = QPushButton(qta.icon("fa5s.flag", color="white"), "标记")
        self.left_button_2 = QPushButton(qta.icon("fa5s.book", color="white"), "背诵")
        self.left_button_3 = QPushButton(qta.icon("fa5s.search", color="white"), "查询")

        self.left_label_2 = QLabel("输出设置与帮助")
        self.left_label_2.setAlignment(Qt.AlignCenter)
        self.left_button_4 = QPushButton(qta.icon("fa5s.cog", color="white"), "设置")
        self.left_button_5 = QPushButton(qta.icon("fa5s.question", color="white"), "帮助")

        # 三、声明窗口右侧部件及其布局
        self.right_widget = QStackedWidget()
        self.right_widget.setObjectName('right_widget')

        # 窗口右侧部件分为多个UI实现
        # 3.1 "标记"页面：mark_ui
        self.mark_ui_widget = QWidget()
        self.mark_ui_layout = QGridLayout(self.mark_ui_widget)

        self.test_label_1 = QLabel("这里是标记页面")

        self.input_text_edit = QTextEdit()
        self.clear_button = QPushButton("清空")
        self.clean_button = QPushButton("去中文去符号去数字")
        self.start_button = QPushButton("开始生熟词判断")

        # 3.2 "背诵"页面：recite_ui
        self.recite_ui_widget = QWidget()
        self.recite_ui_layout = QVBoxLayout(self.recite_ui_widget)

        self.recite_in_widget = QWidget()
        self.recite_in_layout = QHBoxLayout(self.recite_in_widget)

        self.shuci_in_widget = QWidget()
        self.shuci_in_layout = QHBoxLayout(self.shuci_in_widget)

        self.shengci_in_widget = QWidget()
        self.shengci_in_layout = QHBoxLayout(self.shengci_in_widget)

        self.recite_label_cihuiliang = QLabel("词汇量")
        self.recite_label_cihuiliang.setFont(QFont("Roman times", 36, QFont.Bold))
        self.recite_label_shuciliang = QLabel("熟词量：" + str(self.shuci_len_return()))
        self.recite_label_shuciliang.setFont(QFont("Roman times", 18, QFont.Bold))
        self.recite_label_shengciliang = QLabel("生词量：" + str(self.shengci_len_return()))
        self.recite_label_shengciliang.setFont(QFont("Roman times", 18, QFont.Bold))

        self.shuci_output_button = QPushButton("导出熟词本")
        self.shengci_output_button = QPushButton("导出生词本")

        self.recite_label_bar_1 = QtWidgets.QProgressBar()  # 播放进度部件
        self.recite_label_bar_1.setRange(0, 1001)
        self.recite_label_bar_1.setValue(1000)
        self.recite_label_bar_1.setFixedHeight(2)  # 设置进度条高度
        self.recite_label_bar_1.setTextVisible(False)  # 不显示进度条文字

        self.recite_label_beisong = QLabel("背诵生词")
        self.recite_label_beisong.setFont(QFont("Roman times", 36, QFont.Bold))
        self.word_count_question_label = QLabel("你今天想背几个单词呀？")
        self.word_count_question_label.setFont(QFont("Roman times", 18, QFont.Bold))
        self.word_count_line_edit = QLineEdit()
        self.word_recite_button = QPushButton("开始背单词")


        # self.test_label_2 = QLabel("这里是背诵页面")

        # 3.3 "查询"页面：look_up_ui
        self.look_up_ui_widget = QWidget()
        self.look_up_ui_layout = QGridLayout(self.look_up_ui_widget)

        # 右侧顶部搜索框
        self.right_bar_widget = QWidget()
        self.right_bar_layout = QGridLayout(self.right_bar_widget)
        # 搜索标签（图标及文字）
        self.search_button = QPushButton(qta.icon("fa5s.search"), "搜索")
        # 搜索框
        self.search_line_edit = QLineEdit()

        # 单词框
        self.right_word_widget = QWidget()
        self.right_word_layout = QGridLayout(self.right_word_widget)

        self.word_text_edit = QTextEdit("Word")
        self.yb_text_edit = QTextEdit("Phonetic Symbol")
        self.context_text_edit = QTextEdit("Context")
        self.english_text_edit = QTextEdit("English Interpretation")
        self.chinese_text_edit = QTextEdit("Chinese Interpretation")

        # 按钮框
        self.look_up_down_widget = QWidget()
        self.look_up_down_layout = QGridLayout(self.look_up_down_widget)

        self.new_button = QPushButton(qta.icon("fa5s.star", color="black"), "生词")
        self.old_button = QPushButton(qta.icon("fa5s.eye-slash", color="black"), "熟词")

        # 3.4 "设置"页面：settings_ui
        self.settings_ui_widget = QWidget()
        self.settings_ui_layout = QVBoxLayout(self.settings_ui_widget)

        self.settings_button_widget = QWidget()
        self.settings_button_layout = QHBoxLayout(self.settings_button_widget)

        self.test_label_shuci = QLabel("设置熟词")
        self.test_label_shuci.setFont(QFont("Roman times", 16, QFont.Bold))
        self.shuci_xiaoxue_checkbox = QCheckBox('小学词汇')
        self.shuci_chuzhong_checkbox = QCheckBox('初中词汇')
        self.shuci_gaozhong_checkbox = QCheckBox('高中词汇')
        self.shuci_siliuji_checkbox = QCheckBox('英语CET4、6词汇')

        self.down_process_bar_1 = QtWidgets.QProgressBar()  # 播放进度部件
        self.down_process_bar_1.setRange(0, 1001)
        self.down_process_bar_1.setValue(1000)
        self.down_process_bar_1.setFixedHeight(2)  # 设置进度条高度
        self.down_process_bar_1.setTextVisible(False)  # 不显示进度条文字

        self.test_label_choice = QLabel("输出选择")
        self.test_label_choice.setFont(QFont("Roman times", 16, QFont.Bold))
        self.goal_example_original_checkbox = QCheckBox('例句')
        self.goal_example_youdao_checkbox = QCheckBox('有道例句')
        self.goal_ying_checkbox = QCheckBox('英解')
        self.goal_han_checkbox = QCheckBox('汉解')

        self.down_process_bar_2 = QtWidgets.QProgressBar()  # 播放进度部件
        self.down_process_bar_2.setRange(0, 1001)
        self.down_process_bar_2.setValue(1000)
        self.down_process_bar_2.setFixedHeight(2)  # 设置进度条高度
        self.down_process_bar_2.setTextVisible(False)  # 不显示进度条文字

        self.test_label_output = QLabel("输出样式")
        self.test_label_output.setFont(QFont("Roman times", 16, QFont.Bold))
        self.sample_output_button_1 = QToolButton()
        self.sample_output_button_1.setText("样式1")  # 设置按钮文本
        img_1 = QtGui.QImage(r'./sample_format/sample_format_1.png')
        pixmap_1 = QtGui.QPixmap(img_1)
        fitPixmap_1 = pixmap_1.scaled(600, 160, QtCore.Qt.IgnoreAspectRatio, QtCore.Qt.SmoothTransformation)
        icon_1 = QtGui.QIcon(fitPixmap_1)
        self.sample_output_button_1.setIcon(icon_1)  # 设置按钮图标
        self.sample_output_button_1.toggle()
        self.sample_output_button_1.setIconSize(QtCore.QSize(600, 160))  # 设置图标大小
        self.sample_output_button_1.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)

        self.sample_output_button_2 = QToolButton()
        self.sample_output_button_2.setText("样式2")  # 设置按钮文本
        img_2 = QtGui.QImage(r'./sample_format/sample_format_2.png')
        pixmap_2 = QtGui.QPixmap(img_2)
        fitPixmap_2 = pixmap_2.scaled(600, 160, QtCore.Qt.IgnoreAspectRatio, QtCore.Qt.SmoothTransformation)
        icon_2 = QtGui.QIcon(fitPixmap_2)
        self.sample_output_button_2.setIcon(icon_2)  # 设置按钮图标
        self.sample_output_button_2.toggle()
        self.sample_output_button_2.setIconSize(QtCore.QSize(600, 160))  # 设置图标大小
        self.sample_output_button_2.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)

        self.sample_output_button_3 = QToolButton()
        self.sample_output_button_3.setText("样式3")  # 设置按钮文本
        img_3 = QtGui.QImage(r'./sample_format/sample_format_3.png')
        pixmap_3 = QtGui.QPixmap(img_3)
        fitPixmap_3 = pixmap_3.scaled(600, 160, QtCore.Qt.IgnoreAspectRatio, QtCore.Qt.SmoothTransformation)
        icon_3 = QtGui.QIcon(fitPixmap_3)
        self.sample_output_button_3.setIcon(icon_3)  # 设置按钮图标
        self.sample_output_button_3.toggle()
        self.sample_output_button_3.setIconSize(QtCore.QSize(600, 160))  # 设置图标大小
        self.sample_output_button_3.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)

        self.initial_value_button = QPushButton("恢复默认值")
        self.ensure_value_button = QPushButton("确认")

        # 3.5 "帮助"页面：help_ui
        self.help_ui_widget = QWidget()
        self.help_ui_layout = QGridLayout(self.help_ui_widget)
        self.contact_text_browser = QTextBrowser()
        self.support_qr_code_button = QToolButton()

        self.main_ui()
        self.left_ui()
        self.right_ui()
        self.mark_ui()
        self.recite_ui()
        self.look_up_ui()
        self.settings_ui()
        self.help_ui()

    def shengci_len_return(self):
        with open("./vocabulary/vocabulary_words.txt", "r+", encoding="UTF-8") as f:
            temp_words = []
            for sentence in f.readlines():
                if not sentence[0].isalpha():
                    continue
                word = Word(*sentence.split("----"))
                temp_words.append(word)
        return len(temp_words)

    def shuci_len_return(self):
        with open("./familiar/familiar_words.txt", "r+", encoding="UTF-8") as f:
            return len(f.readlines())

    def main_ui(self):
        # 设置窗口大小
        self.setBaseSize(960, 700)
        # 设置窗口主部件
        self.setCentralWidget(self.main_widget)
        # 设置窗口名称
        self.setWindowTitle("字斟句酌 Weigh Every Word")

    def left_ui(self):
        # 设置名称，方便QSS统一修改样式
        self.left_widget.setObjectName('left_widget')

        # 左侧菜单栏属性设置：
        # 两个标签：功能选项、输出设置与帮助
        # 五个按钮：标记、背诵、查询、设置、帮助
        self.left_label_1.setObjectName("left_label")
        self.left_button_1.setObjectName("left_button")
        self.left_button_2.setObjectName("left_button")
        self.left_button_3.setObjectName("left_button")

        self.left_label_2.setObjectName("left_label")
        self.left_button_4.setObjectName("left_button")
        self.left_button_5.setObjectName("left_button")

        # 左侧菜单栏点击事件设置
        self.left_button_1.clicked.connect(self.on_mark_ui_clicked)
        self.left_button_2.clicked.connect(self.on_recite_ui_clicked)
        self.left_button_3.clicked.connect(self.on_look_up_ui_clicked)
        self.left_button_4.clicked.connect(self.on_settings_ui_clicked)
        self.left_button_5.clicked.connect(self.on_help_ui_clicked)

        self.settings_read()

        # 将组件加入窗口
        self.left_add_to_window()
        # 进行美化
        self.left_beautify()

    def left_add_to_window(self):
        # 向左侧部件添加标签及按钮

        self.left_layout.addWidget(self.left_label_1, 0, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_1, 1, 0, 2, 3)
        self.left_layout.addWidget(self.left_button_2, 3, 0, 2, 3)
        self.left_layout.addWidget(self.left_button_3, 5, 0, 2, 3)

        self.left_layout.addWidget(self.left_label_2, 7, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_4, 8, 0, 2, 3)
        self.left_layout.addWidget(self.left_button_5, 10, 0, 2, 3)

        # 左侧部件在第0行第0列，占12行2列
        self.main_layout.addWidget(self.left_widget, 0, 0, 12, 2)

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

    def on_mark_ui_clicked(self):
        self.right_widget.setCurrentIndex(0)

    def on_recite_ui_clicked(self):
        self.right_widget.setCurrentIndex(1)
        self.recite_label_shuciliang.setText("熟词量：" + str(self.shuci_len_return()))
        self.recite_label_shengciliang.setText("生词量：" + str(self.shengci_len_return()))

    def on_look_up_ui_clicked(self):
        self.right_widget.setCurrentIndex(2)

    def on_settings_ui_clicked(self):
        self.right_widget.setCurrentIndex(3)
        self.settings_read()

    def on_help_ui_clicked(self):
        self.right_widget.setCurrentIndex(4)

    def right_ui(self):
        self.right_add_to_window()
        self.right_beautify()

    def right_add_to_window(self):
        # 右侧部件在第0行第3列，占12行10列
        self.main_layout.addWidget(self.right_widget, 0, 3, 12, 10)

    def right_beautify(self):
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

    def mark_ui(self):
        self.input_text_edit.setPlaceholderText("请输入要标记生词的文本")

        self.clear_button.clicked.connect(self.mark_clear)
        self.clean_button.clicked.connect(self.mark_clean)
        self.start_button.clicked.connect(self.mark_start)

        self.mark_add_to_window()
        self.mark_beautify()

    def mark_add_to_window(self):
        # self.mark_ui_layout.addWidget(self.test_label_1, 0, 0,)
        self.mark_ui_layout.addWidget(self.input_text_edit, 0, 0, 11, 10)
        self.mark_ui_layout.addWidget(self.clear_button, 11, 0, 1, 2)
        self.mark_ui_layout.addWidget(self.clean_button, 11, 2, 1, 4)
        self.mark_ui_layout.addWidget(self.start_button, 11, 6, 1, 4)

        self.right_widget.addWidget(self.mark_ui_widget)

    def mark_clear(self):
        self.input_text_edit.clear()

    def mark_clean(self):
        self.s = self.input_text_edit.toPlainText()
        text = re.sub('[^a-zA-Z\']+', ' ', self.s)
        if text:
            self.input_text_edit.setText(text)
            self.input_text_edit.setFontPointSize(15)
            self.test_dialog_1()
        else:
            self.test_dialog_2()

    def test_dialog_1(self):
        res = QtWidgets.QMessageBox.question(self, '提示',
                                             "已接收到文本，初步处理完毕。\n"
                                             "请快速浏览并手动修改不合理的分词:)\n"
                                             , QtWidgets.QMessageBox.Yes |
                                             QtWidgets.QMessageBox.No,
                                             QtWidgets.QMessageBox.Yes)
        if res == QtWidgets.QMessageBox.Yes:
            pass
        else:
            pass

    def test_dialog_2(self):
        res = QtWidgets.QMessageBox.question(self, '提示',
                                             "未接收到文本，请确认输入正确", QtWidgets.QMessageBox.Yes |
                                             QtWidgets.QMessageBox.No,
                                             QtWidgets.QMessageBox.Yes)
        if res == QtWidgets.QMessageBox.Yes:
            pass
        else:
            pass

    def mark_start(self):
        res = QtWidgets.QMessageBox.question(self, '提示',
                                             "文本已确认完毕？", QtWidgets.QMessageBox.Yes |
                                             QtWidgets.QMessageBox.No,
                                             QtWidgets.QMessageBox.Yes)
        if res == QtWidgets.QMessageBox.Yes:
            self.unfamiliar_words, self.unknown_words = first(self.s)
            if len(self.unknown_words) == 0:
                # 如果没有未知词，则不进入DecideUi。直接判断是否有生词，有则生成单词本，没有则再提示改文章也没有生词。
                self.show_dialog(text2="该文本中没有未知词，无需您手动判断。\n"
                                       "将自动生成本文生词单词表。")
                if len(self.unfamiliar_words) == 0:
                    self.show_dialog(text2="该文本中也没有生词，该文本无需标记")
                else:
                    filename, ok = QInputDialog.getText(self, "提示", "生词标记完成，原文及单词表将保存至桌面。\n"
                                                                    "请输入文件名称：")
                    if ok:
                        f = open("./input/" + str(filename) + ".txt", mode="w+",
                                 encoding="UTF-8")
                        f.write(self.s)
                        f.close()
                        third(self.unfamiliar_words,
                              filename,
                              self.goal_example_original_checkbox.isChecked(),
                              self.goal_ying_checkbox.isChecked(),
                              self.goal_han_checkbox.isChecked())

                return 0

            self.dui = DecideUi(s=self.s,
                                unfamiliar_words=self.unfamiliar_words,
                                unknown_words=self.unknown_words,
                                show_youdao=self.goal_example_youdao_checkbox.isChecked(),
                                show_english=self.goal_ying_checkbox.isChecked(),
                                show_chinese=self.goal_han_checkbox.isChecked(),
                                show_context=self.goal_example_original_checkbox.isChecked())
            self.dui.show()

    def show_dialog(self, text1="提示", text2="不符合条件"):
        res = QMessageBox.information(self, text1,
                                   text2, QtWidgets.QMessageBox.Yes |
                                   QtWidgets.QMessageBox.No,
                                   QtWidgets.QMessageBox.Yes)
        if res == QMessageBox.Yes:
            return 0
        else:
            return 0

    def mark_beautify(self):
        self.clear_button.setStyleSheet(
            '''QPushButton{
                    border-style: outset;
                    border-width:2px;
                    border-radius:10px;
                    border-color: black;
                    font: bold 14px;
                    min-width:10em;
                    padding:6px;
            }''')

        self.clean_button.setStyleSheet(
            '''QPushButton{
                    border-style: outset;
                    border-width:2px;
                    border-radius:10px;
                    border-color: black;
                    font: bold 14px;
                    min-width:10em;
                    padding:6px;
            }''')

        self.start_button.setStyleSheet(
            '''QPushButton{
                    border-style: outset;
                    border-width:2px;
                    border-radius:10px;
                    border-color: black;
                    font: bold 14px;
                    min-width:10em;
                    padding:6px;
            }''')
        self.input_text_edit.setStyleSheet(
            '''QTextEdit{
                    border-style: outset;
                    border-width:2px;
                    border-radius:10px;
                    border-color: black;
                    font: bold 16px;
                    min-width:10em;
                    padding:6px;
            }''')

    def recite_ui(self):
        self.word_count_line_edit.returnPressed.connect(self.recite_start)
        self.word_recite_button.clicked.connect(self.recite_start)

        self.shuci_output_button.clicked.connect(self.shuci_output)
        self.shengci_output_button.clicked.connect(self.shengci_output)

        self.recite_add_to_window()
        self.recite_beautify()

    def shuci_output(self):
        familiar_words = open("./familiar/familiar_words.txt", "r+", encoding="UTF-8")
        output_file = open(get_desktop_path() + "/familiar_words.txt", mode="w+", encoding="UTF-8")
        output_file.write(familiar_words.read())
        familiar_words.close()
        output_file.close()
        res = QtWidgets.QMessageBox.information(self, '提示',
                                                "您的熟词本已生成至桌面", QtWidgets.QMessageBox.Yes |
                                                QMessageBox.No,
                                                QtWidgets.QMessageBox.Yes)

    def shengci_output(self):
        temp_words = []
        with open("./vocabulary/vocabulary_words.txt", "r+", encoding="UTF-8") as f:
            for sentence in f.readlines():
                if not sentence[0].isalpha():
                    continue
                text = sentence.split("----")
                word = Word(name=text[0], yb=text[1], context=text[2])
                word.set_en_interpretation(re.split("[)(1-9]+", text[3])[1:])
                word.set_ch_interpretation(re.split("[)(1-9]+", text[4])[1:])
                temp_words.append(word)
        output_file1 = open(get_desktop_path() + "/vocabulary_words.txt", mode="w+", encoding="UTF-8")
        output_file1.writelines(["\n" + i.to_string() for i in temp_words])
        output_file1.close()
        generate_word_list(temp_words, "生词本",
                           self.goal_example_original_checkbox.isChecked(),
                           self.goal_ying_checkbox.isChecked(),
                           self.goal_han_checkbox.isChecked())
        res = QtWidgets.QMessageBox.information(self, '提示',
                                                "您的生词本已生成至桌面", QtWidgets.QMessageBox.Yes |
                                                QMessageBox.No,
                                                QtWidgets.QMessageBox.Yes)

    # 打开背单词页面
    def recite_start(self):
        try:
            self.word_count = int(self.word_count_line_edit.text())
        except ValueError:
            res = QtWidgets.QMessageBox.information(self, '提示，您输入的不是数字',
                                                    "请重新输入要背的单词数目（以阿拉伯数字形式）", QtWidgets.QMessageBox.Yes |
                                                    QMessageBox.No,
                                                    QtWidgets.QMessageBox.Yes)
            if res == QtWidgets.QMessageBox.Yes:
                return 0
            else:
                return 0
        finally:
            self.word_count_line_edit.clear()

        if self.word_count <= 0 or self.word_count > self.shengci_len_return():
            res = QtWidgets.QMessageBox.information(self, '提示', '您输入的数字小于零或大于您生词本的生词数量',
                                                    QtWidgets.QMessageBox.Yes |
                                                    QMessageBox.No,
                                                    QtWidgets.QMessageBox.Yes)
            self.word_count_line_edit.clear()
            return 0

        res = QtWidgets.QMessageBox.question(self, '提示',
                                             "确认就背这" + str(self.word_count) + "个单词吗？", QtWidgets.QMessageBox.Yes |
                                             QMessageBox.No,
                                             QtWidgets.QMessageBox.Yes)
        if res == QtWidgets.QMessageBox.Yes:
            self.rui = ReciteUi(word_count=self.word_count)
            self.rui.show()
        else:
            return 0

    def recite_add_to_window(self):
        self.right_widget.addWidget(self.recite_ui_widget)
        self.recite_ui_layout.addWidget(self.recite_label_cihuiliang)
        self.recite_ui_layout.addWidget(self.shuci_in_widget)
        self.shuci_in_layout.addWidget(self.recite_label_shuciliang)
        self.shuci_in_layout.addWidget(self.shuci_output_button)
        self.recite_ui_layout.addWidget(self.shengci_in_widget)
        self.shengci_in_layout.addWidget(self.recite_label_shengciliang)
        self.shengci_in_layout.addWidget(self.shengci_output_button)
        self.recite_ui_layout.addWidget(self.recite_label_bar_1)
        self.recite_ui_layout.addWidget(self.recite_label_beisong)
        self.recite_ui_layout.addWidget(self.word_count_question_label)

        self.recite_ui_layout.addWidget(self.recite_in_widget)
        self.recite_in_layout.addWidget(self.word_count_line_edit)
        self.recite_in_layout.addWidget(self.word_recite_button)

    def recite_beautify(self):
        self.shuci_output_button.setStyleSheet(
            '''QPushButton{
                    border-style: outset;
                    border-width:2px;
                    border-radius:10px;
                    border-color: black;
                    font: bold 14px;
                    min-width:10em;
                    padding:6px;
            }''')

        self.shengci_output_button.setStyleSheet(
            '''QPushButton{
                    border-style: outset;
                    border-width:2px;
                    border-radius:10px;
                    border-color: black;
                    font: bold 14px;
                    min-width:10em;
                    padding:6px;
            }''')

        self.word_count_line_edit.setStyleSheet(
            '''QLineEdit{
                    border:1px solid gray;
                    width:300px;
                    border-radius:10px;
                    padding:2px 4px;
            }''')

        self.word_recite_button.setStyleSheet(
            '''QPushButton{
                    background-color: orange;
                    border-style: outset;
                    border-width:2px;
                    border-radius:10px;
                    border-color: beige;
                    font: bold 14px;
                    min-width:10em;
                    padding:6px;
            }''')

    def look_up_ui(self):
        # 搜索模块
        self.search_line_edit.setPlaceholderText("输入单词后按回车进行查询")
        # 实现在搜索输入框中按回车进行搜索
        self.search_line_edit.returnPressed.connect(self.look_up_search)
        # 设置搜索按钮的点击事件
        self.search_button.clicked.connect(self.look_up_search)

        # 单词模块
        self.right_word_widget.setObjectName("right_word_widget")

        self.word_text_edit.setPlaceholderText("单词框为空")
        self.word_text_edit.setFontPointSize(36)
        self.yb_text_edit.setPlaceholderText("抱歉，未查询到音标")
        self.yb_text_edit.setFontPointSize(36)
        self.context_text_edit.setPlaceholderText("抱歉，未查询到例句")
        self.context_text_edit.setFontPointSize(18)
        self.english_text_edit.setPlaceholderText("抱歉，未查询到英文解释")
        self.english_text_edit.setFontPointSize(18)
        self.chinese_text_edit.setPlaceholderText("抱歉，未查询到中文解释")
        self.chinese_text_edit.setFontPointSize(18)

        self.new_button.clicked.connect(self.add_to_vocabulary_word)
        self.old_button.clicked.connect(self.add_to_familiar_word)

        self.look_up_add_to_window()
        self.look_up_beautify()

    # 搜索按钮点击事件
    def look_up_search(self):
        text = self.search_line_edit.text()
        if not text.isalpha():
            self.search_line_edit.clear()
            return 0
        word = Word(text)
        self.word_text_edit.setText(word.get_name())
        self.yb_text_edit.setText(word.get_yb())
        self.context_text_edit.setText(word.get_context())
        # self.context_text_edit.setText(word.get_str_context())
        self.english_text_edit.setText(word.get_str_en_interpretation())
        self.chinese_text_edit.setText(word.get_str_ch_interpretation())

    def add_to_vocabulary_word(self):
        pass

    def add_to_familiar_word(self):
        pass

    # 将各个部件添加到窗口
    def look_up_add_to_window(self):
        # 向搜索模块添加搜索Label和搜索框LineEdit
        self.right_bar_layout.addWidget(self.search_line_edit, 0, 0, 1, 8)
        self.right_bar_layout.addWidget(self.search_button, 0, 9, 1, 1)

        # 向单词模块添加单词Label、音标Label、语境Label、英解Label、中解Label
        self.right_word_layout.addWidget(self.word_text_edit, 0, 0, 2, 5)
        self.right_word_layout.addWidget(self.yb_text_edit, 2, 0, 2, 5)
        self.right_word_layout.addWidget(self.english_text_edit, 0, 5, 4, 5)
        self.right_word_layout.addWidget(self.context_text_edit, 5, 0, 6, 5)
        self.right_word_layout.addWidget(self.chinese_text_edit, 5, 5, 6, 5)

        self.look_up_down_layout.addWidget(self.new_button, 0, 0, 0, 5)
        self.look_up_down_layout.addWidget(self.old_button, 0, 6, 0, 5)

        self.look_up_ui_layout.addWidget(self.right_bar_widget, 0, 0, 1, 10)
        self.look_up_ui_layout.addWidget(self.right_word_widget, 1, 0, 10, 10)
        # self.look_up_ui_layout.addWidget(self.look_up_down_widget, 11, 0, 11, 10)

        self.right_widget.addWidget(self.look_up_ui_widget)

    # 美化各种控件显示样式（QSS）
    def look_up_beautify(self):
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
        self.new_button.setStyleSheet(
            '''QPushButton{
                    border-style: outset;
                    border-width:2px;
                    border-radius:10px;
                    border-color: black;
                    font: bold 14px;
                    min-width:10em;
                    padding:6px;
            }''')
        self.old_button.setStyleSheet(
            '''QPushButton{
                    border-style: outset;
                    border-width:2px;
                    border-radius:10px;
                    border-color: black;
                    font: bold 14px;
                    min-width:10em;
                    padding:6px;
            }''')

        self.word_text_edit.setStyleSheet(
            '''QTextEdit{
                border-style: outset;
                border-width: 1px; 
                border-radius: 10px;   
                font: bold 24px;
                min-width: 10em;
                padding: 5px;
            }'''
        )

        self.yb_text_edit.setStyleSheet(
            '''QTextEdit{
                border-style: outset;
                border-width: 1px; 
                border-radius: 10px;   
                font: bold 24px;
                min-width: 10em;
                padding: 5px;
            }'''
        )
        self.english_text_edit.setStyleSheet(
            '''QTextEdit{
                border-style: outset;
                border-width: 1px; 
                border-radius: 10px;   
                font: 14px;
                min-width: 10em;
                padding: 5px;
            }'''
        )
        self.chinese_text_edit.setStyleSheet(
            '''QTextEdit{
                border-style: outset;
                border-width: 1px; 
                border-radius: 10px;   
                font: 14px;
                min-width: 10em;
                padding: 5px;
            }'''
        )
        self.context_text_edit.setStyleSheet(
            '''QTextEdit{
                border-style: outset;
                border-width: 1px; 
                border-radius: 10px;   
                font: 14px;
                min-width: 10em;
                padding: 5px;
            }'''
        )


    def settings_ui(self):
        self.initial_value_button.clicked.connect(self.restore_initial_value)
        self.ensure_value_button.clicked.connect(self.ensure_value)

        self.sample_output_button_1.clicked.connect(self.sample_1_output)
        self.sample_output_button_2.clicked.connect(self.sample_2_output)
        self.sample_output_button_3.clicked.connect(self.sample_3_output)

        self.settings_add_to_window()
        self.settings_beautify()

    def sample_1_output(self):
        self.sample = 1

    def sample_2_output(self):
        self.sample = 2

    def sample_3_output(self):
        self.sample = 3

    def restore_initial_value(self):
        self.shuci_xiaoxue_checkbox.setCheckState(Qt.Checked)
        self.shuci_chuzhong_checkbox.setCheckState(Qt.Checked)
        self.shuci_gaozhong_checkbox.setCheckState(Qt.Checked)
        self.shuci_siliuji_checkbox.setCheckState(Qt.Unchecked)
        self.goal_example_original_checkbox.setCheckState(Qt.Checked)
        self.goal_example_youdao_checkbox.setCheckState(Qt.Unchecked)
        self.goal_ying_checkbox.setCheckState(Qt.Checked)
        self.goal_han_checkbox.setCheckState(Qt.Checked)
        self.sample = 1
        with open("./css/css.txt", "w+", encoding="UTF-8") as f:
            f1 = open("./css/css1.txt", encoding="UTF-8")
            f.writelines(f1.readlines())

    def ensure_value(self):
        res = QtWidgets.QMessageBox.question(self, '警告',
                                             "您选择了"
                                             + ("《小学词汇》" if self.shuci_xiaoxue_checkbox.isChecked() else "")
                                             + ("《初中词汇》" if self.shuci_chuzhong_checkbox.isChecked() else "")
                                             + ("《高中词汇》" if self.shuci_gaozhong_checkbox.isChecked() else "")
                                             + ("《四六级词汇》" if self.shuci_siliuji_checkbox.isChecked() else "" + "\n")
                                             + ("《例句》" if self.goal_example_original_checkbox.isChecked() else "")
                                             + ("《有道例句》" if self.goal_example_youdao_checkbox.isChecked() else "")
                                             + ("《英解》" if self.goal_ying_checkbox.isChecked() else "")
                                             + ("《汉解》" if self.goal_han_checkbox.isChecked() else "" + "\n")
                                             + "样式" + str(self.sample) + "\n"
                                             "此操作会清空你的熟词本,并初始化为你所勾选的单词本。\n"
                                             "按下确认以执行操作", QtWidgets.QMessageBox.Yes |
                                             QtWidgets.QMessageBox.No,
                                             QtWidgets.QMessageBox.Yes)
        if res == QtWidgets.QMessageBox.Yes:
            settings = []
            with open('./familiar/familiar_words.txt', 'w+', encoding='UTF-8') as f:
                xiaoxue = open('./familiar/xiaoxue.txt', 'r+',
                               encoding='UTF-8').readlines() if self.shuci_xiaoxue_checkbox.isChecked() else "\n"
                f.writelines(xiaoxue)
                settings.append(self.shuci_xiaoxue_checkbox.isChecked())
                chuzhong = open('./familiar/chuzhong.txt', 'r+',
                                encoding='UTF-8').readlines() if self.shuci_chuzhong_checkbox.isChecked() else "\n"
                f.writelines(chuzhong)
                settings.append(self.shuci_chuzhong_checkbox.isChecked())
                gaozhong = open('./familiar/gaozhong.txt', 'r+',
                                encoding='UTF-8').readlines() if self.shuci_gaozhong_checkbox.isChecked() else "\n"
                f.writelines(gaozhong)
                settings.append(self.shuci_gaozhong_checkbox.isChecked())
                cet = open('./familiar/cet.txt', 'r+',
                                encoding='UTF-8').readlines() if self.shuci_siliuji_checkbox.isChecked() else "\n"
                f.writelines(cet)
                settings.append(self.shuci_siliuji_checkbox.isChecked())

                settings.append(self.goal_ying_checkbox.isChecked())
                settings.append(self.goal_han_checkbox.isChecked())
                settings.append(self.goal_example_original_checkbox.isChecked())
                settings.append(self.goal_example_youdao_checkbox.isChecked())

            with open("./css/css.txt", "w+", encoding="UTF-8") as f:
                f1 = open("./css/css" + str(self.sample) + ".txt", encoding="UTF-8")
                f.writelines(f1.readlines())

            settings.append(self.sample)
            with open("./settings/settings.txt", "w", encoding="UTF-8") as f:
                f.writelines([str(i) + "\n" for i in settings])

    # 从文件中读取复选框状态
    def settings_read(self):
        with open("./settings/settings.txt", "r+", encoding="UTF-8") as f:
            settings = []
            for line in f.readlines():
                settings.append(line.strip())
            self.shuci_xiaoxue_checkbox.setCheckState(Qt.Checked if settings[0] == "True" else Qt.Unchecked)
            self.shuci_chuzhong_checkbox.setCheckState(Qt.Checked if settings[1] == "True" else Qt.Unchecked)
            self.shuci_gaozhong_checkbox.setCheckState(Qt.Checked if settings[2] == "True" else Qt.Unchecked)
            self.shuci_siliuji_checkbox.setCheckState(Qt.Checked if settings[3] == "True" else Qt.Unchecked)
            self.goal_ying_checkbox.setCheckState(Qt.Checked if settings[4] == "True" else Qt.Unchecked)
            self.goal_han_checkbox.setCheckState(Qt.Checked if settings[5] == "True" else Qt.Unchecked)
            self.goal_example_original_checkbox.setCheckState(Qt.Checked if settings[6] == "True" else Qt.Unchecked)
            self.goal_example_youdao_checkbox.setCheckState(Qt.Checked if settings[7] == "True" else Qt.Unchecked)

            if int(settings[8]) == 1:
                self.sample_1_output()
            elif int(settings[8]) == 2:
                self.sample_2_output()
            elif int(settings[8]) == 3:
                self.sample_3_output()

    def settings_add_to_window(self):
        self.settings_ui_layout.addWidget(self.test_label_shuci)
        self.settings_ui_layout.addWidget(self.shuci_xiaoxue_checkbox)
        self.settings_ui_layout.addWidget(self.shuci_chuzhong_checkbox)
        self.settings_ui_layout.addWidget(self.shuci_gaozhong_checkbox)
        self.settings_ui_layout.addWidget(self.shuci_siliuji_checkbox)

        self.settings_ui_layout.addWidget(self.down_process_bar_1)

        self.settings_ui_layout.addWidget(self.test_label_choice)
        self.settings_ui_layout.addWidget(self.goal_ying_checkbox)
        self.settings_ui_layout.addWidget(self.goal_han_checkbox)
        self.settings_ui_layout.addWidget(self.goal_example_original_checkbox)
        self.settings_ui_layout.addWidget(self.goal_example_youdao_checkbox)

        self.settings_ui_layout.addWidget(self.down_process_bar_2)

        self.settings_ui_layout.addWidget(self.test_label_output)
        self.settings_ui_layout.addWidget(self.sample_output_button_1)
        self.settings_ui_layout.addWidget(self.sample_output_button_2)
        self.settings_ui_layout.addWidget(self.sample_output_button_3)

        self.settings_ui_layout.addWidget(self.settings_button_widget)
        self.settings_button_layout.addWidget(self.initial_value_button)
        self.settings_button_layout.addWidget(self.ensure_value_button)

        self.right_widget.addWidget(self.settings_ui_widget)

    def settings_beautify(self):
        self.initial_value_button.setStyleSheet(
            '''QPushButton{
                    border-style: outset;
                    border-width:2px;
                    border-radius:10px;
                    border-color: black;
                    font: bold 14px;
                    min-width:10em;
                    padding:6px;
            }''')
        self.ensure_value_button.setStyleSheet(
            '''QPushButton{
                    border-style: outset;
                    border-width:2px;
                    border-radius:10px;
                    border-color: black;
                    font: bold 14px;
                    min-width:10em;
                    padding:6px;
            }''')


    def help_ui(self):
        self.contact_text_browser.setText("如遇到使用上的问题或者开发建议，欢迎联系开发者：\n"
                                          "yuanyufei1999@gmail.com\n"
                                          "zhaonanfeng@foxmail.com\n"
                                          "如果您觉得这个软件还不错，可以用支付宝扫描下方二维码支持开发者，万分感谢！\n")
        self.support_qr_code_button.setText("支持开发者，看小哥哥照片")
        self.support_qr_code_button.setIcon(QtGui.QIcon("./zhaonanfeng.jpg"))
        self.support_qr_code_button.setIconSize(QtCore.QSize(500, 500))
        self.support_qr_code_button.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)

        self.help_add_to_window()
        self.help_beautify()

    def help_add_to_window(self):
        self.help_ui_layout.addWidget(self.contact_text_browser, 0, 0, 3, 10)
        self.help_ui_layout.addWidget(self.support_qr_code_button, 3, 0,)
        self.right_widget.addWidget(self.help_ui_widget)

    def help_beautify(self):
        pass


class DecideUi(QMainWindow):
    def __init__(self, s="", unfamiliar_words=[], unknown_words=[],
                 show_context=False, show_english=False, show_chinese=False, show_youdao=False):
        super().__init__()

        self.s = s
        self.unfamiliar_words = unfamiliar_words
        self.unknown_words = unknown_words
        self.new_words = []
        self.old_words = []
        self.temp = []
        self.count = -1
        self.filename = ""
        self.word = Word()

        self.show_context = show_context
        self.show_english = show_english
        self.show_chinese = show_chinese
        self.show_youdao = show_youdao

        self.mark_decide_ui_widget = QWidget()
        self.mark_decide_ui_layout = QGridLayout(self.mark_decide_ui_widget)

        self.mark_up_widget = QWidget()
        self.mark_up_layout = QGridLayout(self.mark_up_widget)

        self.return_button = QPushButton(qta.icon("fa5s.arrow-left", color="black"), "返回")
        self.hint_label = QLabel("还没有开始判断生熟词")
        self.search_button = QPushButton(qta.icon("fa5s.search", color="black"), "搜索")

        self.mark_mid_widget = QWidget()
        self.mark_mid_layout = QGridLayout(self.mark_mid_widget)

        self.word_name_text_edit = QTextEdit()
        self.word_yb_text_edit = QTextEdit()
        self.word_context_text_edit = QTextEdit()
        self.word_ch_text_edit = QTextEdit()
        self.word_en_text_edit = QTextEdit()

        self.last_button = QPushButton(qta.icon("fa5s.angle-left", color="black"), "")
        self.next_button = QPushButton(qta.icon("fa5s.angle-right", color="black"), "")

        self.mark_down_widget = QWidget()
        self.mark_down_layout = QGridLayout(self.mark_down_widget)

        self.progress_bar = QProgressBar()
        self.new_button = QPushButton(qta.icon("fa5s.star", color="black"), "生词")
        self.old_button = QPushButton(qta.icon("fa5s.eye-slash", color="black"), "熟词")

        print("init_ui:" + self.s)
        self.init_ui()

    def init_ui(self):
        self.setBaseSize(960, 700)
        self.setCentralWidget(self.mark_decide_ui_widget)
        self.setWindowTitle("生熟词判断")
        self.mark_decide_ui()
        self.next_one()

    def mark_decide_ui(self):
        # 上方部件：返回按钮、上一个单词状态提示、查询按钮
        self.return_button.setObjectName("up_widget")
        self.return_button.clicked.connect(self.mark_return)

        self.hint_label.setObjectName("up_widget")

        self.search_button.setObjectName("up_widget")
        self.search_button.clicked.connect(self.mark_search)

        # 中部部件：上一个单词、四个框框、下一个单词
        self.last_button.setObjectName("mid_widget")
        self.last_button.clicked.connect(self.last_one)

        self.next_button.setObjectName("mid_widget")
        self.next_button.clicked.connect(self.next_one)

        self.word_name_text_edit.setPlaceholderText("抱歉，无单词名称")
        self.word_name_text_edit.setFontPointSize(36)

        self.word_yb_text_edit.setPlaceholderText("抱歉，未查询到音标")
        self.word_yb_text_edit.setFontPointSize(36)

        self.word_context_text_edit.setPlaceholderText("抱歉，无语境信息")
        self.word_context_text_edit.setFontPointSize(18)

        self.word_en_text_edit.setPlaceholderText("抱歉，未查询到单词英文解释")
        self.word_en_text_edit.setFontPointSize(18)

        self.word_ch_text_edit.setPlaceholderText("抱歉，未查询到单词中文解释")
        self.word_ch_text_edit.setFontPointSize(18)

        # 下部部件：进度条、熟词按钮、生词按钮
        self.progress_bar.setObjectName("down_widget")
        self.progress_bar.setValue(50)
        self.progress_bar.setFixedHeight(3)
        self.progress_bar.setTextVisible(False)
        self.progress_bar.setRange(0, 101)

        self.new_button.setObjectName("down_widget")
        self.new_button.clicked.connect(self.shengci)
        self.new_button.setShortcut('Ctrl+'+chr(32))

        self.old_button.setObjectName("down_widget")
        self.old_button.clicked.connect(self.shuci)
        self.old_button.setShortcut(chr(32))

        self.mark_decide_add_to_window()
        self.mark_decide_beautify()

    def mark_decide_add_to_window(self):
        self.mark_up_layout.addWidget(self.return_button, 0, 0, 1, 1)
        self.mark_up_layout.addWidget(self.hint_label, 0, 1, 1, 10)
        self.mark_up_layout.addWidget(self.search_button, 0, 10, 1, 1)

        self.mark_mid_layout.addWidget(self.last_button, 4, 0, 1, 1)
        self.mark_mid_layout.addWidget(self.next_button, 4, 18, 1, 1)
        self.mark_mid_layout.addWidget(self.word_name_text_edit, 1, 1, 2, 7)
        self.mark_mid_layout.addWidget(self.word_yb_text_edit, 3, 1, 2, 7)
        self.mark_mid_layout.addWidget(self.word_context_text_edit, 6, 1, 6, 7)
        self.mark_mid_layout.addWidget(self.word_en_text_edit, 1, 8, 4, 7)
        self.mark_mid_layout.addWidget(self.word_ch_text_edit, 6, 8, 6, 7)

        self.mark_down_layout.addWidget(self.progress_bar, 0, 0, 1, 18)
        self.mark_down_layout.addWidget(self.new_button, 1, 0, 1, 9)
        self.mark_down_layout.addWidget(self.old_button, 1, 9, 1, 9)

        self.mark_decide_ui_layout.addWidget(self.mark_up_widget, 0, 0, 1, 18)
        self.mark_decide_ui_layout.addWidget(self.mark_mid_widget, 2, 0, 18, 18)
        self.mark_decide_ui_layout.addWidget(self.mark_down_widget, 20, 0, 2, 18)

    def mark_decide_beautify(self):
        self.word_name_text_edit.setStyleSheet(
            '''QTextEdit{
                border-style: outset;
                border-width: 1px; 
                border-radius: 10px;   
                font: bold 24px;
                min-width: 10em;
                padding: 5px;
            }'''
        )
        self.word_yb_text_edit.setStyleSheet(
            '''QTextEdit{
                border-style: outset;
                border-width: 1px; 
                border-radius: 10px;   
                font: bold 24px;
                min-width: 10em;
                padding: 5px;
            }'''
        )
        self.word_en_text_edit.setStyleSheet(
            '''QTextEdit{
                border-style: outset;
                border-width: 1px; 
                border-radius: 10px;   
                font: 14px;
                min-width: 10em;
                padding: 5px;
            }'''
        )
        self.word_ch_text_edit.setStyleSheet(
            '''QTextEdit{
                border-style: outset;
                border-width: 1px; 
                border-radius: 10px;   
                font: 14px;
                min-width: 10em;
                padding: 5px;
            }'''
        )
        self.word_context_text_edit.setStyleSheet(
            '''QTextEdit{
                border-style: outset;
                border-width: 1px; 
                border-radius: 10px;   
                font: 14px;
                min-width: 10em;
                padding: 5px;
            }'''
        )
        self.return_button.setStyleSheet(
            '''QPushButton{
                    border:none;
                    color:black;
            }''')
        self.search_button.setStyleSheet(
            '''QPushButton{
                    border:none;
                    color:black;
            }''')
        self.next_button.setStyleSheet(
            '''QPushButton{
                    border:none;
                    color:black;
            }''')
        self.last_button.setStyleSheet(
            '''QPushButton{
                    border:none;
                    color:black;
            }''')
        self.new_button.setStyleSheet(
            '''QPushButton{
                    border-style: outset;
                    border-width:2px;
                    border-radius:10px;
                    border-color: black;
                    font: bold 14px;
                    min-width:10em;
                    padding:6px;
            }''')
        self.old_button.setStyleSheet(
            '''QPushButton{
                    border-style: outset;
                    border-width:2px;
                    border-radius:10px;
                    border-color: black;
                    font: bold 14px;
                    min-width:10em;
                    padding:6px;
            }''')

    def closeEvent(self, event):
        res = QtWidgets.QMessageBox.question(self, '警告',
                                         "你要确定退出吗？", QtWidgets.QMessageBox.Yes |
                                         QtWidgets.QMessageBox.No,
                                         QtWidgets.QMessageBox.Yes)
        if res == QtWidgets.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def output(self):
        res = QMessageBox.question(self, '提示',
                                             "单词列表已保存至桌面\n"
                                             "仍然有一些Bug，请谅解:)\n"
                                             "持续开发中:)您可以联系开发者提供反馈意见\n"
                                             "yuanyufei1999@gmail.com\n"
                                             "zhaonanfeng@foxmail.com", QMessageBox.Yes |
                                             QMessageBox.No,
                                             QMessageBox.Yes)
        if res == QMessageBox.Yes:
            self.mark_return()

        else:
            pass

    def mark_return(self):
        self.close()

    def mark_search(self):
        self.word = Word(self.word_name_text_edit.toPlainText())
        self.word_yb_text_edit.setPlainText(self.word.get_yb(True))
        self.word_context_text_edit.setPlainText(self.word.get_context(True))
        self.word_ch_text_edit.setPlainText(self.word.get_str_ch_interpretation(True))
        self.word_en_text_edit.setPlainText(self.word.get_str_en_interpretation(True))

    def last_one(self):
        self.count -= 1
        try:
            self.progress_bar.setValue(100.0 * float(self.count) / float(len(self.unknown_words)))
        except ZeroDivisionError:
            return 0
        if self.count < 0:
            self.count += 1
        else:
            self.display()

    def next_one(self):
        self.count += 1
        try:
            self.progress_bar.setValue(100.0 * float(self.count) / float(len(self.unknown_words)))
        except ZeroDivisionError:
            self.show_dialog("该文本中没有未知词")
            return 0
        if self.count >= len(self.unknown_words):
            self.show_dialog()
            self.count -= 1
        else:
            self.display()

    def shengci(self):
        self.hint_label.setText("上一个单词为" + self.word_name_text_edit.toPlainText() + "已被判断为生词")
        text = self.word_name_text_edit.toPlainText()

        if text not in self.temp:
            self.word = Word(name=self.word_name_text_edit.toPlainText(),
                             yb=self.word_yb_text_edit.toPlainText(),
                             context=self.word_context_text_edit.toPlainText(),
                             ch_interpretation=self.word_ch_text_edit.toPlainText(),
                             en_interpretation=self.word_en_text_edit.toPlainText())
            self.new_words.append(self.word)
            self.temp.append(self.word.get_name())
        self.next_one()

    def shuci(self):
        text = self.word_name_text_edit.toPlainText()
        self.hint_label.setText("上一个单词为" + text + "已被判断为熟词")
        if text not in self.old_words:
            self.old_words.append(self.word.get_name())
        self.next_one()

    def finish(self):
        update_familiar_words(old_words=self.old_words)
        update_vocabulary_words(new_words=self.new_words)
        third(self.unfamiliar_words + self.new_words,
              self.filename,
              self.show_context,
              self.show_english,
              self.show_chinese)
        self.output()

    def show_dialog(self, text="提示"):
        text, ok = QtWidgets.QInputDialog.getText(self, text, '生熟词已判断完毕，请输入文件名:')

        if ok:
            self.filename = str(text)
            f = open("./input/" + self.filename + ".txt", mode="w+",
                     encoding="UTF-8")
            f.write(self.s)
            f.close()
            self.finish()
            return True
        return False

    def display(self, flag=False):
        QApplication.processEvents()
        self.word = self.unknown_words[self.count]
        self.word_name_text_edit.setPlainText(self.word.get_name())
        self.word_yb_text_edit.setPlainText(self.word.get_yb(flag))
        # self.word_context_text_edit.setPlainText(self.word.get_str_context())
        self.word_context_text_edit.setPlainText(self.word.get_context(self.show_youdao))
        self.word_ch_text_edit.setPlainText(self.word.get_str_ch_interpretation(flag))
        self.word_en_text_edit.setPlainText(self.word.get_str_en_interpretation(flag))
        QApplication.processEvents()

    def closeEvent(self, event):
        res = QMessageBox.question(self, '警告',
                                         "你要确定退出吗？", QtWidgets.QMessageBox.Yes |
                                         QtWidgets.QMessageBox.No,
                                         QtWidgets.QMessageBox.Yes)
        if res == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


class ReciteUi(QMainWindow):
    def __init__(self, word_count=0):
        super().__init__()
        self.word_count = word_count
        self.words = []
        self.random = 0
        self.count = 0
        self.guess_count = 0
        self.right_words = []

        self.recite_ui_in_widget = QWidget()
        self.recite_ui_in_layout = QGridLayout(self.recite_ui_in_widget)

        self.last_button = QPushButton(qta.icon("fa5s.angle-left", color="black"), "")
        self.next_button = QPushButton(qta.icon("fa5s.angle-right", color="black"), "")
        self.word_line_edit = QLineEdit("Word")
        self.word_line_edit.returnPressed.connect(self.recite_ensure)
        self.yb_text_edit = QTextEdit("Phonetic Symbol")
        self.context_text_edit = QTextEdit("Context")
        self.english_text_edit = QTextEdit("English Interpretation")
        self.chinese_text_edit = QTextEdit("Chinese Interpretation")
        self.ensure_button = QPushButton("确认")
        self.ensure_shuci_button = QPushButton("熟词")

        self.init_ui()

    def init_ui(self):
        self.setBaseSize(960, 700)
        self.setCentralWidget(self.recite_ui_in_widget)
        self.setWindowTitle("单词背诵")
        self.recite_word_get()
        self.recite_response_ui()
        self.recite_next_one()

    def recite_response_ui(self):
        self.recite_add_to_window()

        self.last_button.clicked.connect(self.recite_last_one)
        self.next_button.clicked.connect(self.recite_next_one)
        self.ensure_button.clicked.connect(self.recite_ensure)
        self.ensure_shuci_button.clicked.connect(self.shuci_ensure)

        self.recite_beautify()

    def shuci_ensure(self):
        word = self.words[self.random]
        self.words.remove(word)
        self.right_words.append(word.get_name())
        self.recite_next_one()

    def word_display(self):
        word = self.words[self.random]
        self.word_line_edit.setText(word.get_name())

    def english_display(self):
        word = self.words[self.random]
        if word.get_str_en_interpretation() is "":
            self.count -= 1
            self.recite_next_one()
        self.english_text_edit.setText(word.get_str_en_interpretation() if word.get_str_en_interpretation() is not "" else "抱歉，此单词无英文解释")

    def context_display(self):
        word = self.words[self.random]
        self.context_text_edit.setText(re.sub(word.get_name(), '_' * len(word.get_name()), word.get_context()) if word.get_context() is not "" else "抱歉，此单词无例句")

    def chinese_display(self):
        word = self.words[self.random]
        self.chinese_text_edit.setText(word.get_str_ch_interpretation() if word.get_str_ch_interpretation() is not "" else "抱歉，此单词无中文解释")

    def yb_display(self):
        word = self.words[self.random]
        self.yb_text_edit.setText(word.get_yb() if word.get_yb() is not "" else "抱歉，此单词无音标")

    def random_get(self):
        try:
            self.random = random.randint(0, len(self.words)-1)
        except ValueError:
            self.close()

    def recite_word_get(self):
        with open("./vocabulary/vocabulary_words.txt", "r+", encoding="UTF-8") as f:
            for sentence in f.readlines():
                if not sentence[0].isalpha():
                    continue
                text = sentence.strip().split("----")
                word = Word(name=text[0], yb=text[1], context=text[2])
                word.set_en_interpretation(re.split("[)(1-9]+", text[3]))
                word.set_ch_interpretation(re.split("[)(1-9]+", text[4]))
                self.words.append(word)

    def recite_ensure(self):
        self.guess_count += 1
        word = self.words[self.random]
        if self.word_line_edit.text() == word.get_name():
            self.niubi_dialog()
        else:
            self.laji_dialog()

    def laji_dialog(self):
        res = QMessageBox.information(self, '提示',
                                      "好可惜啊，就差一点点了，再试一次呗！", QtWidgets.QMessageBox.Yes |
                                      QtWidgets.QMessageBox.No,
                                      QtWidgets.QMessageBox.Yes)
        if res == QMessageBox.Yes:
            if self.guess_count == 1:
                self.context_display()
            elif self.guess_count == 2:
                self.chinese_display()
            elif self.guess_count == 3:
                self.yb_display()
            elif self.guess_count == 4:
                self.word_display()
        else:
            self.context_display()

    def niubi_dialog(self):
        res = QMessageBox.information(self, '提示',
                                      "厉害啊，你答对了耶！", QtWidgets.QMessageBox.Yes |
                                      QtWidgets.QMessageBox.No,
                                      QtWidgets.QMessageBox.Yes)
        if res == QMessageBox.Yes:
            word = self.words[self.random]
            if self.guess_count == 1:
                self.right_words.append(word.get_name())
                self.words.remove(word)
                if len(self.words) == 0:
                    self.show_dialog()
                self.recite_next_one()
            else:
                self.recite_next_one()
                # word.count_plus()

        else:
            return 0

    def recite_next_one(self):
        self.word_line_edit.clear()
        self.english_text_edit.clear()
        self.context_text_edit.clear()
        self.chinese_text_edit.clear()
        self.yb_text_edit.clear()
        self.guess_count = 0
        self.count += 1
        self.random_get()
        if self.count > self.word_count:
            self.show_dialog()
            self.count -= 1
        else:
            self.english_display()

    def show_dialog(self, text="提示"):
        res = QMessageBox.information(self, '提示',
                                   "你已经背完了" + str(self.word_count) + "个单词啦，买包辣条奖励一下自己吧！", QtWidgets.QMessageBox.Yes |
                                   QtWidgets.QMessageBox.No,
                                   QtWidgets.QMessageBox.Yes)
        if res == QMessageBox.Yes:
            self.make_close()
        else:
            return 0

    def make_close(self):
        with open("./familiar/familiar_words.txt", "a+", encoding="UTF-8") as f:
            f.writelines(["\n" + i for i in self.right_words])
        with open("./vocabulary/vocabulary_words.txt", "w+", encoding="UTF-8") as ff:
            ff.writelines(["\n" + i.to_string() for i in self.words])
        self.close()

    def closeEvent(self, event):
        res = QtWidgets.QMessageBox.question(self, '警告',
                                             "你要确定退出吗？", QtWidgets.QMessageBox.Yes |
                                             QtWidgets.QMessageBox.No,
                                             QtWidgets.QMessageBox.Yes)
        if res == QtWidgets.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def recite_last_one(self):
        self.count -= 1
        if self.count < 0:
            self.count += 1
        else:
            self.english_display()

    def recite_add_to_window(self):

        self.recite_ui_in_layout.addWidget(self.last_button, 8, 0, 1, 1)
        self.recite_ui_in_layout.addWidget(self.next_button, 8, 11, 1, 1)
        self.recite_ui_in_layout.addWidget(self.ensure_button, 0, 10, 1, 1)

        self.recite_ui_in_layout.addWidget(self.word_line_edit, 0, 1, 2, 9)
        self.recite_ui_in_layout.addWidget(self.english_text_edit, 2, 1, 5, 10)
        self.recite_ui_in_layout.addWidget(self.context_text_edit, 7, 1, 2, 10)
        self.recite_ui_in_layout.addWidget(self.chinese_text_edit, 9, 1, 3, 10)
        self.recite_ui_in_layout.addWidget(self.yb_text_edit, 12, 1, 1, 10)
        self.recite_ui_in_layout.addWidget(self.ensure_shuci_button, 13, 1, 1, 10)

    def recite_beautify(self):
        self.ensure_shuci_button.setStyleSheet(
            '''QPushButton{
                    border-style: outset;
                    border-width:2px;
                    border-radius:10px;
                    border-color: black;
                    font: bold 14px;
                    min-width:10em;
                    padding:6px;
            }''')
        self.last_button.setStyleSheet(
            '''QPushButton{
                    border:none;
                    color:black;
            }''')
        self.next_button.setStyleSheet(
            '''QPushButton{
                    border:none;
                    olor:black;
            }''')

def main():
    app = QApplication(sys.argv)
    gui = MainUi()
    gui.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
