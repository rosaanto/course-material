# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

x = "abcdefghijklnmopqrstuvwxyz"
from itertools import product
for i in product(x, repeat=2):
    print(''.join(i))
