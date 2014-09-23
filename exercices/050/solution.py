# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
x = range(1, 1000, 1)
count = 0
for i in x:
    if (i % 3 == 0 or i % 5 == 0):
        count = count + i
print(count)
