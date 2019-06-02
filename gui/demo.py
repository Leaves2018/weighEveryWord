# # -*- coding: utf-8 -*-
#
# """
# ZetCode PyQt5 tutorial
#
# In this example, we connect a signal
# of a QSlider to a slot of a QLCDNumber.
#
# author: Jan Bodnar
# website: zetcode.com
# last edited: January 2015
# """
#
# import sys
# from PyQt5.QtCore import Qt
# from PyQt5.QtWidgets import (QWidget, QLCDNumber, QSlider,
#                              QVBoxLayout, QApplication)
#
#
# class Example(QWidget):
#
#     def __init__(self):
#         super().__init__()
#
#         self.initUI()
#
#     def initUI(self):
#         lcd = QLCDNumber(self)
#         sld = QSlider(Qt.Horizontal, self)
#
#         vbox = QVBoxLayout()
#         vbox.addWidget(lcd)
#         vbox.addWidget(sld)
#
#         self.setLayout(vbox)
#         sld.valueChanged.connect(lcd.display)
#
#         self.setGeometry(300, 300, 250, 150)
#         self.setWindowTitle('Signal & slot')
#         self.show()
#
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ex = Example()
#     sys.exit(app.exec_())

# -*- coding: utf-8 -*-

"""
ZetCode PyQt5 tutorial

In this example, we reimplement an
event handler.

author: Jan Bodnar
website: zetcode.com
last edited: January 2015
"""

# import sys
# from PyQt5.QtCore import Qt
# from PyQt5.QtWidgets import QWidget, QApplication
#
#
# class Example(QWidget):
#
#     def __init__(self):
#         super().__init__()
#
#         self.initUI()
#
#     def initUI(self):
#         self.setGeometry(300, 300, 250, 150)
#         self.setWindowTitle('Event handler')
#         self.show()
#
#     def keyPressEvent(self, e):
#         if e.key() == Qt.Key_Escape:
#             self.close()
#
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ex = Example()
#     sys.exit(app.exec_())

# -*- coding: utf-8 -*-

"""
ZetCode PyQt5 tutorial

In this example, we determine the event sender
object.

author: Jan Bodnar
website: zetcode.com
last edited: January 2015
"""

# import sys
# from PyQt5.QtWidgets import QMainWindow, QPushButton, QApplication
#
#
# class Example(QMainWindow):
#
#     def __init__(self):
#         super().__init__()
#
#         self.initUI()
#
#     def initUI(self):
#         btn1 = QPushButton("Button 1", self)
#         btn1.move(30, 50)
#
#         btn2 = QPushButton("Button 2", self)
#         btn2.move(150, 50)
#
#         btn1.clicked.connect(self.buttonClicked)
#         btn2.clicked.connect(self.buttonClicked)
#
#         self.statusBar()
#
#         self.setGeometry(300, 300, 290, 150)
#         self.setWindowTitle('Event sender')
#         self.show()
#
#     def buttonClicked(self):
#         sender = self.sender()
#         self.statusBar().showMessage(sender.text() + ' was pressed')
#
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ex = Example()
#     sys.exit(app.exec_())

# !/usr/bin/python3
# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-

"""
ZetCode PyQt5 tutorial

In this example, we receive data from
a QInputDialog dialog.

author: Jan Bodnar
website: zetcode.com
last edited: January 2015
"""

import sys
from PyQt5.QtWidgets import (QWidget, QPushButton, QLineEdit,
                             QInputDialog, QApplication)


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.btn = QPushButton('Dialog', self)
        self.btn.move(20, 20)
        self.btn.clicked.connect(self.showDialog)

        self.le = QLineEdit(self)
        self.le.move(130, 22)

        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('Input dialog')
        self.show()

    def showDialog(self):
        text, ok = QInputDialog.getText(self, 'Input Dialog',
                                        'Enter your name:')

        if ok:
            self.le.setText(str(text))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())