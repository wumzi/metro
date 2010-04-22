#!/usr/bin/env python3
# -*-coding: utf-8 -*-

def help():
    """Display the Help Page"""
    
    HELP_FILE = 'HELP'
    
    return ''.join(open(HELP_FILE).readlines())

def copyright():
    """Display the copyright notes"""

    COPYRIGHT_FILE = 'COPYRIGHT'

    return ''.join(open(COPYRIGHT_FILE).readlines())


if __name__ == '__main__':
    print(help())
    print(copyright())
