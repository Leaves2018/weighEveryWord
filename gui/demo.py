from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import qtawesome
from weigh2 import *
from vocabulary import Word


class MainInter(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        self.init_ui()
        self.old_words = []
        self.unknown_words = []
        self.new_words = []
        self.count = -1
        self.filename = ""

    # 文本输入窗口
    def init_ui(self):
        # 窗口主部件：创建、创建网格布局、设置主部件布局
        self.setFixedSize(960, 700) # 设置窗口大小
        self.main_widget = QtWidgets.QWidget()  # 创建窗口主部件
        self.main_layout = QtWidgets.QGridLayout()  # 创建主部件的网格布局
        self.main_widget.setLayout(self.main_layout)  # 设置窗口主部件布局为网格布局
        # 上方部件：文本输入框
        self.up_widget = QtWidgets.QWidget()  # 创建上方部件
        self.up_widget.setObjectName('up_widget')
        self.up_layout = QtWidgets.QGridLayout()  # 创建上方部件的网格布局层
        self.up_widget.setLayout(self.up_layout)  # 设置上方部件布局为网格
        # 下方部件：清空、确认按钮
        self.down_widget = QtWidgets.QWidget()  # 创建下方部件
        self.down_widget.setObjectName('down_widget')
        self.down_layout = QtWidgets.QGridLayout()
        self.down_widget.setLayout(self.down_layout)  # 设置下方部件布局为网格

        # 将上方部件、下方部件添加到窗口主部件
        self.main_layout.addWidget(self.up_widget, 0, 0, 18, 18)  # 上方部件在第0行第0列，占18行18列
        self.main_layout.addWidget(self.down_widget, 19, 0, 2, 18)  # 上方部件在第19行第0列，占2行18列
        self.setCentralWidget(self.main_widget)  # 设置窗口主部件

        # 设置上方部件属性
        self.widget_text_input = QtWidgets.QWidget()  # 上方顶部文本输入框部件
        self.layout_text_input = QtWidgets.QGridLayout()  # 上方顶部文本输入框网格布局
        self.widget_text_input.setLayout(self.layout_text_input)
        self.up_bar_widget_input = QtWidgets.QTextEdit()
        self.up_bar_widget_input.setPlaceholderText("输入要标记的文本")

        self.layout_text_input.addWidget(self.up_bar_widget_input, 0, 1, 18, 18)
        self.up_layout.addWidget(self.widget_text_input, 0, 0, 1, 9)

        self.btn_clear = QtWidgets.QPushButton("清空")
        self.btn_clear.setObjectName('down_button')
        self.btn_clear.setCheckable(True)
        self.btn_clear.toggle()
        self.btn_clear.clicked.connect(self.clear)

        self.btn_confirm = QtWidgets.QPushButton("确认文本")
        self.btn_confirm.setObjectName('down_button')
        self.btn_confirm.setCheckable(True)
        self.btn_confirm.toggle()
        self.btn_confirm.clicked.connect(self.get)

        self.btn_confirm_again = QtWidgets.QPushButton("下一步")
        self.btn_confirm_again.setObjectName('down_button')
        self.btn_confirm_again.setCheckable(True)
        self.btn_confirm_again.toggle()
        self.btn_confirm_again.clicked.connect(self.openNext)

        self.down_layout.addWidget(self.btn_clear, 0, 0, 1, 3)
        self.down_layout.addWidget(self.btn_confirm, 0, 3, 1, 3)
        self.down_layout.addWidget(self.btn_confirm_again, 0, 6, 1, 3)

    # 决策窗口
    def decide(self):
        self.setFixedSize(960, 700)
        self.main_widget = QtWidgets.QWidget()  # 创建窗口主部件
        self.main_layout = QtWidgets.QGridLayout()  # 创建主部件的网格布局
        self.main_widget.setLayout(self.main_layout)  # 设置窗口主部件布局为网格布局

        self.up_widget = QtWidgets.QWidget()  # 创建上方部件
        self.up_widget.setObjectName('up_widget')
        self.up_layout = QtWidgets.QGridLayout()  # 创建上方部件的网格布局层
        self.up_widget.setLayout(self.up_layout)  # 设置上方部件布局为网格

        self.down_widget = QtWidgets.QWidget()  # 创建下方部件
        self.down_widget.setObjectName('down_widget')
        self.down_layout = QtWidgets.QGridLayout()
        self.down_widget.setLayout(self.down_layout)  # 设置下方部件布局为网格

        self.down_process_bar = QtWidgets.QProgressBar()  # 播放进度部件
        self.down_process_bar.setValue(49)
        self.down_process_bar.setFixedHeight(3)  # 设置进度条高度
        self.down_process_bar.setTextVisible(False)  # 不显示进度条文字
        self.down_layout.addWidget(self.down_process_bar, 0, 0, 1, 18)

        self.main_layout.addWidget(self.up_widget, 0, 0, 18, 18)  # 上方部件在第0行第0列，占18行18列
        self.main_layout.addWidget(self.down_widget, 19, 0, 2, 18)  # 上方部件在第19行第0列，占2行18列
        self.setCentralWidget(self.main_widget)  # 设置窗口主部件

        self.up_button_1 = QtWidgets.QPushButton(qtawesome.icon('fa.music', color='white'), "上一个")
        self.up_button_1.setObjectName('left_button')
        self.up_button_1.setCheckable(True)
        self.up_button_1.toggle()
        self.up_button_1.clicked.connect(self.last_one)

        self.up_button_2 = QtWidgets.QPushButton(qtawesome.icon('fa.sellsy', color='white'), "下一个")
        self.up_button_2.setObjectName('left_button')
        self.up_button_2.setCheckable(True)
        self.up_button_2.toggle()
        self.up_button_2.clicked.connect(self.next_one)

        self.up_button_return = QtWidgets.QPushButton(qtawesome.icon('fa.music', color='white'), "返回")
        self.up_button_return.setObjectName('left_button')
        self.up_button_return.setCheckable(True)
        self.up_button_return.toggle()
        self.up_button_return.clicked.connect(self.init_ui)

        self.up_layout.addWidget(self.up_button_1, 9, 0, 1, 1)
        self.up_layout.addWidget(self.up_button_2, 9, 18, 1, 1)
        self.up_layout.addWidget(self.up_button_return, 0, 0, 1, 1)

        self.widget_text_input = QtWidgets.QWidget()  # 上方顶部部件
        self.layout_text_input = QtWidgets.QGridLayout()  # 上方顶部网格布局
        self.widget_text_input.setLayout(self.layout_text_input)

        self.word_name_output = QtWidgets.QTextEdit()
        self.word_name_output.setPlaceholderText("单词名称")
        self.layout_text_input.addWidget(self.word_name_output, 0, 1, 3, 6)

        self.word_ch_output = QtWidgets.QTextEdit()
        self.word_ch_output.setPlaceholderText("中文解释")
        self.layout_text_input.addWidget(self.word_ch_output, 0, 8, 3, 6)

        self.word_context_output = QtWidgets.QTextEdit()
        self.word_context_output.setPlaceholderText("语境信息")
        self.layout_text_input.addWidget(self.word_context_output, 5, 1, 5, 6)

        self.word_en_output = QtWidgets.QTextEdit()
        self.word_en_output.setPlaceholderText("英文解释")
        self.layout_text_input.addWidget(self.word_en_output, 5, 8, 5, 6)
        self.up_layout.addWidget(self.widget_text_input, 0, 1, 18, 17)

        self.btn_clear = QtWidgets.QPushButton("生词")
        self.btn_clear.setObjectName('down_button')
        self.btn_clear.setCheckable(True)
        self.btn_clear.toggle()
        self.btn_clear.clicked.connect(self.choose_familiar)

        self.btn_confirm = QtWidgets.QPushButton("熟词")
        self.btn_confirm.setObjectName('down_button')
        self.btn_confirm.setCheckable(True)
        self.btn_confirm.toggle()
        self.btn_confirm.clicked.connect(self.choose_vocabulary)

        self.down_layout.addWidget(self.btn_clear, 1, 0, 1, 9)
        self.down_layout.addWidget(self.btn_confirm, 1, 9, 1, 9)

    # 点击系统自带的"关闭"按钮时响应
    def closeEvent(self, event):
        res = QtWidgets.QMessageBox.question(self, '警告',
                                         "你要确定退出吗？", QtWidgets.QMessageBox.Yes |
                                         QtWidgets.QMessageBox.No,
                                         QtWidgets.QMessageBox.No)
        if res == QtWidgets.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def openNext(self, event):
        res = QtWidgets.QMessageBox.question(self, '提示',
                                         "文本已输入完毕？", QtWidgets.QMessageBox.Yes |
                                         QtWidgets.QMessageBox.No,
                                         QtWidgets.QMessageBox.No)
        if res == QtWidgets.QMessageBox.Yes:
            self.decide()
        else:
            return 0

    def output(self):
        res = QtWidgets.QMessageBox.question(self, '提示',
                                             "单词列表已保存至桌面", QtWidgets.QMessageBox.Yes |
                                             QtWidgets.QMessageBox.No,
                                             QtWidgets.QMessageBox.No)
        if res == QtWidgets.QMessageBox.Yes:
            pass
        else:
            pass

    def display(self):
        word = self.unknown_words[self.count]
        self.word_name_output.setPlainText(word.get_name())
        self.word_context_output.setPlainText(word.get_context())
        self.word_ch_output.setPlainText(word.get_ch_interpretation())
        self.word_en_output.setPlainText(word.get_eng_interpretation())

    def last_one(self):
        self.count -= 1
        if self.count < 0:
            self.count += 1
        else:
            self.show()

    def next_one(self):
        self.count += 1
        if self.count >= len(self.unknown_words):
            if self.show_filename_input_dialog():
                self.finish()
        else:
            self.show()

    def show_filename_input_dialog(self):
        text, ok = QtWidgets.QInputDialog.getText(self, '提示',
                                        '生熟词已判断完毕，请输入文件名:')

        if ok:
            self.filename = str(text)
            return True
        return False

    def choose_familiar(self):
        word = Word(name=self.word_name_output.toPlainText(), context=self.word_context_output.toPlainText(),
                    ch_interpretation=self.word_ch_output.toPlainText(), eng_interpretation=self.word_en_output.toPlainText())
        self.new_words.append(word)
        self.next_one()

    def choose_vocabulary(self):
        self.old_words.append(self.word_name_output.toPlainText())
        self.next_one()

    def finish(self):
        update_familiar_words(old_words=self.old_words)
        update_vocabulary_words(new_words=self.new_words)
        third(self.new_words, self.filename)

    def get(self):
        s = self.up_bar_widget_input.toPlainText()
        self.new_words, self.unknown_words = first(s)

    def clear(self):
        self.up_bar_widget_input.clear()


def main():
    app = QtWidgets.QApplication(sys.argv)
    gui = MainInter()
    gui.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
