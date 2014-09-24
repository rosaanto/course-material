# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


def is_prime(num):
    if num == 1:
        return('False')
    else:
        for i in range(2, num):
            if num % i == 0:
                return('False')
        return('True')
count = 0
for i in range(0, 1000):
    if is_prime(i) == 'True':
        count = count + i
print(count)
