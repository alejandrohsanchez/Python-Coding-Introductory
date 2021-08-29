#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 28 01:32:59 2021
@author: alejandrosanchez
"""

#import properties as prop
   
def printBoard(origin, board):
    for i in range(len(origin)):
        if (i % 5 != 0):
            print(origin[i], end = '')
        else:
            print()
            print(origin[i], end = '')
    print("\n")
    
    for i in range(len(board)):
        if (i % 5 != 0):
            print(board[i], end = '')
        else:
            print()
            print(board[i], end = '')
    print()

def enterInput(player, C, board):
    if (C == 1):
        board[0] = player
    elif (C == 2):
        board[2] = player
    elif (C == 3):
        board[4] = player
    elif (C == 4):
        board[10] = player
    elif (C == 5):
        board[12] = player
    elif (C == 6):
        board[14] = player
    elif (C == 7):
        board[20] = player
    elif (C == 8):
        board[22] = player
    elif (C == 9):
        board[24] = player

def startGame(origin, board):
    print('Player 1 (X) vs Player 2 (O)')
    
    for i in range(9):
        if (i % 2 == 0):
            choice = int(input('Player 1: '))
            enterInput(' X ', choice, board)
        else:
            choice = int(input('Player 2: '))
            enterInput(' O ', choice, board)
        
        printBoard(origin, board)

origin = [' 1 ', " | ", " 2 ", " | ", " 3 ", "---", "-|-", "---", "-|-", "---", " 4 ", " | ", " 5 ", " | ", " 6 ", "---", "-|-", "---", "-|-", "---", " 7 ", " | ", " 8 ", " | ", " 9 "]
board = ['   ', " | ", "   ", " | ", "   ", "---", "-|-", "---", "-|-", "---", "   ", " | ", "   ", " | ", "   ", "---", "-|-", "---", "-|-", "---", "   ", " | ", "   ", " | ", "   "]

printBoard(origin, board)
startGame(origin, board)