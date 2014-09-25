# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


def is_prime(num):
    if num == 1:
        return(False)
    else:
        for i in range(2, num):
            if num % i == 0:
                return(False)
        return(True)
prime_list = []
for i in range(100000000, 100000000+10):
    if is_prime(i):
        prime_list.append(str(i))
print(prime_list[0])
