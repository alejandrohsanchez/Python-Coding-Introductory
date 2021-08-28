#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 28 01:32:59 2021
@author: alejandrosanchez
"""
    
def printBoard(board):
    for i in range(len(board)):
        if (i % 5 != 0):
            print(board[i], end = '')
        else:
            print()
            print(board[i], end = '')

board = [' 1 ', " | ", " 2 ", " | ", " 3 ", "---", "-|-", "---", "-|-", "---", " 4 ", " | ", " 5 ", " | ", " 6 ", "---", "-|-", "---", "-|-", "---", " 7 ", " | ", " 8 ", " | ", " 9 "]

printBoard(board)