#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 28 01:32:59 2021
@author: alejandrosanchez
"""

import properties as prop

def startGame(origin, board):
    print('Player 1 (X) vs Player 2 (O)')
    for i in range(9):
        check = False
        win = False
        if (i % 2 == 0):
            while (check == False):
                choice = int(input('Player 1: '))
                # Enter the player input if the tile is available
                if (prop.enterInput(' X ', choice, board)):
                    # Check if the player has won
                    check = True
                    if (prop.checkWin(board)):
                        win = True
                        prop.printBoard(origin, board)
                        print('Player 1 wins!')
                        break
                    prop.printBoard(origin, board)
            if (win):
                break            

        else:
            while (check == False):
                choice = int(input('Player 2: '))
                if (prop.enterInput(' O ', choice, board)):
                    check = True
                    if (prop.checkWin(board)):
                        win = True
                        prop.printBoard(origin, board)
                        print('Player 2 wins!')
                        break
                    prop.printBoard(origin, board)
            if (win):
                break

        prop.printBoard(origin, board)
        if (i == 8 and win == False):
            print('No winner...')
    

origin = [' 1 ', " | ", " 2 ", " | ", " 3 ", "---", "-|-", "---", "-|-", "---", " 4 ", " | ", " 5 ", " | ", " 6 ", "---", "-|-", "---", "-|-", "---", " 7 ", " | ", " 8 ", " | ", " 9 "]
board = ['   ', " | ", "   ", " | ", "   ", "---", "-|-", "---", "-|-", "---", "   ", " | ", "   ", " | ", "   ", "---", "-|-", "---", "-|-", "---", "   ", " | ", "   ", " | ", "   "]

prop.printBoard(origin, board)
startGame(origin, board)