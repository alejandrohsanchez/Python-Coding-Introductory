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
