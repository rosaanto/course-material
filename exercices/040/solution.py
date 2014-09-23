# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

x = range(0, 101, 1)
evensum = 0
for i in x:
    if i % 2 == 0:
        evensum = evensum + i
print(evensum)
