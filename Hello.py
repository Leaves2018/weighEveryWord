from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import qtawesome


class MainInter(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.output()

    def output(self):
        res = QtWidgets.QMessageBox.question(self, '提示',
                                             "单词列表已保存至桌面", QtWidgets.QMessageBox.Yes |
                                             QtWidgets.QMessageBox.No,
                                             QtWidgets.QMessageBox.No)
        if res == QtWidgets.QMessageBox.Yes:
            pass
        else:
            pass


def main():
    app = QtWidgets.QApplication(sys.argv)
    gui = MainInter()
    gui.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()




