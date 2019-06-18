# coding:utf-8


# 字典树的结点结构
class TrieNode(object):
    def __init__(self):
        self.data = {}          # 结点数据（字典类型）
        self.is_word = False    # 默认为False（只有叶子结点代表单词）


# 字典树的定义
class Trie(object):
    # 初始化：定义根为一个TrieNode
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """
        向字典树中插入新结点
        :type word: str
        :rtype: void
        """
        # 设置当前结点node为根，即从根开始插入
        node = self.root
        # 顺序遍历输入字符串word的每一个字符
        for letter in word:
            # 在node的数据字典中查找该字符，如果不存在，则返回默认值None
            child = node.data.get(letter)
            # 如果返回的是None，即根结点的数据字典中没有该字符
            if not child:
                # 则以该字符为根创建一颗子字典树
                node.data[letter] = TrieNode()
            # 进入字典树的下一层，继续插入
            node = node.data[letter]
        # 单词插入完成。此时node为叶子结点，代表一个单词
        node.is_word = True

    def search(self, word):
        """
        如果word在字典树中，则返回True；否则返回False
        :type word: str
        :rtype: bool
        """
        # 设置当前结点node为根，即从根开始查找
        node = self.root
        # 顺序遍历输入字符串word的每一个字符
        for letter in word:
            # 在node的数据字典中查找该字符，如果不存在，则返回默认值None
            node = node.data.get(letter)
            # 如果返回了None，则认为查找失败，终止查找，返回False
            if not node:
                return False
        # 判断单词是否是完整的存在于字典树中
        return node.is_word

    def starts_with(self, prefix):
        """
        如果字典树中存在以prefix为前缀的单词，则返回True；否则返回False
        :type prefix: str
        :rtype: bool
        """
        # 设置当前结点node为根，即从根开始查找
        node = self.root
        # 顺序遍历输入字符串prefix的每一个字符
        for letter in prefix:
            # 从node的数据字典中获取该字符
            node = node.data.get(letter)
            # 如果找不到，则认为字典树中没有以该字符开头的单词，返回False
            if not node:
                return False
        # 如果for循环没有被中断，则默认返回True
        return True

    def get_start(self, prefix):
        """
        以列表形式返回字典树中所有以prefix为前缀的单词
        :param prefix:
        :return: words (list)
        """
        def _get_key(pre, pre_node):
            words_list = []
            # 如果前一个结点是单词（叶子结点）
            if pre_node.is_word:
                # 直接加入待返回列表
                words_list.append(pre)
            # 遍历pre_node的数据字典的键
            for x in pre_node.data.keys():
                # 扩展words_list，以递归的形式按层向下深入
                words_list.extend(_get_key(pre + str(x), pre_node.data.get(x)))
            return words_list

        words = []
        # 如果字典树中没有以输入字符串prefix为前缀的单词，直接返回空列表
        if not self.starts_with(prefix):
            return words
        # 如果字典书中刚好有输入字符串prefix，则返回含有prefix的列表
        if self.search(prefix):
            words.append(prefix)
            return words
        # 从根开始
        node = self.root
        # 顺序遍历输入的字符串prefix
        for letter in prefix:
            # 在node的数据字典中查找该字符
            node = node.data.get(letter)
        # 无论prefix中的字符找到与否，都交由_get_key(prefix, node)函数处理
        return _get_key(prefix, node)
