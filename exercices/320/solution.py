# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


words_open = open('words', 'r')
words_read = words_open.read()
words = words_read
# words = ['hello', 'hello', 'hello', 'helllleeeooooeertty']

i = 0
# input('press to continue')

#print(set(word))
m = {}
for l in set(word)-set(('\n',"'")):
#    my_dict = {'char': l, 'freq': word.count(l)/len(word)}
    m[l] = word.count(l)/len(word)
# print(sorted(m.items()))
#print(sorted(m))
for char in sorted(m):
    print("{}: {:.2f}".format(char, m[char]))


#for i in sorted(m, key=lambda x: x['char']):
#    print(m[i]['char']+':',"".format(n[i]['freq']))
 #   print("{char}: {freq:.2f}".format(char=i['char'], freq=i['freq']))
