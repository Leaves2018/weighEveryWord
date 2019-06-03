# -*- coding:utf-8 -*-
import time
import threading
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mBox
import hashlib
import json
import random
import pyperclip
import webbrowser
import base64
import os
from urllib import parse
from urllib import request

"""
类说明:有道词典翻译的类
"""


class YOUDAO:

    def _quit(self):
        self.exitFlag = False
        mBox.showinfo(title='小y温馨提示', message='感谢您的使用~')
        self.root.quit()
        self.root.destroy()

    #         exit()

    def _progressGo(self):
        self.proBar.grid(row=0, column=0)
        for i in range(100):
            if not self.exitFlag:
                return
            self.proBar["value"] = i + 1
            self.root.update()
            time.sleep(0.06)
        self.proBar.grid_forget()

    def __init__(self, width=500, height=300):
        self.w = width
        self.h = height
        self.title = '有道词典(特别开心版)'
        self.root = tk.Tk(className=self.title)
        # 绑定关闭窗口为自定义函数
        self.root.protocol("WM_DELETE_WINDOW", self._quit)

        self.radio = tk.StringVar()
        self.radio.set('AUTO')
        self.exitFlag = True
        self.errorFlag = 0
        self.nextFlag = 0

        # 创建tabControl
        tabControl = ttk.Notebook(self.root)
        # 创建tab
        tab1 = ttk.Frame(tabControl)
        tabControl.add(tab1, text='O(∩_∩)O~')
        tabControl.pack(expand=1, fill="both")

        tab2 = ttk.Frame(tabControl)
        tabControl.add(tab2, text='点我点我')
        tabControl.pack(expand=1, fill="both")
        ttk.Label(tab2, text="作者长得帅").pack(pady=100)

        # 创建Frame空间
        # pack控件布局
        frame1 = ttk.Frame(tab1)
        frame2 = ttk.LabelFrame(tab1, text='翻译区')
        frame3 = ttk.Frame(tab1)

        # 创建MenuBar
        menuBar = tk.Menu(self.root)
        self.root.config(menu=menuBar)
        # 创建menu
        menu1 = tk.Menu(menuBar, tearoff=0)
        menuBar.add_cascade(label='菜单', menu=menu1)
        # 添加菜单项
        menu1.add_command(label='关于作者', command=lambda: webbrowser.open('http://inplus.top'))
        menu1.add_separator()
        menu1.add_command(label='退出', command=self._quit)

        toLangDictList = [{'自动': 'AUTO'}, {'汉->日': 'ja'}, {'汉->韩': 'ko'}, {'汉->法': 'fr'}, {'汉->俄': 'ru'},
                          {'汉->西班牙': 'es'}, {'汉->葡萄牙': 'pt'}, {'汉->越': 'vi'}]

        # 控件内容设置
        # 使用grid布局需要填写行列
        # 使用pack的side布局方式可以依次排开
        # ipadx控制左右内边距，ipady控制上下内边距
        # padx控制左右外边距，padx控制上下外边距
        # row控制行数，column控制列数
        # rowspan控制占据行数，columnspan控制占据列数
        # sticky控制位置，W、N、S、E、W+N等等八个方位
        ttk.Label(frame1, text="模式：").pack(side=tk.LEFT)
        for i in range(len(toLangDictList)):
            textKey = list(toLangDictList[i].keys())[0]
            textValue = list(toLangDictList[i].values())[0]
            # Radiobutton的indicatoron默认为1，当设置成0时，则其外观是Sunken
            tk.Radiobutton(frame1, text=textKey, variable=self.radio, value=textValue,
                           command=lambda: self.text_translateAnsy(1), indicatoron=0).pack(side=tk.LEFT)
        label1 = ttk.Label(frame2, text="请输入要翻译的文本：")
        self.text1 = tk.Text(frame2, height=6, width=35)
        translateButton1 = ttk.Button(frame2, text="翻译▼", command=lambda: self.text_translateAnsy(1))
        translateButton3 = ttk.Button(frame2, text="从剪贴板翻译", command=self.pasteAndExecute)
        label2 = ttk.Label(frame2, text="翻译结果：")
        self.text2 = tk.Text(frame2, height=6, width=35)
        translateButton2 = ttk.Button(frame2, text="自动▲", command=lambda: self.text_translateAnsy(2))
        translateButton4 = ttk.Button(frame2, text="复制结果到剪贴板",
                                      command=lambda: pyperclip.copy(self.text2.get(1.0, tk.END)[:-1]))

        self.proBar = ttk.Progressbar(frame3, length=200, mode="determinate", orient=tk.HORIZONTAL)
        self.proBar["maximum"] = 100
        self.proBar["value"] = 0
        # ttk需要使用style
        style = ttk.Style()
        style.configure("BW.TLabel", foreground='red', font=('楷体', 12, 'bold'))
        label_tip = ttk.Label(frame3, text='作者:风澈', style="BW.TLabel")

        frame1.pack(pady=10)
        frame2.pack()
        frame3.pack()

        label1.grid(row=2, column=0)
        self.text1.grid(row=2, column=1, rowspan=2)
        translateButton1.grid(row=3, column=2)
        translateButton3.grid(row=3, column=0, padx=5)
        label2.grid(row=4, column=0)
        self.text2.grid(row=4, column=1, rowspan=2)
        translateButton2.grid(row=4, column=2)
        translateButton4.grid(row=5, column=0, padx=5)

        label_tip.grid(row=1, column=0)

    """
    创建线程，异步调用
    """

    def text_translateAnsy(self, mode):
        if self.nextFlag == 1:
            return
        translateT = threading.Thread(target=self.text_translate, args=(mode,))
        translateT.setDaemon(True)
        translateT.start()
        self.progressT = threading.Thread(target=self._progressGo(), args=(mode,))
        self.progressT.start()

    """
    函数说明:执行翻译
    """

    def text_translate(self, mode):
        self.nextFlag = 1
        # 主通道
        urlMain = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
        # 备用通道
        urlBak = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
        # text1翻译至text2
        if mode == 1:
            textGet = self.text1
            textSet = self.text2
            toLang = self.radio.get()
        # text2翻译至text1
        if mode == 2:
            textGet = self.text2
            textSet = self.text1
            toLang = 'AUTO'
        if self.errorFlag == 1:
            urlMain = urlBak
        # 获取将要源text的值，并剔除最后一个字符，即text自带的一个换行符
        contentWord = textGet.get(1.0, tk.END)[:-1]
        # 因为有道网页是textarea，识别\r\n但不识别\n，在此做替换 
        contentWord.replace('\n', '\r\n')
        if not contentWord:
            self.nextFlag = 0
            self.proBar.grid_forget()
            return
        translateResults = self.conn(urlMain, contentWord, 'AUTO', toLang)
        # 找到翻译结果
        try:
            if translateResults["errorCode"] == 0:
                newResult = ''
                for translateResult in translateResults["translateResult"]:
                    newResult += translateResult[0]['tgt'] + '\n'

            elif translateResults["errorCode"] == 40:
                newResult = '输入个汉语呗~~'
            else:
                mBox.showerror(title='小y温馨提示', message='网络连接异常')
                self.nextFlag = 0
                self.proBar.grid_forget()
                return
        except:
            # 异常时启用备用地址翻译
            if self.errorFlag == 0:
                self.errorFlag = 1
                return self.text_translate(mode)
            mBox.showerror(title='小y温馨提示', message='网络连接异常')
            self.nextFlag = 0
            self.proBar.grid_forget()
            return
        # 结束前设置进度条100，显得更符合逻辑
        self.proBar["value"] = 100
        self.root.update()
        textSet.delete(1.0, tk.END)
        textSet.insert(tk.INSERT, newResult[:-1])
        self.nextFlag = 0
        self.proBar.grid_forget()

    """
    函数说明:连接服务器执行翻译
    """

    def conn(self, url, contentWord, fromLang, toLang):
        # 构造有道的加密参数
        client = "fanyideskweb"
        ts = int(time.time() * 1000)
        salt = str(ts + random.randint(1, 10))
        flowerStr = "p09@Bn{h02_BIEe]$P^nG"
        sign = hashlib.md5((client + contentWord + salt + flowerStr).encode('utf-8')).hexdigest()
        bv = '9deb57d53879cce82ff92bccf83a3e4c'
        # 创建Form_Data字典，存储请求体
        Form_Data = {}
        # 需要翻译的文字
        Form_Data['i'] = contentWord
        # 下面这些都先按照我们之前抓包获取到的数据
        Form_Data['from'] = fromLang
        Form_Data['to'] = toLang
        Form_Data['smartresult'] = 'dict'
        Form_Data['client'] = client
        Form_Data['salt'] = salt
        Form_Data['sign'] = sign
        Form_Data['ts'] = ts
        Form_Data['bv'] = bv
        Form_Data['doctype'] = 'json'
        Form_Data['version'] = '2.1'
        Form_Data['keyfrom'] = 'fanyi.web'
        Form_Data['action'] = 'FY_BY_REALTIME'
        Form_Data['typoResult'] = 'false'
        # 对数据进行字节流编码处理
        data = parse.urlencode(Form_Data).encode('utf-8')
        # 创建Request对象
        req = request.Request(url=url, data=data, method='POST')
        # 写入header信息
        req.add_header('User-Agent',
                       'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36')
        req.add_header('cookie', 'OUTFOX_SEARCH_USER_ID=-1626129620@10.168.8.63')
        req.add_header('Referer', 'http://fanyi.youdao.com/')
        # 传入创建好的Request对象
        try:
            # 超时时间设置3秒
            response = request.urlopen(req, timeout=3)
        except:
            return
        # 读取信息并解码
        html = response.read().decode('utf-8')
        # 使用JSON
        return json.loads(html)

    '''
从剪贴板粘贴并执行翻译
    '''

    def pasteAndExecute(self):
        self.text1.delete(1.0, tk.END)
        self.text1.insert(tk.INSERT, pyperclip.paste())
        self.text_translateAnsy(1)

    """
    函数说明:tkinter窗口居中
    """

    def center(self):
        ws = self.root.winfo_screenwidth()
        hs = self.root.winfo_screenheight()
        x = int((ws / 2) - (self.w / 2))
        y = int((hs / 2) - (self.h / 2))
        self.root.geometry('{}x{}+{}+{}'.format(self.w, self.h, x, y))

    """
    函数说明:loop等待用户事件
    """

    def loop(self):
        # 禁止修改窗口大小
        self.root.resizable(False, False)
        # 窗口居中
        self.center()
        # 设置图标
        self.root.iconbitmap(r'resource\youdao.ico')
        # 光标焦点
        self.text1.focus()
        self.root.mainloop()


if __name__ == '__main__':
    app = YOUDAO()  # 实例化APP对象
    app.loop()  # loop等待用户事件