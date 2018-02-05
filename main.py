# -*- coding: utf-8 -*-
"""
# @Time    : 2018-02-01
# @Author  : StillRiver 
# @FileName: main.py  
# @Software: Spyder
# Python3.6 

"""
import sys
import time

from exception import MyException as expt
from fileIO import Fop as proc



if __name__ == '__main__':
#    create a class <Fop> instance
    fpath = r'D:\WorkSpace\TextMining\Data\all\投诉.xlsx'
    
    start_time = time.time()
    
    try:
        fop = proc.Fop(fpath)
    except expt.MyException as e:
        print(e.message)
        sys.exit(1)
    
#    read files
    colIndices = [4,40,50]   #depent on which order you wanna to access
#    contentList = fop.rdExcelbyIndex(colIndices)
    colNames = ['ORDERNO','ACCEPTCONTENT','HANDLESITUATION']
    fop.rdExcelbyColName(colNames)
    wordsegmtDF = fop.doWordSegmt()
    fop.wtExcel(r'D:\WorkSpace\TextMining\投诉.xlsx')
    
    end_time = time.time()
    
    print('Running time: %d' %(end_time - start_time))
    
    
    
    
    
        

