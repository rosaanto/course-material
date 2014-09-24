# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def myadd(a, b):
    return(a+b)
#

import sys
oper = ['+', '-', '\*', '/']
if (len(sys.argv) != 4):
    print('usage: python3 ./%s a_number (an_operator +-\*) a_number'
          % sys.argv[0])
else:
    if((sys.argv[2] not in oper) or (sys.argv[1].count('.')
       or sys.argv[3].count('.')) > 0):
        print('input error')
    else:
        if sys.argv[2] == '+':
            print(int(sys.argv[2])+int(sys.argv[3]))
        
#        print(type(sys.argv[1]), type(sys.argv[2]), type(sys.argv[3]))
    #if (type(sys.argv[1]) or type(sys.argv[3])) != int:
       # print('input error')
#if sys.argv[2] == '+':
#    return(sys.argv[1]+sys.argv[3])
#if sys.argv[2] == '-':
#    return(sys.argv[1]-sys.argv[3])
#if sys.argv[2] == '\*':
#    return(sys.argv[1]*sys.argv[3])
#if sys.argv[2] == '/':
#    return(sys.argv[1]/sys.argv[3])
    



#def myadd(a, b):
#    return(a+b)

#if len(sys.argv) > 1:
#    print(myadd(int(sys.argv[1]), int(sys.argv[2])))
#else:
#    print('usage: python3 %s OP1 OP2' % sys.argv[0])

