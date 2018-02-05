# -*- coding: utf-8 -*-
"""
# @Time    : 2018-02-01
# @Author  : StillRiver 
# @FileName: Fop.py  
# @Goal    : File OPeration Class
# @Software: Spyder
# Python3.6 

"""
from exception import MyException as expt
from lib import wordsegmt as ws

import os
import sys
import re

import xlrd
import pandas as pd

import jieba.analyse
import jieba


class Fop(object):
    """
    class Fop aims to operate a file, check assuence in advance.
    """
    
#    constructor func.
    def __init__(self,fpath):
#        print('I\'m constructor func.')
        # equivalently, assert statement
#        assert os.path.isfile(fpath), 'Neither a file input Nor with a Absolute/Relative path.'
        
        if not os.path.isfile(fpath):
            raise expt.MyException("Neither a file input Nor with a Absolute/Relative path.")
        else:
            self.fpath = fpath
#            self.outList = []
            self.outDF = pd.DataFrame()
        
##    method1:
#    def rdExcel(self,inList):
#        '''
#        method1: rdExcel(inList)
#        to read an excel file,giving their col indices
#        '''
#        
#        print('Here in rExcel')
#        
#        try:
#            wkbook = xlrd.open_workbook(self.fpath)
#        except IOError:
#            print('Failed to read this excel file')
#            sys.exit(1)
#            
#        sheet = wkbook.sheet_by_index(0)
#        print("Sheet.name=%s, nrows=%d, ncols=%d" %(sheet.name,sheet.nrows,sheet.ncols))
#        
#        for ind in inList:
#            self.outList.append(sheet.col(ind))
#            
#        return self.outList
    
    def rdExcelbyIndex(self,inList):
        '''
        method1: rdExcel(inList)
        to read an excel file via pandas,giving their col indices or col names
        '''
        
        print('Here in rExcel')
        
        # read file
        try:
            inDF = pd.read_excel(self.fpath,sheetname = 0)
        except IOError:
            print('Failed to read this excel file')
            sys.exit(1)
            
        # extract and return slices you want
        self.outDF = inDF.iloc[:,inList]
        return self.outDF
              

    def rdExcelbyColName(self,inList):
        '''
        method1: rdExcel(inList)
        to read an excel file via pandas,giving their col indices or col names
        '''
        
        print('Here in rExcel')
        
        # read file
        try:
            inDF = pd.read_excel(self.fpath,sheetname = 0)
        except IOError:
            print('Failed to read this excel file')
            sys.exit(1)
            
        # extract and return slices you want
        self.outDF = inDF.loc[:,inList]
        return self.outDF

        
        
#    method2:
    def doWordSegmt(self):
        """
        method2: doWordSegmt()
        carry out segmenting words, giving the text contained within class
        """
        print('Here in doWordSegmt')    

        df = self.outDF        
        
        # initialization
        wdsegmtDF = pd.DataFrame(columns = ["OrderNO","Labels",
                                            "AcceptSegmts","AcceptRefs",
                                            "HandleSegmts","HandleRefs"])

        

        # define my own re pattern 
        extractLabels_pattern = re.compile(r'【(.*?)】')   #? used for non-greedy mode, due to some labels placed afterwards
        removeDigitals_pattern = re.compile(r'\d+')  # at least 1 continous digital numbers
        clearText_pattern = re.compile(r'\W+')   # \W means non-character(not a zifu, not a digital, not a underscore _), namely [^A-Za-z0-9_]
        
        
        # ensemble
        wdsegmtDF.loc[:,"OrderNO"] = df.loc[:,"ORDERNO"]        
        acptContentSeries = df.loc[:,"ACCEPTCONTENT"]
        hadlContentSeries = df.loc[:,"HANDLESITUATION"]
        
        jieba.analyse.set_stop_words(r'D:\WorkSpace\TextMining\Python\WordSegmentation\stopwords\nonsense_words.txt')
        
        # loop iorder
        for iorder in range(len(df.index)):
            acptContent = str(acptContentSeries[iorder])
            hadlContent = str(hadlContentSeries[iorder])
            
            # remove digitals first
            acptText = removeDigitals_pattern.sub("",acptContent)
            hadlText = removeDigitals_pattern.sub("",hadlContent)
            # and then extract&clear labels
            labels = "/".join(extractLabels_pattern.findall(acptText))
            acptText = re.sub(r'【.*?】',"",acptText)
            # finally clear the text
            acptText = clearText_pattern.sub("",acptText)
            hadlText = clearText_pattern.sub("",hadlText)
            
            # jieba 
            acptWordList = ws.removestopwords(jieba.cut(acptText,cut_all=False))
            acptWords = "/".join(acptWordList) 
            acptTags = "/".join(jieba.analyse.extract_tags(acptText,topK=10,withWeight=False))
            
            hadlWordList = ws.removestopwords(jieba.cut(hadlText,cut_all=False))
            hadlWords = "/".join(hadlWordList) 
            hadlTags = "/".join(jieba.analyse.extract_tags(hadlText,topK=10,withWeight=False))
            
            # write into the data.frame
#            wdsegmtDF.at[iorder,"Labels"] = labels
#            wdsegmtDF.at[iorder,"Labels"] = 
            wdsegmtDF.loc[iorder,['Labels', 'AcceptSegmts', 'AcceptRefs', 'HandleSegmts','HandleRefs']] = [labels,acptWords,acptTags,hadlWords,hadlTags]
        
        self.outDF = wdsegmtDF
        return wdsegmtDF
            
        
#    def doWordSegmt(self):
#        """
#        method2: doWordSegmt()
#        carry out segmenting words, giving the acptText list
#        """
#        print('Here in doWordSegmt')    
#        
#        # initialization
#        wdsegmtList = []
#        contentList = self.outList
#        
#        # define my own re pattern 
#        extractOderNO_pattern = re.compile(r'text:\'(\d+)\'')   #\ used for transfer sense, () used for grouping to be extracted
#        extractLabels_pattern = re.compile(r'【(.*?)】')   #? used for non-greedy mode, due to some labels placed afterwards
#        removeDigitals_pattern = re.compile(r'\d+')  # at least 1 continous digital numbers
#        clearText_pattern = re.compile(r'\W+')   # \W means non-character(not a zifu, not a digital, not a underscore _), namely [^A-Za-z0-9_]
#        
#        # loop process
#        for icol in range(len(contentList)):
#            list = str(contentList[icol]).strip()  #str() convertion first, due to the need of re.
#            
#            if bool(re.search('ORDERNO',list[0],re.I)):   #if true, means this col corresponds to "ORDERNO"
#                wdsegmtList.append(extractOderNO_pattern.findall(list[1:]))  # remove title index
#            else:
#                # remove digitals first
#                list = removeDigitals_pattern.sub('',list[1:])
#                
#                # and then extract and clear labels
#                labels = "/".join(extractLabels_pattern.findall(list))
#                list = re.sub(r'【.*?】',"",list)
#                # and clear text form in list
#                list = clearText_pattern.sub("",list)
#                
#                # remove stopwords
#                pass
#                
                
                
    def wtExcel(self,fpath):
        """
        method3: wtExcel()
        write a dataframe to an excel file via pandas
        """
        print('Here in wtExcel')  
        
        writer = pd.ExcelWriter(fpath)

        self.outDF.to_excel(writer,
                            sheet_name = 'Sheet1',
                            na_rep = 'NULL',
                            header = True,
                            index = False) 
        
        writer.save()         