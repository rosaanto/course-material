# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


words_open = open('words', 'r')
words_read = words_open.read()
words_content = words_read[:-1]
print(words_content)
