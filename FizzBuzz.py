# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 15:28:21 2019

@author: junka
"""

for idx in range(1,101):
    if idx%3 == 0 and idx%5 == 0:
        print ("fizzbuzz")
    elif idx%5 == 0:
        print ("fizz")
    elif idx%3 == 0:
        print ("buzz")
    else:
        print ("idx")
        