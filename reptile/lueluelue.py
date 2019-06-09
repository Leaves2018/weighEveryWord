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
        self.new_button.setShortcut('Ctrl+'+chr(32))

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