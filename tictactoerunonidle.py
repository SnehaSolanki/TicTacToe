def DisplayBoard(board):
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|  ", board[0][0], "  |  ", board[0][1], "  |  ", board[0][2], "  |")
    print("|       |       |       |")
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|  ", board[1][0], "  |  ", board[1][1], "  |  ", board[1][2], "  |")
    print("|       |       |       |")
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|  ", board[2][0], "  |  ", board[2][1], "  |  ", board[2][2], "  |")
    print("|       |       |       |")
    print("+-------+-------+-------+")

#
# the function accepts one parameter containing the board's current status
# and prints it out to the console
#

def EnterMove(board):
    usmove = int(input("Enter your move:"))
    global mnum
    
    if usmove > 0 and usmove < 10:
        freeo = []
        if usmove == 1:
            freeo = MakeListOfFreeFields(board)
            for tup in freeo:
                if tup[0] == 0 and tup[1] == 0:
                    board[0][0] = 'O'
                    mnum += 1
                    break
        elif usmove == 2:
            freeo = MakeListOfFreeFields(board)
            for tup in freeo:
                if tup[0] == 0 and tup[1] == 1:
                    board[0][1] = 'O'
                    mnum += 1
                    break
        elif usmove == 3:
            freeo = MakeListOfFreeFields(board)
            for tup in freeo:
                if tup[0] == 0 and tup[1] == 2:
                    board[0][2] = 'O'
                    mnum += 1
                    break
        elif usmove == 4:
            freeo = MakeListOfFreeFields(board)
            for tup in freeo:
                if tup[0] == 1 and tup[1] == 0:
                    board[1][0] = 'O'
                    mnum += 1
                    break
        elif usmove == 5:
            freeo = MakeListOfFreeFields(board)
            print(freeo)
            for tup in freeo:
                if tup[0] == 1 and tup[1] == 1:
                    board[1][1] = 'O'
                    mnum += 1
                    break
        elif usmove == 6:
            freeo = MakeListOfFreeFields(board)
            for tup in freeo:
                if tup[0] == 1 and tup[1] == 2:
                    board[1][2] = 'O'
                    mnum += 1
                    break
        elif usmove == 7:
            freeo = MakeListOfFreeFields(board)
            for tup in freeo:
                if tup[0] == 2 and tup[1] == 0:
                    board[2][0] = 'O'
                    mnum += 1
                    break
        elif usmove == 8:
            freeo = MakeListOfFreeFields(board)
            for tup in freeo:
                if tup[0] == 2 and tup[1] == 1:
                    board[2][1] = 'O'
                    mnum += 1
                    break
        elif usmove == 9:
            freeo = MakeListOfFreeFields(board)
            for tup in freeo:
                if tup[0] == 2 and tup[1] == 2:
                    board[2][2] = 'O'
                    mnum += 1
                    break
    else:
        print("Invalid number, you will be prompted to enter again")
        EnterMove(board)  
        
    stat = VictoryFor(board, 'O')
    if stat == "Tie":
        print("Its a tie !!")
    elif stat == "comp":
        print("The computer wins !!")
    elif stat == "you":
        print("You win !!")
    else:
        DisplayBoard(board)
        DrawMove(board)
#
# the function accepts the board current status, asks the user about their move, 
# checks the input and updates the board according to the user's decision
#

def MakeListOfFreeFields(board):
    freeFields = []
    for i in range(3):
        for j in range(3):
            if board[i][j] != 'X' and board[i][j] != 'O':
                freeFields.append((i, j))
                
    return freeFields
#
# the function browses the board and builds a list of all the free squares; 
# the list consists of tuples, while each tuple is a pair of row and column numbers
#

