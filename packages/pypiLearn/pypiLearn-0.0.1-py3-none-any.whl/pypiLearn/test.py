# -*- coding: utf-8 -*

"""
@author: Ocean
"""

import sys
import os

class Test:
    __version__ = '0.0.1'
    def __init__(self):
        ''' initialization
        '''
        print("__init__")

    def sayhello(self):
        ''' say hello :)
        '''
        print("Hello world!")


if __name__ == '__main__':
    t = Test()
    t.sayhello()
