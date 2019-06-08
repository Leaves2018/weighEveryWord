# coding:utf-8

from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import *
import sys
import qtawesome


class MainUi(QMainWindow):
    def __init__(self):
        super().__init__()

        # 一、主部件
        self.main_widget = QWidget()
        self.main_layout = QGridLayout()

        # 二、左侧部件
        self.left_widget = QWidget()
        self.left_layout = QGridLayout()

        self.left_close = QPushButton("")
        self.left_visit = QPushButton("")
        self.left_mini = QPushButton("")

        self.left_label_1 = QPushButton("每日推荐")
        self.left_label_2 = QPushButton("我的音乐")
        self.left_label_3 = QPushButton("联系与帮助")

        self.left_button_1 = QPushButton(qtawesome.icon("fa.music", color="white"), "华语流行")
        self.left_button_2 = QPushButton(qtawesome.icon("fa.sellsy", color="white"), "在线FM")
        self.left_button_3 = QPushButton(qtawesome.icon("fa.film", color="white"), "热门MV")
        self.left_button_4 = QPushButton(qtawesome.icon("fa.home", color="white"), "本地音乐")
        self.left_button_5 = QPushButton(qtawesome.icon("fa.download", color="white"), "下载管理")
        self.left_button_6 = QPushButton(qtawesome.icon("fa.heart", color="white"), "我的收藏")
        self.left_button_7 = QPushButton(qtawesome.icon("fa.comment", color="white"), "反馈建议")
        self.left_button_8 = QPushButton(qtawesome.icon("fa.star", color="white"), "关注我们")
        self.left_button_9 = QPushButton(qtawesome.icon("fa.question", color="white"), "遇到问题")

        self.left_xxx = QPushButton(" ")

        # 三、右侧部件
        # 1 右侧部件（容器）
        self.right_widget = QWidget()
        self.right_layout = QGridLayout()

        # 2 搜索模块
        # 2.1 搜索按钮
        self.right_bar_widget = QWidget()
        self.right_bar_layout = QGridLayout()
        self.search_icon = QLabel(chr(0xf002) + " " + "搜索  ")
        # 2.2 搜索框
        self.right_bar_widget_search_input = QLineEdit()

        # 3 推荐音乐模块
        # 3.1 标题："今日推荐"
        self.right_recommend_label = QLabel("今日推荐")
        self.right_recommend_widget = QWidget()
        self.right_recommend_layout = QGridLayout()
        # 3.2 推荐专辑按钮
        self.recommend_button_1 = QToolButton()
        self.recommend_button_2 = QToolButton()
        self.recommend_button_3 = QToolButton()
        self.recommend_button_4 = QToolButton()
        self.recommend_button_5 = QToolButton()

        # 4 音乐列表
        self.right_new_song_label = QLabel("最新歌曲")
        self.right_playlist_label = QLabel("热门歌单")

        self.right_new_song_widget = QWidget()
        self.right_new_song_layout = QGridLayout()

        self.new_song_button_1 = QPushButton("夜机      陈慧娴      永远的朋友      03::29")
        self.new_song_button_2 = QPushButton("夜机      陈慧娴      永远的朋友      03::29")
        self.new_song_button_3 = QPushButton("夜机      陈慧娴      永远的朋友      03::29")
        self.new_song_button_4 = QPushButton("夜机      陈慧娴      永远的朋友      03::29")
        self.new_song_button_5 = QPushButton("夜机      陈慧娴      永远的朋友      03::29")
        self.new_song_button_6 = QPushButton("夜机      陈慧娴      永远的朋友      03::29")

        # 5 音乐歌单
        self.right_playlist_widget = QWidget()
        self.right_playlist_layout = QGridLayout()

        self.playlist_button_1 = QToolButton()
        self.playlist_button_2 = QToolButton()
        self.playlist_button_3 = QToolButton()
        self.playlist_button_4 = QToolButton()

        # 6 进度条
        self.right_process_bar = QProgressBar()

        self.right_playconsole_widget = QWidget()
        self.right_playconsole_layout = QGridLayout()

        self.console_button_1 = QPushButton(qtawesome.icon("fa.backward", color="#F76677"), "")
        self.console_button_2 = QPushButton(qtawesome.icon("fa.forward", color="#F76677"), "")
        self.console_button_3 = QPushButton(qtawesome.icon("fa.pause", color="#F76677", font=18), "")

        self.init_ui()

    def init_ui(self):
        # 零、窗口大小
        self.setFixedSize(960, 720)

        # 一、主部件
        self.main_widget.setLayout(self.main_layout)

        # 二、左侧部件
        self.left_widget.setObjectName("left_widget")
        self.left_widget.setLayout(self.left_layout)

        self.right_widget.setObjectName("right_widget")
        self.right_widget.setLayout(self.right_layout)

        self.main_layout.addWidget(self.left_widget, 0, 0, 12, 2)
        self.main_layout.addWidget(self.right_widget, 0, 2, 12, 10)

        self.setCentralWidget(self.main_widget)

        self.left_button_1.setObjectName("left_button")
        self.left_button_2.setObjectName("left_button")
        self.left_button_3.setObjectName("left_button")
        self.left_button_4.setObjectName("left_button")
        self.left_button_5.setObjectName("left_button")
        self.left_button_6.setObjectName("left_button")
        self.left_button_7.setObjectName("left_button")
        self.left_button_8.setObjectName("left_button")
        self.left_button_9.setObjectName("left_button")

        self.left_layout.addWidget(self.left_mini, 0, 0, 1, 1)
        self.left_layout.addWidget(self.left_visit, 0, 1, 1, 1)
        self.left_layout.addWidget(self.left_close, 0, 2, 1, 1)

        self.left_layout.addWidget(self.left_label_1, 1, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_1, 2, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_2, 3, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_3, 4, 0, 1, 3)

        self.left_layout.addWidget(self.left_label_2, 5, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_4, 6, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_5, 7, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_6, 8, 0, 1, 3)

        self.left_layout.addWidget(self.left_label_3, 9, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_7, 10, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_8, 11, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_9, 12, 0, 1, 3)

        # 三、右侧部件
        self.right_bar_widget.setLayout(self.right_bar_layout)  # 设置右侧部件布局

        # 搜索标志与搜索框
        self.search_icon.setFont(qtawesome.font("fa", 16))  # 设置搜索框字体及大小
        self.right_bar_widget_search_input.setPlaceholderText("输入歌手、歌曲或用户，按回车进行搜索")  # 提示符
        # 向右侧部件添加搜索标志、文本与搜索框
        self.right_bar_layout.addWidget(self.search_icon, 0, 0, 1, 1)
        self.right_bar_layout.addWidget(self.right_bar_widget_search_input, 0, 1, 1, 8)
        self.right_layout.addWidget(self.right_bar_widget, 0, 0, 1, 9)

        # 推荐模块：设置标签名、设置模块布局
        self.right_recommend_label.setObjectName("right_label")
        self.right_recommend_widget.setLayout(self.right_recommend_layout)

        # 推荐专辑按钮
        self.recommend_button_1.setText("Piano Chill")
        self.recommend_button_1.setIconSize(QtCore.QSize(100, 100))
        self.recommend_button_1.setIcon(QtGui.QIcon("r1.jpeg"))
        self.recommend_button_1.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)

        self.recommend_button_2.setText("Queen Essentials")
        self.recommend_button_2.setIconSize(QtCore.QSize(100, 100))
        self.recommend_button_2.setIcon(QtGui.QIcon("r2.jpeg"))
        self.recommend_button_2.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)

        self.recommend_button_3.setText("The A-List: Mandopop")
        self.recommend_button_3.setIconSize(QtCore.QSize(100, 100))
        self.recommend_button_3.setIcon(QtGui.QIcon("r3.jpeg"))
        self.recommend_button_3.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)

        self.recommend_button_4.setText("Today's Chill")
        self.recommend_button_4.setIconSize(QtCore.QSize(100, 100))
        self.recommend_button_4.setIcon(QtGui.QIcon("r4.jpeg"))
        self.recommend_button_4.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)

        self.recommend_button_5.setText("Unit 8 Modern College English")
        self.recommend_button_5.setIconSize(QtCore.QSize(100, 100))
        self.recommend_button_5.setIcon(QtGui.QIcon("r5.jpeg"))
        self.recommend_button_5.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)

        self.right_recommend_layout.addWidget(self.recommend_button_1, 0, 0)
        self.right_recommend_layout.addWidget(self.recommend_button_2, 0, 1)
        self.right_recommend_layout.addWidget(self.recommend_button_3, 0, 2)
        self.right_recommend_layout.addWidget(self.recommend_button_4, 0, 3)
        self.right_recommend_layout.addWidget(self.recommend_button_5, 0, 4)

        self.right_layout.addWidget(self.right_recommend_label, 1, 0, 1, 9)
        self.right_layout.addWidget(self.right_recommend_widget, 2, 0, 2, 9)

        # 4 音乐列表
        self.right_new_song_widget.setLayout(self.right_new_song_layout)

        self.right_new_song_layout.addWidget(self.new_song_button_1, 0, 1, )
        self.right_new_song_layout.addWidget(self.new_song_button_2, 1, 1, )
        self.right_new_song_layout.addWidget(self.new_song_button_3, 2, 1, )
        self.right_new_song_layout.addWidget(self.new_song_button_4, 3, 1, )
        self.right_new_song_layout.addWidget(self.new_song_button_5, 4, 1, )
        self.right_new_song_layout.addWidget(self.new_song_button_6, 5, 1, )

        # 5 音乐歌单
        self.right_playlist_widget.setLayout(self.right_playlist_layout)

        self.playlist_button_1.setText("无法释怀的整天循环音乐…")
        self.playlist_button_1.setIcon(QtGui.QIcon('./r1.jpg'))
        self.playlist_button_1.setIconSize(QtCore.QSize(100, 100))
        self.playlist_button_1.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)

        self.playlist_button_2.setText("不需要歌词,也可以打动你的心")
        self.playlist_button_2.setIcon(QtGui.QIcon('./r2.jpg'))
        self.playlist_button_2.setIconSize(QtCore.QSize(100, 100))
        self.playlist_button_2.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)

        self.playlist_button_3.setText("那些你熟悉又不知道名字…")
        self.playlist_button_3.setIcon(QtGui.QIcon('./r3.jpg'))
        self.playlist_button_3.setIconSize(QtCore.QSize(100, 100))
        self.playlist_button_3.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)

        self.playlist_button_4.setText("那些只听前奏就中毒的英文歌")
        self.playlist_button_4.setIcon(QtGui.QIcon('./r4.jpg'))
        self.playlist_button_4.setIconSize(QtCore.QSize(100, 100))
        self.playlist_button_4.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)

        self.right_playlist_layout.addWidget(self.playlist_button_1, 0, 0)
        self.right_playlist_layout.addWidget(self.playlist_button_2, 0, 1)
        self.right_playlist_layout.addWidget(self.playlist_button_3, 1, 0)
        self.right_playlist_layout.addWidget(self.playlist_button_4, 1, 1)

        # 将音乐列表、音乐歌单添加到右侧布局层中
        self.right_layout.addWidget(self.right_new_song_label, 4, 0, 1, 5)
        self.right_layout.addWidget(self.right_playlist_label, 4, 5, 1, 4)
        self.right_layout.addWidget(self.right_new_song_widget, 5, 0, 1, 5)
        self.right_layout.addWidget(self.right_playlist_widget, 5, 5, 1, 4)

        # 6 进度条
        self.right_process_bar.setValue(49)
        self.right_process_bar.setFixedHeight(3)  # 设置进度条高度
        self.right_process_bar.setTextVisible(False)  # 不显示进度条文字

        self.right_playconsole_widget.setLayout(self.right_playconsole_layout)

        self.console_button_3.setIconSize(QtCore.QSize(30, 30))

        self.right_playconsole_layout.addWidget(self.console_button_1, 0, 0)
        self.right_playconsole_layout.addWidget(self.console_button_2, 0, 2)
        self.right_playconsole_layout.addWidget(self.console_button_3, 0, 1)
        self.right_playconsole_layout.setAlignment(QtCore.Qt.AlignCenter)  # 设置布局内部件居中显示

        self.right_layout.addWidget(self.right_process_bar, 9, 0, 1, 9)
        self.right_layout.addWidget(self.right_playconsole_widget, 10, 0, 1, 9)


        # 美化
        self.left_close.setFixedSize(15, 15)  # 设置关闭按钮的大小
        self.left_visit.setFixedSize(15, 15)  # 设置按钮大小
        self.left_mini.setFixedSize(15, 15)  # 设置最小化按钮大小

        self.left_close.setStyleSheet(
            '''QPushButton{background:#F76677;border-radius:5px;}QPushButton:hover{background:red;}''')
        self.left_visit.setStyleSheet(
            '''QPushButton{background:#F7D674;border-radius:5px;}QPushButton:hover{background:yellow;}''')
        self.left_mini.setStyleSheet(
            '''QPushButton{background:#6DDF6D;border-radius:5px;}QPushButton:hover{background:green;}''')

        self.left_widget.setStyleSheet('''
            QPushButton{border:none;color:white;}
            QPushButton#left_label{
                border:none;
                border-bottom:1px solid white;
                font-size:18px;
                font-weight:700;
                font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
            }
            QPushButton#left_button:hover{border-left:4px solid red;font-weight:700;}
        ''')

        self.right_bar_widget_search_input.setStyleSheet(
            '''QLineEdit{
                    border:1px solid gray;
                    width:300px;
                    border-radius:10px;
                    padding:2px 4px;
            }''')

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
            QLabel#right_lable{
                border:none;
                font-size:16px;
                font-weight:700;
                font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
            }
        ''')

        self.right_recommend_widget.setStyleSheet(
            '''
                QToolButton{border:none;}
                QToolButton:hover{border-bottom:2px solid #F76677;}
            ''')
        self.right_playlist_widget.setStyleSheet(
            '''
                QToolButton{border:none;}
                QToolButton:hover{border-bottom:2px solid #F76677;}
            ''')

        self.right_new_song_widget.setStyleSheet('''
            QPushButton{
                border:none;
                color:gray;
                font-size:12px;
                height:40px;
                padding-left:5px;
                padding-right:10px;
                text-align:left;
            }
            QPushButton:hover{
                color:black;
                border:1px solid #F3F3F5;
                border-radius:10px;
                background:LightGray;
            }
        ''')

        self.right_process_bar.setStyleSheet('''
            QProgressBar::chunk {
                background-color: #F76677;
            }
        ''')

        self.right_playconsole_widget.setStyleSheet('''
            QPushButton{
                border:none;
            }
        ''')

        self.setWindowOpacity(0.9)  # 设置窗口透明度
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)  # 设置窗口背景透明
        # self.setWindowFlag(QtCore.Qt.FramelessWindowHint)  # 隐藏边框

        # self.left_widget.setStyleSheet('''
        # background:gray;
        # border-top:1px solid white;
        # border-bottom:1px solid white;
        # border-left:1px solid white;
        # border-top-left-radius:10px;
        # border-bottom-left-radius:10px;
        # ''')

        self.main_layout.setSpacing(0)



def main():
    app = QApplication(sys.argv)
    gui = MainUi()
    gui.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()