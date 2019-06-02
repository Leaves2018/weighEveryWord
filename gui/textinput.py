from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import qtawesome


class MainInter(QtWidgets.QMainWindow):
    s = ''

    def __init__(self):
        super().__init__()
        self.init_ui()

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
        self.up_button_2 = QtWidgets.QPushButton(qtawesome.icon('fa.sellsy', color='white'), "下一个")
        self.up_button_2.setObjectName('left_button')
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
        self.up_bar_widget_output_1 = QtWidgets.QTextEdit()
        self.up_bar_widget_output_1.setPlaceholderText("显示要判断的单词信息")
        self.up_bar_layout.addWidget(self.up_bar_widget_output_1, 0, 1, 3, 6)
        self.up_bar_widget_output_2 = QtWidgets.QTextEdit()
        self.up_bar_widget_output_2.setPlaceholderText("显示要判断的单词信息")
        self.up_bar_layout.addWidget(self.up_bar_widget_output_2, 0, 8, 3, 6)
        self.up_bar_widget_output_3 = QtWidgets.QTextEdit()
        self.up_bar_widget_output_3.setPlaceholderText("显示要判断的单词信息")
        self.up_bar_layout.addWidget(self.up_bar_widget_output_3, 5, 1, 5, 6)
        self.up_bar_widget_output_4 = QtWidgets.QTextEdit()
        self.up_bar_widget_output_4.setPlaceholderText("显示要判断的单词信息")
        self.up_bar_layout.addWidget(self.up_bar_widget_output_4, 5, 8, 5, 6)
        self.up_layout.addWidget(self.up_bar_widget, 0, 1, 18, 17)

        self.down_button_1 = QtWidgets.QPushButton("生词")
        self.down_button_1.setObjectName('down_button')
        self.down_button_2 = QtWidgets.QPushButton("熟词")
        self.down_button_2.setObjectName('down_button')
        self.down_button_2.setCheckable(True)
        self.down_button_2.toggle()
        self.down_button_2.clicked.connect(self.output)
        self.down_layout.addWidget(self.down_button_1, 1, 0, 1, 9)
        self.down_layout.addWidget(self.down_button_2, 1, 9, 1, 9)

    def get(self):
        s = self.up_bar_widget_input.toPlainText()

    def init_ui(self):
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

        self.main_layout.addWidget(self.up_widget, 0, 0, 18, 18)  # 上方部件在第0行第0列，占18行18列
        self.main_layout.addWidget(self.down_widget, 19, 0, 2, 18)  # 上方部件在第19行第0列，占2行18列
        self.setCentralWidget(self.main_widget)  # 设置窗口主部件

        self.up_bar_widget = QtWidgets.QWidget()  # 上方顶部搜索框部件
        self.up_bar_layout = QtWidgets.QGridLayout()  # 上方顶部搜索框网格布局
        self.up_bar_widget.setLayout(self.up_bar_layout)
        self.up_bar_widget_input = QtWidgets.QTextEdit()
        self.up_bar_widget_input.setPlaceholderText("输入要标记的文本")

        self.up_bar_layout.addWidget(self.up_bar_widget_input, 0, 1, 18, 18)
        self.up_layout.addWidget(self.up_bar_widget, 0, 0, 1, 9)

        self.down_button_1 = QtWidgets.QPushButton("清空")
        self.down_button_1.setObjectName('down_button')
        self.down_button_2 = QtWidgets.QPushButton("确认文本")
        self.down_button_2.setObjectName('down_button')
        self.down_button_2.setCheckable(True)
        self.down_button_2.toggle()
        self.down_button_2.clicked.connect(self.get)
        self.down_button_3 = QtWidgets.QPushButton("确认输入完毕")
        self.down_button_3.setObjectName('down_button')
        self.down_button_3.setCheckable(True)
        self.down_button_3.toggle()
        self.down_button_3.clicked.connect(self.openNext)
        self.down_layout.addWidget(self.down_button_1, 0, 0, 1, 3)
        self.down_layout.addWidget(self.down_button_2, 0, 3, 1, 3)
        self.down_layout.addWidget(self.down_button_3, 0, 6, 1, 3)


def main():
    app = QtWidgets.QApplication(sys.argv)
    gui = MainInter()
    gui.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()


