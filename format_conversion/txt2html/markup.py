# import sys
# import re
# from handlers import *
# from util import *
# from rules import *
#
# class Parser:
#     """
#     Parser读取文本文件，应用规则并控制处理程序
#     """
#     def __init__(self, handler):
#         self.handler = handler
#         self.rules = []
#         self.filters = []
#
#     def add_rule(self, rule):
#         self.rules.append(rule)
#
#     def add_filter(self, pattern, name):
#         def filter(block, handler):
#             return re.sub(pattern, handler.sub(name), block)
#         self.filters.append(filter)
#
#     def parse(self, file):
#         self.handler.start('document')
#         for block in blocks(file):
#             for filter in self.filters:
#                 block = filter(block, self.handler)
#                 for rule in self.rules:
#                     if rule.condition(block):
#                         last = rule.action(block, self.handler)
#                         if last:
#                             break
#         self.handler.end('document')
#
#
# class BasicTextParser(Parser):
#     """
#     在构造函数中添加规则和过滤器的Parser子类
#     """
#     def __init__(self, handler):
#         Parser.__init__(self, handler)
#         self.add_rule(ListRule)
#         self.add_rule(ListItemRule)
#         self.add_rule(TitleRule)
#         self.add_rule(HeadingRule)
#         self.add_rule(ParagraphRule)
#
#         self.add_filter(r'\*(.+?)\*', 'emphasis')
#         self.add_filter(r'(http://[\.a-zA-Z/]+)', 'url')
#         self.add_filter(r'([\.a-zA-Z]+@[\.a-zA-Z]+[a-zA-Z]+)', 'mail')
#
#
# handler = HTMLRenderer()
# parser = BasicTextParser(handler)
#
# parser.parse(sys.stdin)
import sys, re
from format_conversion.txt2html.handlers import *
from format_conversion.txt2html.util import *
from format_conversion.txt2html.rules import *

class Parser:
    """
    A Parser reads a text file, applying rules and controlling a handler.
    """
    def __init__(self, handler):
        self.handler = handler
        self.rules = []
        self.filters = []
    def addRule(self, rule):
        self.rules.append(rule)
    def addFilter(self, pattern, name):
        def filter(block, handler):
            return re.sub(pattern, handler.sub(name), block)
        self.filters.append(filter)

    def parse(self, file):
        self.handler.start('document')
        for block in blocks(file):
            for filter in self.filters:
                block = filter(block, self.handler)
                for rule in self.rules:
                    if rule.condition(block):
                        last = rule.action(block,
                               self.handler)
                        if last: break
        self.handler.end('document')

class BasicTextParser(Parser):
    """
    A specific Parser that adds rules and filters in its constructor.
    """
    def __init__(self, handler):
        Parser.__init__(self, handler)
        self.addRule(ListRule())
        self.addRule(ListItemRule())
        self.addRule(TitleRule())
        self.addRule(HeadingRule())
        self.addRule(ParagraphRule())

        self.addFilter(r'\*(.+?)\*', 'emphasis')
        self.addFilter(r'(http://[\.a-zA-Z/]+)', 'url')
        self.addFilter(r'([\.a-zA-Z]+@[\.a-zA-Z]+[a-zA-Z]+)', 'mail')

handler = HTMLRenderer()
parser = BasicTextParser(handler)

parser.parse(sys.stdin)
