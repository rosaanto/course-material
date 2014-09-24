# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


def is_alpha(alpha):
    alphabeth = 'abcdefghijklmnopqrstuvwxyz'
    ALPHABETH = alphabeth.upper()
    for i in alphabeth+ALPHABETH:
        if alpha.count(i) != 0:
            return True
    return False
