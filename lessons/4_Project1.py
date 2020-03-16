"""
Practice Project 1: Coding an exit function
Created: 3/7/2020

In this project we will use what we learned from assignments 1, 2, and 3
to code a function called "project_1" that will do the following:

Inputs:
    1. f - a function that defines the mathematical formula: y = x^2
    2. input_val - the initial input value
    3. terminal_val - the terminating value

Functionality:
    1. Use a while loop to increment to the input value
        1a. The value added to input_val is based on the input function (f)
        1b. Use the number of loops as the x value for the function (f)
        1c. Thus: y = x^(num_loops)
        1d. Add y to the input_value each iteration of the loop
        1e. Increment the num_loops each loop
    2. Terminate the loop when the input value is greater than or equal to the terminal value

Return:
    1. The number of loop iterations it took for
        the input value to surpass the terminal value

This project has no real world application necessarily, but the description contains a lot of valuable
coding terminology that you need to be able to understand and replicate.

This is basically reading comprehension for code.
"""

from solutions.CheckSolutions import CheckSolutions
checkSolutions = CheckSolutions().projectSolutions

'''
Function: y = x^2
'''
def f(x):
    y = None
    return y

def project_1(f, input_val, terminal_val):
    num_loops = 0
    while None:
        None
        None
    return num_loops

print(project_1(f, 5, 10))
checkSolutions['project1'](project_1, f, 0, 15)
