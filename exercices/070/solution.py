# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

x = "abcdefghijklmnopqrstuvwxyz"

from itertools import permutations
for i in permutations(x, 2):
    print(''.join(i))
