# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#x = ["abcdefghijklnmopqrstuvwxyz"]
#x = ["daf"]
#print(x)

from itertools import permutations
perms = [''.join(p) for p in permutations("daf")]
print(sorted(perms))