def VictoryFor(board, sign):
    status = "play"
    wino = 0
    winx = 0
    if sign == 'O':
        if board[0][0] == 'O' and board[0][1] == 'O' and board[0][2] == 'O':
            wino += 1
        if board[1][0] == 'O' and board[1][1] == 'O' and board[1][2] == 'O':
            wino += 1
        if board[2][0] == 'O' and board[2][1] == 'O' and board[2][2] == 'O':
            wino += 1
        if board[0][0] == 'O' and board[1][0] == 'O' and board[2][0] == 'O':
            wino += 1
        if board[0][1] == 'O' and board[1][1] == 'O' and board[2][1] == 'O':
            wino += 1
        if board[0][2] == 'O' and board[1][2] == 'O' and board[2][2] == 'O':
            wino += 1
        if board[0][0] == 'O' and board[1][1] == 'O' and board[2][2] == 'O':
            wino += 1
        if board[0][2] == 'O' and board[1][1] == 'O' and board[2][0] == 'O':
            wino += 1
        
    else:
        if board[0][0] == 'X' and board[0][1] == 'X' and board[0][2] == 'X':
            winx += 1
        if board[1][0] == 'X' and board[1][1] == 'X' and board[1][2] == 'X':
            winx += 1
        if board[2][0] == 'X' and board[2][1] == 'X' and board[2][2] == 'X':
            winx += 1
        if board[0][0] == 'X' and board[1][0] == 'X' and board[2][0] == 'X':
            winx += 1
        if board[0][1] == 'X' and board[1][1] == 'X' and board[2][1] == 'X':
            winx += 1
        if board[0][2] == 'X' and board[1][2] == 'X' and board[2][2] == 'X':
            winx += 1
        if board[0][0] == 'X' and board[1][1] == 'X' and board[2][2] == 'X':
            winx += 1
        if board[0][2] == 'X' and board[1][1] == 'X' and board[2][0] == 'X':
            winx += 1
            
    if wino == winx and wino != 0 and winx != 0:
        status = "Tie"
    elif wino > winx:
        status = "you"
    elif wino < winx:
        status = "comp"
        
    return status
#
# the function analyzes the board status in order to check if 
# the player using 'O's or 'X's has won the game
#

def DrawMove(board):
    from random import randrange
    randnum = randrange(1,10)
    global mnum
    if mnum == 1:
        board[1][1] = 'X'
    else:
        free = []
        if randnum == 1:
            free = MakeListOfFreeFields(board)
            for tup in free:
                if tup[0] == 0 and tup[1] == 0:
                    board[0][0] = 'X'
                    mnum += 1
                    break
        elif randnum == 2:
            free = MakeListOfFreeFields(board)
            for tup in free:
                if tup[0] == 0 and tup[1] == 1:
                    board[0][1] = 'X'
                    mnum += 1
                    break
        elif randnum == 3:
            free = MakeListOfFreeFields(board)
            for tup in free:
                if tup[0] == 0 and tup[1] == 2:
                    board[0][2] = 'X'
                    mnum += 1
                    break
        elif randnum == 4:
            free = MakeListOfFreeFields(board)
            for tup in free:
                if tup[0] == 1 and tup[1] == 0:
                    board[1][0] = 'X'
                    mnum += 1
                    break
        elif randnum == 5:
            free = MakeListOfFreeFields(board)
            for tup in free:
                if tup[0] == 1 and tup[1] == 1:
                    board[1][1] = 'X'
                    mnum += 1
                    break
        elif randnum == 6:
            free = MakeListOfFreeFields(board)
            for tup in free:
                if tup[0] == 1 and tup[1] == 2:
                    board[1][2] = 'X'
                    mnum += 1
                    break
        elif randnum == 7:
            free = MakeListOfFreeFields(board)
            for tup in free:
                if tup[0] == 2 and tup[1] == 0:
                    board[2][0] = 'X'
                    mnum += 1
                    break
        elif randnum == 8:
            free = MakeListOfFreeFields(board)
            for tup in free:
                if tup[0] == 2 and tup[1] == 1:
                    board[2][1] = 'X'
                    mnum += 1
                    break
        elif randnum == 9:
            free = MakeListOfFreeFields(board)
            for tup in free:
                if tup[0] == 2 and tup[1] == 2:
                    board[2][2] = 'X'
                    mnum += 1
                    break
 
    stat = VictoryFor(board, 'X')
    if stat == "Tie":
        print("Its a tie !!")
    elif stat == "comp":
        print("The computer wins !!")
    elif stat == "you":
        print("You win !!")
    else:
        DisplayBoard(board)
        EnterMove(board)       
#
# the function draws the computer's move and updates the board

#board creation - appending empty lists
board = []
for i in range(3):
    board.append([])

#board creation - filling empty lists
count = 1        
for row in board:
    if count == 1:
        for i in range(1,4):
            row.append(i)
        count += 1
    elif count == 2:
        for i in range(4,7):
            row.append(i)
        count += 1
    else:
        for i in range(7,10):
            row.append(i)
            
DisplayBoard(board)

#play begins
mnum = 1

DrawMove(board)
DisplayBoard(board)

