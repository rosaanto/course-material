# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import sys


def mysub(a, b):
    return(a-b)

if len(sys.argv) > 1:
    mysub(int(sys.argv[1]), int(sys.argv[2]))
else:
    print('usage: python3 %s OP1 OP2' % sys.argv[0])
