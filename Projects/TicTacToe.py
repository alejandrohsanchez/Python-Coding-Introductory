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
    if (C <= 0 or C >= 10):
        print('Incorrect input, please enter a number 1 - 9')
        return 0

    if (C == 1 and board[0] == '   '):
        board[0] = player
        return 1
    elif (C == 2 and board[2] == '   '):
        board[2] = player
        return 1
    elif (C == 3 and board[4] == '   '):
        board[4] = player
        return 1
    elif (C == 4 and board[10] == '   '):
        board[10] = player
        return 1
    elif (C == 5 and board[12] == '   '):
        board[12] = player
        return 1
    elif (C == 6 and board[14] == '   '):
        board[14] = player
        return 1
    elif (C == 7 and board[20] == '   '):
        board[20] = player
        return 1
    elif (C == 8 and board[22] == '   '):
        board[22] = player
        return 1
    elif (C == 9 and board[24] == '   '):
        board[24] = player
        return 1
    else:
        print('Tile is already taken, please try again.')
        return 0

def checkWin(board):
    if (board[0] != '   ' and board[2] != '   ' and board[4] != '   ' and board[0] == board[2] and board[2] == board[4]):
        return True
    elif (board[10] != '   ' and board[12] != '   ' and board[14] != '   ' and board[10] == board[12] and board[12] == board[14]):
        return True
    elif (board[20] != '   ' and board[22] != '   ' and board[24] != '   ' and board[20] == board[22] and board[22] == board[24]):
        return True
    elif (board[0] != '   ' and board[10] != '   ' and board[20] != '   ' and board[0] == board[10] and board[10] == board[20]):
        return True
    elif (board[2] != '   ' and board[12] != '   ' and board[22] != '   ' and board[2] == board[12] and board[12] == board[22]):
        return True
    elif (board[4] != '   ' and board[14] != '   ' and board[24] != '   ' and board[4] == board[14] and board[14] == board[24]):
        return True
    elif (board[0] != '   ' and board[12] != '   ' and board[24] != '   ' and board[0] == board[12] and board[12] == board[24]):
        return True
    elif (board[4] != '   ' and board[12] != '   ' and board[20] != '   ' and board[4] == board[12] and board[12] == board[20]):
        return True
    else:
        return False

def startGame(origin, board):
    print('Player 1 (X) vs Player 2 (O)')
    for i in range(9):
        check = False
        win = False
        if (i % 2 == 0):
            while (check == False):
                choice = int(input('Player 1: '))
                # Enter the player input if the tile is available
                if (enterInput(' X ', choice, board)):
                    # Check if the player has won
                    check = True
                    if (checkWin(board)):
                        win = True
                        printBoard(origin, board)
                        print('Player 1 wins!')
                        break
                    printBoard(origin, board)
            if (win):
                break            

        else:
            while (check == False):
                choice = int(input('Player 2: '))
                if (enterInput(' O ', choice, board)):
                    check = True
                    if (checkWin(board)):
                        win = True
                        printBoard(origin, board)
                        print('Player 2 wins!')
                        break
                    printBoard(origin, board)
            if (win):
                break

        printBoard(origin, board)
        if (i == 8 and win == False):
            print('No winner...')

origin = [' 1 ', " | ", " 2 ", " | ", " 3 ", "---", "-|-", "---", "-|-", "---", " 4 ", " | ", " 5 ", " | ", " 6 ", "---", "-|-", "---", "-|-", "---", " 7 ", " | ", " 8 ", " | ", " 9 "]
board = ['   ', " | ", "   ", " | ", "   ", "---", "-|-", "---", "-|-", "---", "   ", " | ", "   ", " | ", "   ", "---", "-|-", "---", "-|-", "---", "   ", " | ", "   ", " | ", "   "]

printBoard(origin, board)
startGame(origin, board)