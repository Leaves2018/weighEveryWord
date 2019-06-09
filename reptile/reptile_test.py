# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
import sys
import qtawesome as qta
from vocabulary import Word
import re
from weigh2 import *


class MainUi(QMainWindow):
    def __init__(self):
        super().__init__()
        self.unfamiliar_words = []
        self.unknown_words = []
        self.s = ""
        self.dui = None
        self.rui = None
        self.word_count = 0

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
        self.recite_ui_layout = QGridLayout(self.recite_ui_widget)

        self.word_count_question_label = QLabel("你今天想背几个单词呀？")
        self.word_count_text_edit = QTextEdit()
        self.word_recite_button = QPushButton("开始背单词")
        # self.test_label_2 = QLabel("这里是背诵页面")

        # 3.3 "查询"页面：look_up_ui
        self.look_up_ui_widget = QWidget()
        self.look_up_ui_layout = QGridLayout(self.look_up_ui_widget)

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
        self.word_text_edit = QTextEdit("Word")
        self.yb_text_edit = QTextEdit("Phonetic Symbol")
        self.context_text_edit = QTextEdit("Context")
        self.english_text_edit = QTextEdit("English Interpretation")
        self.chinese_text_edit = QTextEdit("Chinese Interpretation")

        # 3.4 "设置"页面：settings_ui
        self.settings_ui_widget = QWidget()
        self.settings_ui_layout = QGridLayout(self.settings_ui_widget)
        self.test_label_shuci = QLabel("设置熟词")
        self.shuci_xiaoxue_checkbox = QCheckBox('小学词汇')
        self.shuci_chuzhong_checkbox = QCheckBox('初中词汇')
        self.shuci_gaozhong_checkbox = QCheckBox('高中词汇')
        self.shuci_siliuji_checkbox = QCheckBox('英语CET4、6词汇')

        self.test_label_goal = QLabel("学习目标")
        self.goal_IELTS_checkbox = QCheckBox('雅思词汇')
        self.goal_TOEFL_checkbox = QCheckBox('托福词汇')

        self.test_label_output = QLabel("输出样式")
        self.sample_output_button_1 = QToolButton()
        self.sample_output_button_1.setText("样式1")  # 设置按钮文本
        self.sample_output_button_1.setIcon(QtGui.QIcon('./r1.jpg'))  # 设置按钮图标
        self.sample_output_button_1.setIconSize(QtCore.QSize(100, 100))  # 设置图标大小
        self.sample_output_button_1.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)

        self.sample_output_button_2 = QToolButton()
        self.sample_output_button_2.setText("样式2")  # 设置按钮文本
        self.sample_output_button_2.setIcon(QtGui.QIcon('./r1.jpg'))  # 设置按钮图标
        self.sample_output_button_2.setIconSize(QtCore.QSize(100, 100))  # 设置图标大小
        self.sample_output_button_2.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)

        self.sample_output_button_3 = QToolButton()
        self.sample_output_button_3.setText("样式3")  # 设置按钮文本
        self.sample_output_button_3.setIcon(QtGui.QIcon('./r1.jpg'))  # 设置按钮图标
        self.sample_output_button_3.setIconSize(QtCore.QSize(100, 100))  # 设置图标大小
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

    def on_look_up_ui_clicked(self):
        self.right_widget.setCurrentIndex(2)

    def on_settings_ui_clicked(self):
        self.right_widget.setCurrentIndex(3)

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
            self.test_dialog_1()
        else:
            self.test_dialog_2()

    def test_dialog_1(self):
        res = QtWidgets.QMessageBox.question(self, '提示',
                                             "已接收到文本，初步处理完毕。\n"
                                             "请快速浏览并手动修改不合理的分词:)\n"
                                             , QtWidgets.QMessageBox.Yes |
                                             QtWidgets.QMessageBox.No,
                                             QtWidgets.QMessageBox.No)
        if res == QtWidgets.QMessageBox.Yes:
            pass
        else:
            pass

    def test_dialog_2(self):
        res = QtWidgets.QMessageBox.question(self, '提示',
                                             "未接收到文本，请确认输入正确", QtWidgets.QMessageBox.Yes |
                                             QtWidgets.QMessageBox.No,
                                             QtWidgets.QMessageBox.No)
        if res == QtWidgets.QMessageBox.Yes:
            pass
        else:
            pass

    def mark_start(self):
        res = QtWidgets.QMessageBox.question(self, '提示',
                                             "文本已确认完毕？", QtWidgets.QMessageBox.Yes |
                                             QtWidgets.QMessageBox.No)
        if res == QtWidgets.QMessageBox.Yes:
            self.unfamiliar_words, self.unknown_words = first(self.s)
            print("mark_start:" + self.s)
            self.dui = DecideUi(s=self.s, unfamiliar_words=self.unfamiliar_words, unknown_words=self.unknown_words)
            self.dui.show()
        else:
            return 0

    def mark_beautify(self):
        pass

    def recite_ui(self):
        self.word_recite_button.clicked.connect(self.recite_start)

        self.recite_add_to_window()
        self.recite_beautify()

    def recite_start(self):
        try:
            self.word_count = int(self.word_count_text_edit.toPlainText())
        except ValueError:
            res = QtWidgets.QMessageBox.information(self, '提示，您输入的不是数字',
                                                    "请重新输入要背的单词数目（以阿拉伯数字形式）", QtWidgets.QMessageBox.Yes |
                                                    QMessageBox.No)
            if res == QtWidgets.QMessageBox.Yes:
                return 0
            else:
                return 0
        finally:
            self.word_count_text_edit.clear()

        res = QtWidgets.QMessageBox.question(self, '提示',
                                             "确认就背这" + str(self.word_count) + "个单词吗？", QtWidgets.QMessageBox.Yes |
                                             QMessageBox.No)
        if res == QtWidgets.QMessageBox.Yes:
            self.rui = ReciteUi(word_count=self.word_count)
            self.rui.show()
        else:
            return 0

    def recite_add_to_window(self):
        self.right_widget.addWidget(self.recite_ui_widget)
        self.recite_ui_layout.addWidget(self.word_count_question_label, 0, 0, 1, 10)
        self.recite_ui_layout.addWidget(self.word_count_text_edit, 1, 0, 1, 8)
        self.recite_ui_layout.addWidget(self.word_recite_button, 1, 8, 1, 2)

    def recite_beautify(self):
        pass

    def look_up_ui(self):
        # 搜索模块
        self.right_bar_widget.setLayout(self.right_bar_layout)
        self.search_line_edit.setPlaceholderText("输入单词后按回车进行查询")
        # 实现在搜索输入框中按回车进行搜索
        self.search_line_edit.returnPressed.connect(self.look_up_search)
        # 设置搜索按钮的点击事件
        self.search_button.clicked.connect(self.look_up_search)

        # 单词模块
        self.right_word_widget.setObjectName("right_word_widget")
        self.right_word_widget.setLayout(self.right_word_layout)

        self.look_up_add_to_window()
        self.look_up_beautify()

    # 搜索按钮点击事件
    def look_up_search(self):
        text = self.search_line_edit.text()
        word = Word(text)
        self.word_text_edit.setText(word.get_name())
        self.yb_text_edit.setText(word.get_yb())
        self.context_text_edit.setText(word.get_context())
        self.english_text_edit.setText(word.get_en_interpretation())
        self.chinese_text_edit.setText(word.get_ch_interpretation())

    # 将各个部件添加到窗口
    def look_up_add_to_window(self):
        self.right_widget.addWidget(self.look_up_ui_widget)

        self.look_up_ui_layout.addWidget(self.right_bar_widget, 0, 0, 1, 9)
        self.look_up_ui_layout.addWidget(self.right_word_widget, 1, 0, 11, 10)

        # 向搜索模块添加搜索Label和搜索框LineEdit
        self.right_bar_layout.addWidget(self.search_line_edit, 0, 0, 1, 8)
        self.right_bar_layout.addWidget(self.search_button, 0, 9, 1, 1)

        # 向单词模块添加单词Label、音标Label、语境Label、英解Label、中解Label
        self.right_word_layout.addWidget(self.word_text_edit, 0, 0, 3, 10)
        self.right_word_layout.addWidget(self.yb_text_edit, 3, 0, 1, 10)
        self.right_word_layout.addWidget(self.context_text_edit, 4, 0, 2, 10)
        self.right_word_layout.addWidget(self.english_text_edit, 6, 0, 3, 10)
        self.right_word_layout.addWidget(self.chinese_text_edit, 9, 0, 3, 10)

        self.look_up_ui_layout.addWidget(self.right_bar_widget, 0, 0, 1, 9)
        self.look_up_ui_layout.addWidget(self.right_word_widget, 1, 0, 11, 10)

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

    def settings_ui(self):
        self.

        self.settings_add_to_window()
        self.settings_beautify()

    def settings_add_to_window(self):
        self.settings_ui_layout.addWidget(self.test_label_4, 0, 0, )
        self.right_widget.addWidget(self.settings_ui_widget)

    def settings_beautify(self):
        pass

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
        self.help_ui_layout.addWidget(self.support_qr_code_button, 3, 0, )
        self.right_widget.addWidget(self.help_ui_widget)

    def help_beautify(self):
        pass


