"""
Practice Project 1: Coding an exit function
Created: 3/7/2020

In this project we will use what we learned from assignments 1, 2, and 3
to code a function that will:

3 Inputs:
    1. A function that defines the mathematical formula: y = x^2
    2. Input value
    3. Terminating value

Functionality:
1. Use a while loop to increment to the input value
    1a. The value added to input_val is based on the input function
    1b. Use the number of loops as the x value for the function
    1c. Thus: y = x^(num_loops) and add y to the input_value
2. Terminate the loop when the input value is greater than or equal to the terminal value

Return:
1. Return the number of loop iterations it took for
   the input value to surpass the terminal value
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
    return num_loops

print(project_1(f, 5, 10))
checkSolutions['project1'](project_1, f, 0, 15)
