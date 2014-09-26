# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


def euclidean(a, b):
    dpar = 0
    for i in range(0, len(a)):
        dpar = dpar + (b[i]-a[i])**2
    d = dpar**0.5
    return(d)


def opt_euclidean(a, b):
    import math
    dpar = 0
    for i in range(0, len(a)):
        dpar = dpar + math.pow((b[i]-a[i]), 2)
    d = math.sqrt(dpar)
    return(d)


def np_euclidean(a, b):
    import numpy as np
    import math
    d = math.sqrt(sum(np.power((np.array(b)-np.array(a)), 2)))
    return(d)

# a = [2,3]
# b =[5,6]
# a = [2,3,7,3,4,0,8,2,1]
# b = [5,3,0,7,8,6,9,4,5]
# print(euclidean(a, b))
# print(opt_euclidean(a, b))
# print(np_opt_euclidean(a, b))
