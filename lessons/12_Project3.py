"""
Practice Project 3: Taking Input from Terimal to play Tic-Tac-Toe
Created: 3/16/2020

In this project we will use what we learned from assignments 1-11 to
to code a tic-tac-toe game.


Functionality:
    1. Initialize a game board that is size 3x3.
        - The game board should be initialized with all "-" characters
    2. Take two user inputs:
        "row: "
        "column: "
    3. Mark the game board with a "O" for user inputs with a function called markBoardUser(gameboard)
    4. Pass the game board to my function markBoardCPU(gameboard) that determines the best move for the computer
        - This function edits the game board directly and adds "X"
    5. Continue playing until there is a winner or all the spots are filled

"""
import numpy as np

''' 
Part 1a:
    Initialize a game board that is a list of size 3x3.
    Make all the characters on the board "-"
'''
def createBoard():
    gb = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]
    return gb


'''
Part 1b:
    Lets make a print function to print a game board. 
    The function will print the game board to the terminal.
    example:
     - | - | O
     - | - | X
     - | O | -
'''
def printGameBaord(gb):
    for row in gb:
        for i in range(len(row)):
            if i < len(row)-1:
                print(" " + row[i] + " |", end='')
            else:
                print(" " + row[i])


'''
Part 2a:
    Lets take user input! 
    If the user wants to place a piece on the board, 
    we need to get a users input from the terminal. 
    
    The easiest way to get an input from the terminal is with the following method:
    row = input()
    column = input()
    
    Adopt this for getting the row and column of user input.     
    return the row and column values for this function.
    Hint: Make sure they are cast to ints using int() otherwise they will be strings
'''
def getUserInput():
    print("Input Row: ", end="")
    row = input()
    print("Input Column: ", end="")
    column = input()
    return int(row), int(column)


'''
Part 2b: 
    Check User Input:
    1. Request user input using getUserInput()
    2. Make sure the row / column is on the game board: 
        - we will take row / column values of 1, 2, 3 (not 0, 1, 2)
        - make sure the position isn't already taken
    3. If either condition is false, 
        print a statement saying, invalid entry, then ask for user input again
    4. Once the conditions are met, return the row column pair
'''
def userTurn(gb):
    invalid_entry = True
    while(invalid_entry):
        invalid_entry = False
        row, column = getUserInput()
        if row < 0 or row > 3 or column < 0 or column > 3 or gb[row-1][column-1] != "-":
            print("Invalid Entry, Try again")
            invalid_entry = True
    return row, column


'''
Part 3: 
    Mark the gameboard for a user with a "O" 
    based on the row / column returned by userTurn(gb)
'''
def markBoardUser(gb):
    row, column = userTurn(gb)
    gb[row-1][column-1] = "O"


'''
Do Not Edit: CPU Game Play
'''
def markBoardCPU(gb):
    def row_sum(pgb, row):
        sum = np.sum(pgb[row])
        if sum == 4:
            sum = 8
        if sum == 6:
            sum = 9
        if sum == 5:
            sum = 1
        return sum
    def column_sum(pgb, col):
        sum = np.sum(pgb.T[col])
        if sum == 4:
            sum = 8
        if sum == 6:
            sum = 9
        if sum == 5:
            sum = 1
        return sum
    def back_horiz(pgb):
        sum = pgb[0][0] + pgb[1][1] + pgb[2][2]
        if sum == 4:
            sum = 8
        if sum == 6:
            sum = 9
        if sum == 5:
            sum = 1
        return sum
    def for_horiz(pgb):
        sum = pgb[0][2] + pgb[1][1] + pgb[2][0]
        if sum == 4:
            sum = 8
        if sum == 6:
            sum = 9
        if sum == 5:
            sum = 1
        return sum
    pgb = np.zeros((3,3))
    pgbf = np.zeros((3,3))
    for r in range(3):
        for c in range(3):
            if gb[r][c] == 'O':
                pgb[r][c] += 2
            if gb[r][c] == 'X':
                pgb[r][c] += 3
    for r in range(3):
        for c in range(3):
            if gb[r][c] == '-':
                pgbf[r][c] = row_sum(pgb, r)
                pgbf[r][c] += column_sum(pgb, c)
                if r == 0 and c == 0 or r == 1 and c == 1 or r == 2 and c == 2:
                    pgbf[r][c] += back_horiz(pgb)
                if r == 2 and c == 0 or r == 1 and c == 1 or r == 0 and c == 2:
                    pgbf[r][c] += for_horiz(pgb)
    pgbf[1][1] += 1
    #print(pgbf)
    pgbf = pgbf.reshape(9,1)
    max = np.argmax(pgbf)
    r = int(max/3)
    c = max%3
    gb[r][c] = "X"


'''
Part 5:
    Check Termination
    Define a function called checkTermination 
    
    Hint: use a large if statement with 8 checks for the eight ways to win tic-tac-toe
    
    If the game board has no spots left or if someone one, 
    checkTermination = True
    return termination, tieOrWin
    tieOrWin = 0 if tied, 1 if playerOrCPU wins 
'''
def checkTermination(gb):
    termination = True
    tieOrWin = "tie"
    for row in gb:
        for column in row:
            if column == "-":
                termination = False
                tieOrWin = None
    if  gb[0][0] == gb[1][0] and gb[0][0] == gb[2][0] and gb[0][0] != '-' or \
        gb[0][1] == gb[1][1] and gb[0][1] == gb[2][1] and gb[0][1] != '-' or \
        gb[0][2] == gb[1][2] and gb[0][2] == gb[2][2] and gb[0][2] != '-' or \
        gb[0][0] == gb[0][1] and gb[0][0] == gb[0][2] and gb[0][0] != '-' or \
        gb[1][0] == gb[1][1] and gb[1][0] == gb[1][2] and gb[1][0] != '-' or \
        gb[2][0] == gb[2][1] and gb[2][0] == gb[2][2] and gb[2][0] != '-' or \
        gb[0][0] == gb[1][1] and gb[0][0] == gb[2][2] and gb[0][0] != '-' or \
        gb[2][0] == gb[1][1] and gb[2][0] == gb[0][2] and gb[2][0] != '-':
        termination = True
        tieOrWin = "win"
    return termination, tieOrWin


'''
Part 4:
    Play Game!
    Define a function called playGame
    use a while loop to play. 

    Alternate between user turns and CPU turns
    General layout:
        whose_turn = 0
        while continue_game:
            if whose_turn == 0:
                markBoardUser(gb)
                whose_turn = 1
            else:
                markBoardCPU(gb)
                whose_turn = 0
            printGameBoard(gb)
            continue_game = checkTermination(gb)
        print(who won?)
        printGameBoard(gb)
'''
def playGame():
    game_board = createBoard()
    whose_turn = 0
    terminate_game = False
    printGameBaord(game_board)
    while not terminate_game:
        if whose_turn == 0:
            print("Users Turn")
            markBoardUser(game_board)
            whose_turn = 1
        else:
            print("CPU Turn")
            markBoardCPU(game_board)
            whose_turn = 0
        printGameBaord(game_board)
        terminate_game, tieOrWin = checkTermination(game_board)
    if tieOrWin == "win":
        if whose_turn == 0:
            print("CPU Winner")
        else:
            print("Player Winner")
    else:
        print("Tie Game")
    printGameBaord(game_board)

playGame()