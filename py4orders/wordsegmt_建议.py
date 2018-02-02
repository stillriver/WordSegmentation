# -*- coding: utf-8 -*-
"""
# @Time    : 2018-01-31
# @Author  : StillRiver 
# @FileName: wordsegmt_建议.py  
# @Software: Spyder
# Python3.6 

"""
import xlrd
import re
import csv
import jieba
import jieba.analyse

#read and write file path config
orderPath = r'D:\WorkSpace\TextMining\Data\all\建议.xlsx'
csvPath = r'D:\WorkSpace\TextMining\Data\all\建议.csv'
stpwdPath = r'D:\WorkSpace\TextMining\Python\WordSegmentation\stopwords\stop_words2.txt'
nsswdPath = r'D:\WorkSpace\TextMining\Python\WordSegmentation\stopwords\nonsense_words.txt'

#feature location
orderNoCol = 4
acptTextCol = 40
hadlTextCol = 50


#Read input excel file
#import xlrd

#fpath = 'D:\\WorkSpace\\Python\\Jupyter\\TextMining\\Steming\\投诉.xlsx'
#fpath = r'D:\WorkSpace\TextMining\Data\all\投诉.xlsx'
#wkbook = xlrd.open_workbook(fpath)
wkbook = xlrd.open_workbook(orderPath)

sheet = wkbook.sheet_by_index(0)
print("Sheet.name=%s, nrows=%d, ncols=%d" %(sheet.name,sheet.nrows,sheet.ncols))


#Regular expr. compile
#import re

#udf re mode
removeDigital = re.compile(r'\d+')
extractLabels = re.compile(r'【(.*?)】')
clearText = re.compile(r'\W+')

#import csv

csvFile = open(csvPath,'w',newline='')
wr = csv.writer(csvFile)
wr.writerow(["Index","Labels",
             #"AcceptContent",
             "AcceptSegmts","AcceptRefs",
             #"HandleContent",
             "HandleSegmts","HandleRefs"])

#import jieba
## 去除停用词的2个函数
# 创建停用词list
def stopwordslist(filepath):
    stopwords = [line.strip() for line in open(filepath, 'r').readlines()]
    return stopwords

# 对句子去除停用词
def removestopwords(sentence):
    stopwords = stopwordslist(stpwdPath)  # 这里加载停用词的路径
    words = []
    for word in sentence:
        if word not in stopwords:
            if word != ' 'and '\t'and'\n':
                words.append(word)

    return words

# config jieba
jieba.analyse.set_stop_words(nsswdPath)
    
for iOrder in range(1,sheet.nrows):   # from 1, because of excel file with header 
    #oderNo
    orderNoStr = sheet.cell_value(iOrder,orderNoCol)
    
    #AcceptContent
    acptText = removeDigital.sub("",sheet.cell_value(iOrder,acptTextCol))   
    labels = "/".join(extractLabels.findall(acptText))
    
    acptContent = clearText.sub("",re.sub(r'【.*?】',"",acptText.strip()))  #re.sub(r'【.*】',"",acptText).strip()
    acptWordList = removestopwords(jieba.cut(acptContent,cut_all=False))
    acptWords = "/".join(acptWordList)    
#    wordSet = set(wordList) 
    
    #TF-IDF
    acptTags = "/".join(jieba.analyse.extract_tags(acptContent,topK=10,withWeight=False))
    
    #HandleContent
    hadlText = removeDigital.sub("",sheet.cell_value(iOrder,hadlTextCol))   
    hadlContent = clearText.sub("",hadlText.strip())
    hadlWordList = removestopwords(jieba.cut(hadlContent,cut_all=False))
    hadlWords = "/".join(hadlWordList)  
    
    hadlTags = "/".join(jieba.analyse.extract_tags(hadlContent,topK=10,withWeight=False))
    
    wr.writerow([orderNoStr,labels,
                 # sheet.cell_value(iOrder,acptTextCol),
                 acptWords,acptTags,
                 #sheet.cell_value(iOrder,hadlTextCol),
                 hadlWords,hadlTags])
    
csvFile.close()
    

