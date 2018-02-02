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
import xlrd
#import xlwt


class Fop(object):
    """
    class Fop aims to operate a file, check assuence in advance.
    """
    
#    constructor func.
    def __init__(self,fpath):
#        print('I\'m constructor func.')
        if not os.path.isfile(fpath):
            raise expt.MyException("Neither a file input Nor with a Absolute/Relative path.")
        else:
            self.fpath = fpath
            self.outList = []
    
#    methods:
    def rExcel(self,inList):
        print('Here in rExcel')
        
        wkbook = xlrd.open_workbook(self.fpath)
        sheet = wkbook.sheet_by_index(0)
        print("Sheet.name=%s, nrows=%d, ncols=%d" %(sheet.name,sheet.nrows,sheet.ncols))
        
        for ind in inList:
            self.outList.append(sheet.col(ind))
            
        return self.outList
        
        
        