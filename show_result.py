#!/usr/bin/env python3
# -*-coding: utf-8 -*-

def display(path_done):
    text = []
    line = ''
    for c, etape in enumerate(path_done):
        if etape[1] != line:
            if c > 0:
                text.append(' et descendre à la station %s\n' % (path_done[c - 1][0]))
            text.append('Prendre la ligne %s direction %s' % (etape[1], etape[2]))
            line = etape[1]
          
    return ''.join(text)
