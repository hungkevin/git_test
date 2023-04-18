##!/Anaconda/envs/py37_vis/python
# -*- coding: utf-8 -*-
##!/usr/bin/python
## -*- coding: utf-8 -*-
#
# ref:
# Python __init__.py Uasge :
#  https://www.cnblogs.com/Lands-ljk/p/5880483.html
#  https://www.cnblogs.com/AlwinXu/p/5598543.html
#
#
#
# 魔术方法（magic method）是特殊方法的昵称。有些 Python 开发者在提到
# __getitem__ 这个特殊方法的时候，会用诸如“under-under-getitme” 这种说
# 法，但是显然这种说法会引起歧义，因为像 __x 这种命名在 Python 里还有其他含
# 义， 但是如果完整地说出“下划线－下划线－ getitem －下划线－下划线”，又会很麻
# 烦。于是我跟着 Steve Holden，一位技术书作者和老师，学会了“双下－
# getitem”（dunder-getitem）这种说法。于是乎，特殊方法也叫双下方法（dunder
# method）。
#
#
#

__version__ = 1.0
__author__ = 'JackHung@IEC'
__date__ = 20210120


import os
import sys
import time


""" =================================================== """

def func(i=0, j=1, k=2, l=3, m=4):

    print('ijklm: {} {} {} {} {} \r\n'.format(i,j,k,l,m))

    return 0

def main(argv):
    print('-'*50)
    L1 = ['a',2,'c',4]

    print('L1[0]: {} \r\n'.format(L1[0]))
    print('L1[0]: {} \r\n'.format(L1.__getitem__(0)))

    print('L1 Len: {} \r\n'.format(len(L1)))
    print('L1 Len: {} \r\n'.format(L1.__len__()))

    i0 = 0
    i5 = 5
    print('i0 Len: {} \r\n'.format(bool(i0)))
    print('i5 Len: {} \r\n'.format(bool(i5)))

    func('a',...,'e',...)

    print('-'*50)

    idx = 77
    print('idx org:{} {}\r\n'.format(idx, id(idx)))

    def local_func():
        for idx in range(5):
            print('idx local_func:{} {}\r\n'.format(idx, id(idx)))

    local_func()
    print('idx check _func:{} {}\r\n'.format(idx, id(idx)))

    iL5 = [idx for idx in range(5)]
    print('iL5:{}\r\n'.format(iL5))
    print('idx check _[]:{} {}\r\n'.format(idx, id(idx)))

    for idx in range(5):
        print('idx for loop:{} {}\r\n'.format(idx, id(idx)))
    print('idx check _for:{} {}\r\n'.format(idx, id(idx)))

""" =================================================== """


if __name__ == '__main__':
    print('='*50)
    main(sys.argv)
    print('='*50)
    #

