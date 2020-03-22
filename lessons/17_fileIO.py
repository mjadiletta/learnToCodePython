"""
Practice Group 17: File Input and Output
Created: 3/21/2020

Reading and writing to files in python is crucial for creating programs that
require external data, output lots of data, etc. There are a number of ways
to read and write files in python. We will talk about two. The most common way
is to use python's open() function which will return a "file object". The second
way is to use "with open() as file:"

In either case, there are 3 modes you can use to open a file.
    1. Read only: "r"
    2. Write only: "w"
        - Write deletes everything that was originally in the file.
    3. Append to File: "a"
        - Append writes to the end of the file, leaving everything in the file originally.

Open Function:
    open("filename", "mode")

    General Read Structure:
        file = open("filename", "r")
        for line in file:
            # do something with the line
        file.close()

        Other read functions:
            file.read()  # returns the whole file
            file.readlines()  # returns a list of lines in the file
            file.readline(3)  # returns line 3


    General Write Structure:
        file = open("filename", "w")
        file.write("Whatever you want")
        file.close()

        Other write / append functions:
            file.writelines(list of lines to write)

With Open Function:
    with open("filename", "mode"):
    The benefit of the with open method is that you don't need to remember to
    close() the file, because as long as you're in the "with open" tab space,
    then the file is open. But if you leave the "with open" tab space, then the
    file closes automatically.

    General Read Structure:
        with open("filename", "r") as file:
            data = file.readlines()

    General Write Structure:
        with open("filename", "w") as file:
            file.write("Whatever you want")

Another thing we need to look at is string parsing. When we read from a file
we are reading "strings." The following is a list of string methods python
offers that are necessary to parse data from a file.

string_a = "test this string"
string)b = "second string\n"
    *   string_a.split(" ")      ->      ["test", "this", "string"]
    *   string_a.split("t")      ->      ["est ", "his ", "s", "ring"]
    *   string_b.rstrip("\n")    ->      "second string"
    *   string_b.replace("s", "S") ->    "Second String\n"

    *   joining_string = "."
    *   joining_string.join(string_a.split(" "))    ->      "test.this.string"

Other string methods: https://www.w3schools.com/python/python_ref_string.asp


In this tutorial we will cover how to open a file and close a file in python.

Learning Objectives:
    1. Read the text file as input to a program
        - Create a text parser
    2. Create a new text file in pyCharm
    3. Write to a text file as output of a program
    4. Redirect standard output std.out

Example 1 is completed as a template.
For each of the following examples, replace blank lines
with the correct functionality. If completed correctly, the checkSolutions
will print "Correct Solution" to the terminal.
"""

import sys
from solutions.CheckSolutions import CheckSolutions
checkSolutions = CheckSolutions().fileIOSolutions

print("----------------------------")

'''
Example 1: 
    Read the file "../fileIO/text1.txt" and print the contents to the terminal.
'''
def ex1():
    file = open("../fileIO/text1.txt", 'r')
    print(file.read())
    file.close()

checkSolutions['example1'](ex1)
print("----------------------------")



'''
Example 2: 
    Read the file "../fileIO/text1.txt" and 
    print the third line to the terminal as a string
    Note: Don't forget to close the file using file.close()

    Hint: use file.readlines()
'''
def ex2():
    file = None

checkSolutions['example2'](ex2)
print("----------------------------")



'''
Example 3: 
    Read the file "../fileIO/text1.txt" and 
    print the second line to the terminal after
    1. splitting the string by the character ' '.
    
    Note: Don't forget to close the file using file.close()
'''
def ex3():
    file = None

checkSolutions['example3'](ex3)
print("----------------------------")



'''
Example 4: 
    Read the file "../fileIO/text1.txt" and 
    print the last line to the terminal after
    1. splitting the string by the character ' '
    2. replacing all occurances of "t" with "!".
    
    Note: Don't forget to close the file using file.close()
'''
def ex4():
    file = None

checkSolutions['example4'](ex4)
print("----------------------------")



