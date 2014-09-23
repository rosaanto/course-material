# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import sys
arg = sys.argv
mylist = list(enumerate(arg))
for i in mylist:
    print(' '.join([str(item) for item in i]))
