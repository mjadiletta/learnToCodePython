"""
Practice Project 3: Taking Input from Terimal to play Tic-Tac-Toe
Created: 3/17/2020

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
from solutions.CheckSolutions import CheckSolutions
checkSolutions = CheckSolutions().project3Solutions

''' 
Part 1a:
    Initialize a game board that is a list of size 3x3.
    Make all the characters on the board "-"
'''
def createBoard():
    gb = None
    return gb

checkSolutions['project3p1a'](createBoard)


'''
Part 1b:
    Lets make a print function to print a game board. 
    The function will print the game board to the terminal.
    example:
     - | - | O
     - | - | X
     - | O | -
     
     There's no check solution to this, so just do it correctly.
'''
def printGameBaord(gb):
    for r in range(len(gb)):
        for c in range(len(gb[r])):
            None


'''
Part 2a:
    Lets take user input! 
    If the user wants to place a piece on the board, 
    we need to get a users input from the terminal. 
    
    The easiest way to get an input from the terminal is with the following method:
    row = input("message")
    column = input("message")
    
    Adopt this for getting the row and column of user input.     
    return the row and column values for this function.
    Hint: Make sure they are cast to ints using int() otherwise they will be strings
'''
def getUserInput():
    row = None
    column = None
    return None, None

checkSolutions['project3p2a'](getUserInput)

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
        row, column = 0, 0
        if None:  # check for invalid entry
            print("Invalid Entry, Try again")
            invalid_entry = True
    return row, column

checkSolutions['project3p2b'](userTurn, createBoard())


'''
Part 3: 
    Mark the gameboard for a user with a "O" 
    based on the row / column returned by userTurn(gb)
'''
def markBoardUser(gb):
    row, column = userTurn(gb)
    gb[row-1][column-1] = "O"

checkSolutions['project3p3'](markBoardUser, createBoard())


'''
Do Not Edit: CPU Game Play
There is one way to beat this CPU 
- find it for a "fantastic prize"
'''
def markBoardCPU(gb):
    def row_sum(pgb, row):
        sum = np.sum(pgb[row])
        if sum == 4:
            sum = 8
        if sum == 6:
            sum = 12
        if sum == 5:
            sum = 1
        return sum
    def column_sum(pgb, col):
        sum = np.sum(pgb.T[col])
        if sum == 4:
            sum = 8
        if sum == 6:
            sum = 12
        if sum == 5:
            sum = 1
        return sum
    def back_horiz(pgb):
        sum = pgb[0][0] + pgb[1][1] + pgb[2][2]
        if sum == 4:
            sum = 8
        if sum == 6:
            sum = 12
        if sum == 5:
            sum = 1
        #if sum == 3 and pgb[2][0] == 2 and pgb[0][2] == 2:
        #    sum = 0
        return sum
    def for_horiz(pgb):
        sum = pgb[0][2] + pgb[1][1] + pgb[2][0]
        if sum == 4:
            sum = 8
        if sum == 6:
            sum = 12
        if sum == 5:
            sum = 1
        if sum == 3 and pgb[0][0] == 2 and pgb[2][2] == 2:
            sum = 0
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
    
    If the game board has no spots left or if someone won, 
        checkTermination = True
        return termination, tieOrWin
    tieOrWin =  "tie": if tied / there are no spots left on the board, 
                "win": if the player or cpu won, 
                None: if there are still spots left to play and no one won 
    
    Note:
    Start with Part 5 below and just call checkTermination(game_board) in part4 in the correct spot
    Test this function yourself with various game board instances / setups.
    The check solution will tell you if it is actually correct or not.  
'''
def checkTermination(gb):
    termination = True
    tieOrWin = "tie"

    # check if there are still empty spots
    # if there are still empty spots, termination = False, tieOrWin = None
    for row in gb:
        for column in row:
            if None:
                None

    # add the other checks to this if statement to check all possible winning solutions to tic-tac-toe
    if gb[0][0] == gb[1][0] and gb[0][0] == gb[2][0] and gb[0][0] != '-' or \
        None :
        termination = None
        tieOrWin = None

    return None, None

checkSolutions['project3p5'](checkTermination, createBoard())


'''
Part 4:
    Play Game!
    Define a function called playGame
    use a while loop to play. 

    Alternate between user turns and CPU turns
    General layout:
        whose turn -> 0
        while continueGame
            if players turn:
                player marks the board
                whose turn -> 1
            if cpu turn:
                cpu marks the board
                whose turn -> 0
        print who won
        print game board
    
        
        Note: There is only 1 way to beat my CPU.
            If you find it, I'll give you a "fabulous prize!" 
            
        - There is no check solution for this. If you can play
            a game of Tic-Tac-Toe and the correct outcomes appear
            then you succeeded in creating the function.
'''
def playGame():
    game_board = None
    while False:
        None

playGame()