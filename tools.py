#!/usr/bin/env python3
# -*-coding: utf-8 -*-

def clean_name(name):
    name = name.lower()
    map = (('à', 'a'), ('â', 'a'), ('é', 'e'), ('è', 'e'), ('ë', 'e'), ('ê', 'e'), ('û', 'u'), ('ô', 'o'), ('ü', 'u'), ('ö', 'o'), ('-', ' '))

    for item in map:
        name = name.replace(item[0], item[1])
    
    return name

def secondes_to_higher(time):

    hours = int(time / 3600)
    minutes = int((time - (3600 * hours)) / 60)
    #seconds = time - ((3600 * hours) + (60 * minutes))

    return minutes
