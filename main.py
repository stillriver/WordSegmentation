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
    fpath = r'D:\WorkSpace\TextMining\Data\all\建议.xlsx'
    
    try:
        fop = proc.Fop(fpath)
    except expt.MyException as e:
        print(e.message)
        sys.exit(1)
    
#    read files
    contentList = fop.rExcel([4,40,50])
    
    
    
    
        

