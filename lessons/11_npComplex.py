"""
Practice Group 11: Using Numpy for matrix multiplication
Created: 3/16/2020


Example 1 is completed as a template.
For each of the following examples, replace blank lines
with the correct functionality. If completed correctly, the checkSolutions
will print "Correct Solution" to the terminal.
"""

import numpy as np
import copy
from solutions.CheckSolutions import CheckSolutions

checkSolutions = CheckSolutions().numpyComplexSolutions
randInt = lambda : np.random.randint(-100, 100)

a = ["test", " ", "this"]

'''
Example 1: 
    Code a loop that creates a string using the values from list a
    Then return the string.
'''
def ex1(list_a):
    string = ""
    for element in list_a:
        string += element
    return string

# make a copy of a, not needed for this problem but in others is necessary
print(ex1(copy.deepcopy(a)))
checkSolutions['example1'](ex1, copy.deepcopy(a))