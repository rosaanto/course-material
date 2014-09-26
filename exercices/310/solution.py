# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


words_open = open('words', 'r')
words_read = words_open.readlines()
count = 0
word = words_read
for w in range(0, len(word)):
    count = count + word[w].count('e')
print(count)
