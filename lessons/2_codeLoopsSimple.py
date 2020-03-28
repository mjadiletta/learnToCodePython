"""
Practice Group 2: Coding Simple Loops
Created: 3/6/2020

In this assignment we will learn to code simple loops.

Learning Outcomes:
1) Define a function in python
2) Call a function in python
3) Use basic loop styles in python

Example 1 is completed as a template.
For each of the following examples, replace blank lines
with the correct equation. If completed correctly, the checkSolutions
will print "Correct Solution" to the terminal.

techniques learned:
for loop
while loop
"""

import numpy as np
from solutions.CheckSolutions import CheckSolutions

checkSolutions = CheckSolutions().loopSolutions
randInt = lambda : np.random.randint(-100, 100)

'''
Example 1: 
    Code a for loop that creates the string "0 1 2 3 4 5 "
    Then return the string.
'''
def ex1():
    string = ""
    for i in range(0, 6):
        string += str(i) + " "
    return string

checkSolutions['example1'](ex1)


'''
Example 2: 
    Code a for loop that creates the string "012345"
    Then return the string.
'''
def ex2():
    string = ""


    return string

checkSolutions['example2'](ex2)


'''
Example 3: 
    Code a for loop that creates the string "6789"
    Then return the string.
'''
def ex3():
    string = ""


    return string

checkSolutions['example3'](ex3)


'''
Example 4: 
    Code a for loop that finds the sum of 0 - 5 inclusive
    Then return the sum.
'''
def ex4():
    sum = 0


    return sum

checkSolutions['example4'](ex4)


'''
Example 5: 
    Code a for loop that finds the sum of the numbers between two integers
        Then return the sum.
    ex: ex5(20, 25) = 20 + 21 + 22 + 23 + 24
'''
def ex5(a, b):
    sum = 0


    return sum

checkSolutions['example5'](ex5, 20, 25)


'''
repeat examples 1 - 5 but instead of using a for loop, use a while loop
'''


'''
Example 6: Completed as an example :)
    Code a while loop that creates the string "0 1 2 3 4 5 "
    Then return the string.
'''
def ex6():
    string = ""
    i = 0
    while i < 6:
        string += str(i) + " "
        i += 1
    return string

checkSolutions['example6'](ex6)


'''
Example 7: 
    Code a while loop that creates the string "012345"
    Then return the string.
'''
def ex7():
    string = ""



    return string

checkSolutions['example7'](ex7)


'''
Example 8: 
    Code a while loop that creates the string "6789"
    Then return the string.
'''
def ex8():
    string = ""



    return string

checkSolutions['example8'](ex8)


'''
Example 9: 
    Code a while loop that finds the sum of 0 - 5
    Then return the sum.
'''
def ex9():
    sum = 0



    return sum

checkSolutions['example9'](ex9)


'''
Example 10: 
    Code a while loop that finds the sum of the numbers between two integers
        Then return the sum.
        assume input a is always  less than input b
    ex: ex5(20, 25) = 20 + 21 + 22 + 23 + 24
'''
def ex10(a, b):
    sum = 0



    return sum

checkSolutions['example10'](ex10, 20, 25)


'''
Example 11: 
    Code a loop that multiplies a by b
    - do not use multiplication operator *
    example: a = 2, b = 3
    ans: 2 + 2 + 2 = 6
'''
def ex11(a, b):
    ans = 0


    return ans

checkSolutions['example11'](ex11, 2, 3)

