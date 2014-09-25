# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


def draw_n_squares(n):
    line1 = '+---'
    line2 = '|   '
    square = n*(n*line1 + '+' + '\n' + n*line2+'|' + '\n') + (n*line1 + '+')
    return(square)
