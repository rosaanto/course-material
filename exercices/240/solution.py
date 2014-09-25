# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

f0 = 1
f1 = 2
fibo_list = []
for i in range(1, 11):
    f2 = int(f1) + int(f0)
    f0 = f1
    f1 = f2
    fibo_list.append(str(f2))
print(", ".join(fibo_list)+'.')
