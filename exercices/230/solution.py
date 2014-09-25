# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


def is_prime(num):
    if num == 1:
        return(False)
    else:
        for i in range(2, int((num**0.5)+1)):
            if num % i == 0:
                return(False)
        return(True)


def search_prime_1(num):
    while not is_prime(num):
        num += 1
        is_prime(num)
    else:
        return(num)


def search_prime_2(num):
    prime_list = []
    for i in range(num, num+8):
        if is_prime(i):
            prime_list.append(str(i))
    return(prime_list[0])

num = 100000000
# print(search_prime_1(num))
print(search_prime_2(num))
