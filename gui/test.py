from PyQt5 import QtCore,QtGui,QtWidgets
import sys
import qtawesome


class MainInter(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

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

        self.main_layout.addWidget(self.up_widget, 0, 0, 18, 18)  # 上方部件在第0行第0列，占12行12列
        self.main_layout.addWidget(self.down_widget, 19, 0, 2, 18)  # 上方部件在第13行第13列，占3行12列
        self.setCentralWidget(self.main_widget)  # 设置窗口主部件

        self.up_bar_widget = QtWidgets.QWidget()  # 上方顶部搜索框部件
        self.up_bar_layout = QtWidgets.QGridLayout()  # 上方顶部搜索框网格布局
        self.up_bar_widget.setLayout(self.up_bar_layout)
        self.up_bar_widget_search_input = QtWidgets.QLineEdit()
        self.up_bar_widget_search_input.setPlaceholderText("输入要标记的文本")
        self.up_bar_layout.addWidget(self.up_bar_widget_search_input, 0, 1, 18, 18)
        self.up_layout.addWidget(self.up_bar_widget, 0, 0, 1, 9)

        self.down_button_1 = QtWidgets.QPushButton("清空")
        self.down_button_1.setObjectName('down_button')
        self.down_button_2 = QtWidgets.QPushButton("确认")
        self.down_button_2.setObjectName('down_button')
        self.down_layout.addWidget(self.down_button_1, 0, 0, 1, 3)
        self.down_layout.addWidget(self.down_button_2, 0, 3, 1, 3)



def main():
    app = QtWidgets.QApplication(sys.argv)
    gui = MainInter()
    gui.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()




