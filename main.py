# -*- coding: utf-8 -*-
"""
# @Time    : 2018-02-01
# @Author  : StillRiver 
# @FileName: main.py  
# @Software: Spyder
# Python3.6 

"""
import sys
from exception import MyException as expt
from fileIO import Fop as proc



if __name__ == '__main__':
#    create a class <Fop> instance
    fpath = r'D:\WorkSpace\TextMining\Data\all\意见.xlsx'
    
    try:
        fop = proc.Fop(fpath)
    except expt.MyException as e:
        print(e.message)
        sys.exit(1)
    
#    read files
    colIndices = [4,40,50]   #depent on which order you wanna to access
    contentList = fop.rdExcelbyIndex(colIndices)
    wordsegmtDF = fop.doWordSegmt()
    fop.wtExcel(r'D:\WorkSpace\TextMining\意见.xlsx')
    
    
    
    
    
        

