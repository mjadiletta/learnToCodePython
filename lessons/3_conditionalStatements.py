"""
Practice Group 3: Coding Conditional Statements
Created: 3/7/2020

In this assignment we will learn to code conditional statements.
We have already been introduced to conditional statements from while loops.
This is more detailed practice.

Learning Outcomes:
1) Be able to use if else statements
2) use conditional operators such as: > < == <= >= !=

Example 1 is completed as a template.
For each of the following examples, replace blank lines
with the correct equation. If completed correctly, the checkSolutions
will print "Correct Solution" to the terminal.
"""

import numpy as np
from solutions.CheckSolutions import CheckSolutions

checkSolutions = CheckSolutions().conditionalSolutions
randInt = lambda: np.random.randint(-100, 100)

'''
Example 1: 
    use a conditional if else statement to return 
    the largest number between inputs a and b.
'''
def ex1(a, b):
    if a > b:
        return a
    else:
        return b

checkSolutions['example1'](ex1, 5, 6)


'''
Example 2: 
    use a conditional if else statement to return 
    the smaller number between inputs a and b.
'''
def ex2(a, b):
    if None:
        return None
    else:
        return None

checkSolutions['example2'](ex2, 5, 6)

'''
Example 3: 
    use a conditional if else statement to return 
    0 if the number if a equals be or the lower of the two numbers
'''
def ex3(a, b):
    if None:
        return None
    else:
        if None:
            return None
        else:
            return None

checkSolutions['example3'](ex3, randInt(), randInt())

'''
Example 4: 
    use a conditional if else statement to return the larger number between: 
    a^2 / 5 and b^3 / 3
'''
def ex4(a, b):
    if None:
        return None
    else:
        return None

checkSolutions['example4'](ex4, randInt(), randInt())








