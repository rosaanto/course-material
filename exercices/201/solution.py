# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


def is_alpha(alpha):
    alphabeth = 'aàbcçdeéèfghijklmnopqrstuvwxyz'
    ALPHABETH = alphabeth.upper()
    sum_alpha = 0
    for i in alphabeth+ALPHABETH:
        sum_alpha = sum_alpha + alpha.count(i)
    if sum_alpha == len(alpha):
        return True
    return False