class DecideUi(QMainWindow):
    def __init__(self, s="", unfamiliar_words=[], unknown_words=[]):
        super().__init__()

        self.s = s
        self.unfamiliar_words = unfamiliar_words
        self.unknown_words = unknown_words
        self.new_words = []
        self.old_words = []
        self.temp = []
        self.count = -1
        self.filename = ""

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

    # def receive(self, s="", unfamiliar_words=[], unknown_words=[]):
    #     self.s = s
    #     self.unfamiliar_words = unfamiliar_words
    #     self.unknown_words = unknown_words

    def init_ui(self):
        self.setFixedSize(960, 700)
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
        self.new_button.setShortcut('Ctrl+' + chr(32))

        self.old_button.setObjectName("down_widget")
        self.old_button.clicked.connect(self.shuci)
        self.old_button.setShortcut(chr(32))

        self.mark_decide_add_to_window()
        self.mark_decide_beautify()

    def mark_decide_add_to_window(self):
        self.mark_up_layout.addWidget(self.return_button, 0, 0, 1, 1)
        self.mark_up_layout.addWidget(self.hint_label, 0, 1, 1, 10)
        self.mark_up_layout.addWidget(self.search_button, 0, 10, 1, 1)

        self.mark_mid_layout.addWidget(self.last_button, 9, 0, 1, 1)
        self.mark_mid_layout.addWidget(self.next_button, 9, 18, 1, 1)
        self.mark_mid_layout.addWidget(self.word_name_text_edit, 1, 1, 4, 7)
        self.mark_mid_layout.addWidget(self.word_context_text_edit, 6, 1, 6, 7)
        self.mark_mid_layout.addWidget(self.word_ch_text_edit, 1, 8, 4, 7)
        self.mark_mid_layout.addWidget(self.word_en_text_edit, 6, 8, 6, 7)

        self.mark_down_layout.addWidget(self.progress_bar, 0, 0, 1, 18)
        self.mark_down_layout.addWidget(self.new_button, 1, 0, 1, 9)
        self.mark_down_layout.addWidget(self.old_button, 1, 9, 1, 9)

        self.mark_decide_ui_layout.addWidget(self.mark_up_widget, 0, 0, 1, 18)
        self.mark_decide_ui_layout.addWidget(self.mark_mid_widget, 2, 0, 18, 18)
        self.mark_decide_ui_layout.addWidget(self.mark_down_widget, 20, 0, 2, 18)

    def mark_decide_beautify(self):
        pass

    def closeEvent(self, event):
        res = QtWidgets.QMessageBox.question(self, '警告',
                                             "你要确定退出吗？", QtWidgets.QMessageBox.Yes |
                                             QtWidgets.QMessageBox.No,
                                             QtWidgets.QMessageBox.No)
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
                                   QMessageBox.No)
        if res == QMessageBox.Yes:
            self.mark_return()

        else:
            pass

    def mark_return(self):
        self.close()

    def mark_search(self):
        word = Word(self.word_name_text_edit.toPlainText())
        self.word_name_text_edit.setPlainText(word.get_name())
        self.word_context_text_edit.setPlainText(word.get_context(True))
        self.word_ch_text_edit.setPlainText(word.get_ch_interpretation(True))
        self.word_en_text_edit.setPlainText(word.get_en_interpretation(True))

    def last_one(self):
        self.count -= 1
        self.progress_bar.setValue(100.0 * self.count / len(self.unknown_words))
        if self.count < 0:
            self.count += 1
        else:
            self.display()

    def next_one(self):
        self.count += 1
        try:
            self.progress_bar.setValue(100.0 * self.count / len(self.unknown_words))
        except ZeroDivisionError:
            self.show_dialog("该文本中没有未知词")
        if self.count >= len(self.unknown_words):
            self.show_dialog()
            self.count -= 1
        else:
            self.display()

    def shengci(self):
        self.hint_label.setText("上一个单词为" + self.word_name_text_edit.toPlainText() + "已被判断为生词")
        text = self.word_name_text_edit.toPlainText()

        if text not in self.temp:
            word = Word(name=self.word_name_text_edit.toPlainText(), context=self.word_context_text_edit.toPlainText(),
                        ch_interpretation=self.word_ch_text_edit.toPlainText(),
                        en_interpretation=self.word_en_text_edit.toPlainText())
            self.new_words.append(word)
            self.temp.append(text)
        self.next_one()

    def shuci(self):
        text = self.word_name_text_edit.toPlainText()
        self.hint_label.setText("上一个单词为" + text + "已被判断为熟词")
        if text not in self.old_words:
            self.old_words.append(text)
        self.next_one()

    def finish(self):
        update_familiar_words(old_words=self.old_words)
        update_vocabulary_words(new_words=self.new_words)
        third(self.unfamiliar_words + self.new_words, self.filename)
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

    def display(self):
        QApplication.processEvents()
        word = self.unknown_words[self.count]
        self.word_name_text_edit.setPlainText(word.get_name())
        self.word_context_text_edit.setPlainText(word.get_context())
        self.word_ch_text_edit.setPlainText(word.get_ch_interpretation())
        self.word_en_text_edit.setPlainText(word.get_en_interpretation())
        QApplication.processEvents()

    def closeEvent(self, event):
        res = QMessageBox.question(self, '警告',
                                   "你要确定退出吗？", QtWidgets.QMessageBox.Yes |
                                   QtWidgets.QMessageBox.No,
                                   QtWidgets.QMessageBox.No)
        if res == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


