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

import os
import sys
import re

import xlrd
import pandas as pd


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
            self.outList = []
        
#    method1:
    def rdExcel(self,inList):
        '''
        method1: rdExcel(inList)
        to read an excel file,giving their col indices
        '''
        
        print('Here in rExcel')
        
        try:
            wkbook = xlrd.open_workbook(self.fpath)
        except IOError:
            print('Failed to read this excel file')
            sys.exit(1)
            
        sheet = wkbook.sheet_by_index(0)
        print("Sheet.name=%s, nrows=%d, ncols=%d" %(sheet.name,sheet.nrows,sheet.ncols))
        
        for ind in inList:
            self.outList.append(sheet.col(ind))
            
        return self.outList
        
#    method2:
    def doWordSegmt(self):
        """
        method2: doWordSegmt()
        carry out segmenting words, giving the content list
        """
        print('Here in doWordSegmt')    
        
        # initialization
        wdsegmtList = []
        contentList = self.outList
        
        # define my own re pattern 
        extractOderNO_pattern = re.compile(r'text:\'(\d+)\'')   #\ used for transfer sense, () used for grouping to be extracted
        extractLabels_pattern = re.compile(r'【(.*?)】')   #? used for non-greedy mode, due to some labels placed afterwards
        removeDigitals_pattern = re.compile(r'\d+')  # at least 1 continous digital numbers
        clearText_pattern = re.compile(r'\W+')   # \W means non-character(not a zifu, not a digital, not a underscore _), namely [^A-Za-z0-9_]
        
        # loop process
        for icol in range(len(contentList)):
            list = str(contentList[icol]).strip()  #str() convertion first, due to the need of re.
            
            if bool(re.search('ORDERNO',list[0],re.I)):   #if true, means this col corresponds to "ORDERNO"
                wdsegmtList.append(extractOderNO_pattern.findall(list[1:]))  # remove title index
            else:
                # remove digitals first
                list = removeDigitals_pattern.sub('',list[1:])
                
                # and then extract and clear labels
                labels = "/".join(extractLabels_pattern.findall(list))
                list = re.sub(r'【.*?】',"",list)
                # and clear text form in list
                list = clearText_pattern.sub("",list)
                
                # remove stopwords
                
                
                
        