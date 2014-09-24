# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import sys
oper = ['+', '-', '*', '/', '%', '^']
if (len(sys.argv) != 4):
    print('usage: python3 solution.py a_number'
          '(an_operator +-*/%^) a_number')
elif((sys.argv[2] not in oper) or (sys.argv[1].count('.')
     or sys.argv[3].count('.')) > 0
     or (sys.argv[2] == '/' and sys.argv[3] == '0')):
    print('input error')
elif sys.argv[2] == '+':
    print(int(sys.argv[1]) + int(sys.argv[3]))
elif sys.argv[2] == '-':
    print(int(sys.argv[1]) - int(sys.argv[3]))
elif sys.argv[2] == '*':
    print(int(sys.argv[1]) * int(sys.argv[3]))
elif sys.argv[2] == '/':
    print(int(sys.argv[1]) / int(sys.argv[3]))
elif sys.argv[2] == '%':
    print(int(sys.argv[1]) % int(sys.argv[3]))
elif sys.argv[2] == '^':
    print(int(sys.argv[1]) ** int(sys.argv[3]))
