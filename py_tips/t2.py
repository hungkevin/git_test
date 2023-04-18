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
#
#
#

__version__ = 1.0
__author__ = 'JackHung@IEC'
__date__ = 20210120


import os
import sys
import time

# 引用numpy套件
import numpy as np


""" =================================================== """

# Generate a function to add two numbers
def add(x, y):
    return x + y


# with Python
# Generate an array of all the colors from the rainbow
rainbow = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']

# 產生一個10個數字的陣列
numbers = range(10)
# 將陣列中的數字相加
sum_of_numbers = sum(numbers)


# 產生 2個 1到100 的隨機數
random_numbers = np.random.randint(1, 100, 2)
# 將陣列中的數字相加
sum_of_numbers = add(*random_numbers)
# 將陣列中的數字相乘





def main(argv):

    print('-'*50)


""" =================================================== """


if __name__ == '__main__':
    print('='*50)
    main(sys.argv)
    print('='*50)
    #