class ReciteUi(QMainWindow):
    def __init__(self, word_count=0):
        super().__init__()
        self.word_count = word_count

        self.recite_ui_in_widget = QWidget()
        self.recite_ui_in_layout = QGridLayout(self.recite_ui_in_widget)

        self.last_button = QPushButton(qta.icon("fa5s.angle-left", color="black"), "")
        self.next_button = QPushButton(qta.icon("fa5s.angle-right", color="black"), "")
        self.word_text_edit = QTextEdit("Word")
        self.yb_text_edit = QTextEdit("Phonetic Symbol")
        self.context_text_edit = QTextEdit("Context")
        self.english_text_edit = QTextEdit("English Interpretation")
        self.chinese_text_edit = QTextEdit("Chinese Interpretation")
        self.ensure_button = QPushButton("确认")

        self.init_ui()

    def init_ui(self):
        self.setFixedSize(960, 700)
        self.setCentralWidget(self.recite_ui_in_widget)
        self.setWindowTitle("单词背诵")
        self.recite_response_ui()
        self.recite_next_one()

    def recite_response_ui(self):
        self.recite_add_to_window()

        self.last_button.clicked.connect(self.recite_last_one)
        self.next_button.clicked.connect(self.recite_next_one)
        self.ensure_button.clicked.connect(self.recite_ensure)

        self.recite_beautify()

    def recite_ensure(self):
        pass

    def recite_next_one(self):
        pass

    def recite_last_one(self):
        pass

    def recite_add_to_window(self):
        self.recite_ui_in_layout.addWidget(self.last_button, 4, 0, 1, 1)
        self.recite_ui_in_layout.addWidget(self.next_button, 4, 11, 1, 1)
        self.recite_ui_in_layout.addWidget(self.ensure_button, 0, 10, 1, 1)

        self.recite_ui_in_layout.addWidget(self.word_text_edit, 0, 1, 2, 9)
        self.recite_ui_in_layout.addWidget(self.yb_text_edit, 1, 1, 2, 10)
        self.recite_ui_in_layout.addWidget(self.context_text_edit, 2, 1, 2, 10)
        self.recite_ui_in_layout.addWidget(self.english_text_edit, 3, 1, 5, 10)
        self.recite_ui_in_layout.addWidget(self.chinese_text_edit, 7, 1, 3, 10)

    def recite_beautify(self):
        pass


def main():
    app = QApplication(sys.argv)
    gui = MainUi()
    gui.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
