# -*- coding: utf-8 -*-

class MyException(Exception):
    '''define my own exception type and corresponding handling treasurs'''
    '''usage:
            ...=MyException(message)
    '''
    def __init__(self,msg):
        Exception.__init__(self)
        self.message = msg