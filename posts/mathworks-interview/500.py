class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        charRowMapping = {} # 搞一个字符到排号的映射
        charRowMapping.update({v: 0 for v in "qwertyuiop"}) # 第一排的所有字符
        charRowMapping.update({v: 1 for v in "asdfghjkl"}) # 第二排的所有字符
        charRowMapping.update({v: 2 for v in "zxcvbnm"}) # 第三排的所有字符
        res = []

        for word in words:
            if len(set(charRowMapping[v] for v in word.lower())) == 1: # 如果单词里面所有的字符都在同一排
                res.append(word)

        return res