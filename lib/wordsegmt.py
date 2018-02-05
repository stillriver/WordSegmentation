# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 13:45:21 2018
@Author: stillriver
@Python: 3.6
@IDE: Spyder3
"""

## 去除停用词的2个函数
# 创建停用词list
def stopwordslist(filepath):
    stopwords = [line.strip() for line in open(filepath, 'r').readlines()]
    return stopwords

# 对句子去除停用词
def removestopwords(sentence):
    stopwords = stopwordslist(r'D:\WorkSpace\TextMining\Python\WordSegmentation\stopwords\stop_words2.txt')  # 这里加载停用词的路径
    words = []
    for word in sentence:
        if word not in stopwords:
            if word != ' 'and '\t'and'\n':
                words.append(word)

    return words
