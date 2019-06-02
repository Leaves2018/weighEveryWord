from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import qtawesome


# class MainInter(QtWidgets.QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.confirm()

def confirm(self):
    self.main_widget = QtWidgets.QWidget()  # 创建窗口主部件
    self.main_layout = QtWidgets.QGridLayout()  # 创建主部件的网格布局
    self.main_widget.setLayout(self.main_layout)  # 设置窗口主部件布局为网格布局

    self.up_widget = QtWidgets.QWidget()  # 创建上方部件
    self.up_widget.setObjectName('up_widget')
    self.up_layout = QtWidgets.QGridLayout()  # 创建上方部件的网格布局层
    self.up_widget.setLayout(self.up_layout)  # 设置上方部件布局为网格

    self.main_layout.addWidget(self.up_widget, 0, 0, 18, 18)  # 上方部件在第0行第0列，占18行18列
    self.setCentralWidget(self.main_widget)  # 设置窗口主部件

    self.text_prompt = QtWidgets.QLabel("文本已输入完毕？")
    self.text_prompt.setObjectName('right_lable')
    self.up_layout.addWidget(self.text_prompt, 0, 0, 1, 9)

    self.up_button_1 = QtWidgets.QPushButton("返回")
    self.up_button_1.setObjectName('down_button')
    self.up_button_1.setCheckable(True)
    self.up_button_1.toggle()
    self.up_button_1.clicked.connect(self.init_ui)
    self.up_button_2 = QtWidgets.QPushButton("确认")
    self.up_button_2.setObjectName('down_button')
    self.up_button_2.setCheckable(True)
    self.up_button_2.toggle()
    self.up_button_2.clicked.connect(self.decide)
    self.up_layout.addWidget(self.up_button_1, 1, 0, 1, 3)
    self.up_layout.addWidget(self.up_button_2, 1, 5, 1, 3)




# def main():
#     app = QtWidgets.QApplication(sys.argv)
#     gui = MainInter()
#     gui.show()
#     sys.exit(app.exec_())
#
#
# if __name__ == '__main__':
#     main()




