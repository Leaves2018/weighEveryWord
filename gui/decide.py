from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import qtawesome


class MainInter(QtWidgets.QMainWindow):
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

        self.up_bar_widget = QtWidgets.QWidget()  # 上方顶部搜索框部件
        self.up_bar_layout = QtWidgets.QGridLayout()  # 上方顶部搜索框网格布局
        self.up_bar_widget.setLayout(self.up_bar_layout)
        self.up_bar_widget_search_input = QtWidgets.QTextEdit()
        self.up_bar_widget_search_input.setPlaceholderText("显示要判断的单词信息")
        self.up_bar_layout.addWidget(self.up_bar_widget_search_input, 0, 1, 18, 17)
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




def main():
    app = QtWidgets.QApplication(sys.argv)
    gui = MainInter()
    gui.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()