'''
Example 5: 
    Read the file "../fileIO/text1.txt" and 
    print the first line to the terminal after
    1. splitting the string by the character ' '
    2. replacing all occurances of "R" with "r"
    3. changing the third word to "useless"
    4. appending "You" to the beginning of the list
    5. joining the list back together with character ' ' to create a new string
    
    Note: Don't forget to close the file using file.close()
'''
def ex5():
    file = None

checkSolutions['example5'](ex5)
print("----------------------------")


'''
Example 6: 
    Write to the file "../fileIO/out1.txt" 
    the exact contents in file "../fileIO/text1.txt"
    using fileOut.writelines(data)
    
    Note: Don't forget to close the file using file.close()
'''
def ex6():
    fileIn = None
    fileOut = None

checkSolutions['example6'](ex6)
print("----------------------------")



'''
Example 7:
    For this example, we will learn to redirect the standard output!
    But what is the standard output? The simple answer is that the standard
    output is where your print statements are sent. For example, when you
    initially run a program, the standard output (sys.stdout) is the terminal. 
    This is why when you type print("HERE"), "HERE" appears in the terminal. 
    
    But we can change this location to where ever we want! 
    
    For this example, we will redirect the standard output from the terminal to a file.
    
    There are three steps for this example to show you know how to redirect the standard output: 
    1. print "Printing to the Terminal!" in the terminal
    2. redirect the standard output to the file "../fileIO/out1.txt"
        and print "Printing to the Out1.txt File!"
    3. redirect the standard output to the terminal again 
        and print "Printing Back to the Terminal!"
        
    Notes:
        - to change the standard output, set the variable sys.stdout
        - when you initialize a program the sys.stdout = terminal
            * to preserve the location of the terminal, store sys.stdout in a variable called temp1
                before setting sys.stdout the open file "out1.txt"
            * note you still need to close the file after writing to it
        - when you revert back to the terminal, just set sys.stdout = temp1. 
        
        - make sure your print statements are the exact same as the question asks. 
'''
def ex7():
    temp1 = None
    f = None
    sys.stdout = None

checkSolutions['example7'](ex7)
print("----------------------------")



'''
Example 8: 
    For lecture 12 / project 3 you were asked to create a TicTacToe game. 
    The game was played in the terminal. 
    
    For example 8 we will:
    1. read a file from fileIO called "../fileIO/ticTacToeBoard1.txt"
    2. load the board as a playable tictactoe gameboard
        - You will need to use a similar function to the createBoard() function
        - Instead of initializing all spots to '-',
            initialize the 3x3 array with the correct character from the input file
    3. play the game from this configuration
    4. instead of printing the display to the terminal, we will print
        to an output file called "../fileIO/ticTacToeOut". 
        
    Note: In the case that your solution was not perfect, I created a file called
    ticTacToeSolutions.py in the solutions folder which has a class called TicTacToe. 
    I have already imported this class for you. It has a function called 
        playGame(game_board) 
    Which will have 2 CPU's play each other starting from the game_board configuration.
    
    Redirect the print statements from the terminal to the output file. (Do not edit the ticTacToeSolutions.py!!) 
'''

'''
    Example 8a:
        Write the function createBoard() that reads "../fileIO/ticTacToeBoard1.txt"
        and returns the equivalent game_board. 
        
        Hint: use replace and split to edit the input until you return a row that possibly looks like:
            ['X', 'O', '-']
            Then append it to the game_board
            
            Final game_board should be shape (3x3) with only characters '-', 'X', or 'O'
'''
def createBoard():
    game_board = []
    inputFile = None

    return game_board

checkSolutions['example8a'](createBoard)
print("----------------------------")



'''
    Example 8b:
        Instantiate the correct game board from the file - use your fuction from 8a.
        
        Redirect playGame(game_board) so that the output isn't printed to the terminal
        rather is printed to "../fileIO/ticTacToeOut.txt"
        
        After redirecting the output to the ticTacToeOut.txt, return the stdout back to
        it's original location (the terminal) and print "Fixed the output!" in the terminal.
'''
from solutions.ticTacToeSolution import ticTacToe
def playGameFromBoard():
    tTT = ticTacToe()
    game_board = createBoard()

    #tTT.playGame(game_board)


checkSolutions['example8b'](playGameFromBoard, createBoard())

