from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import qtawesome


class SecondInter(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.decide()



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
        self.up_button_1.clicked.connect(self.lastone)

        self.up_button_2 = QtWidgets.QPushButton(qtawesome.icon('fa.sellsy', color='white'), "下一个")
        self.up_button_2.setObjectName('left_button')
        self.up_button_2.setCheckable(True)
        self.up_button_2.toggle()
        self.up_button_2.clicked.connect(self.nextone)

        self.up_button_return = QtWidgets.QPushButton(qtawesome.icon('fa.music', color='white'), "返回")
        self.up_button_return.setObjectName('left_button')
        self.up_button_return.setCheckable(True)
        self.up_button_return.toggle()
        self.up_button_return.clicked.connect(self.init_ui)

        self.up_layout.addWidget(self.up_button_1, 9, 0, 1, 1)
        self.up_layout.addWidget(self.up_button_2, 9, 18, 1, 1)
        self.up_layout.addWidget(self.up_button_return, 0, 0, 1, 1)

        self.up_bar_widget = QtWidgets.QWidget()  # 上方顶部部件
        self.up_bar_layout = QtWidgets.QGridLayout()  # 上方顶部网格布局
        self.up_bar_widget.setLayout(self.up_bar_layout)

        self.word_name_output = QtWidgets.QTextEdit()
        self.word_name_output.setPlaceholderText("单词名称")
        self.up_bar_layout.addWidget(self.word_name_output, 0, 1, 3, 6)

        self.word_ch_output = QtWidgets.QTextEdit()
        self.word_ch_output.setPlaceholderText("中文解释")
        self.up_bar_layout.addWidget(self.word_ch_output, 0, 8, 3, 6)

        self.word_context_output = QtWidgets.QTextEdit()
        self.word_context_output.setPlaceholderText("语境信息")
        self.up_bar_layout.addWidget(self.word_context_output, 5, 1, 5, 6)

        self.word_en_output = QtWidgets.QTextEdit()
        self.word_en_output.setPlaceholderText("英文解释")
        self.up_bar_layout.addWidget(self.word_en_output, 5, 8, 5, 6)
        self.up_layout.addWidget(self.up_bar_widget, 0, 1, 18, 17)

        self.btn_vocabulary_word = QtWidgets.QPushButton("生词")
        self.btn_vocabulary_word.setObjectName('down_button')
        self.btn_vocabulary_word.setCheckable(True)
        self.btn_vocabulary_word.toggle()
        self.btn_vocabulary_word.clicked.connect(self.shengci)

        self.btn_familiar_word = QtWidgets.QPushButton("熟词")
        self.btn_familiar_word.setObjectName('down_button')
        self.btn_familiar_word.setCheckable(True)
        self.btn_familiar_word.toggle()
        self.btn_familiar_word.clicked.connect(self.shuci)

        self.down_layout.addWidget(self.btn_vocabulary_word, 1, 0, 1, 9)
        self.down_layout.addWidget(self.btn_familiar_word, 1, 9, 1, 9)


# def main():
#     app = QtWidgets.QApplication(sys.argv)
#     gui = SecondInter()
#     gui.show()
#     sys.exit(app.exec_())
#
#
# if __name__ == '__main__':
#     main()




