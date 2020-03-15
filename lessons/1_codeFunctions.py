"""
Practice Group 1: Coding Basic Functions
Created: 3/4/2020

In this assignment we will learn to code simple functions.

Learning Outcomes:
1) Define a function in python
2) Call a function in python
3) use basic arithmetic operations in python
4) use basic arithmetic operations from numpy package

Example 1 is completed as a template.
For each of the following examples, replace "None"
with the correct equation. If completed correctly, the checkSolutions
will print "Correct Solution" to the terminal.
All examples are solved with one line.

operations learned:
+ * / ** %
abs() np.exp() np.sqrt()
"""

import numpy as np
from solutions.CheckSolutions import CheckSolutions

checkSolutions = CheckSolutions().functionSolutions
randInt = lambda : np.random.randint(-100, 100)


'''
Example 1: 
    Code the function: a + b = c
    test function using various inputs
'''
def ex1(a, b):
    c = a + b
    return c
checkSolutions['example1'](ex1, 4, 5)

# randInt generates random # between -100 to 100 - good for testing
checkSolutions['example1'](ex1, randInt(), randInt())

'''
Example 2: 
    Code the function: a * b = c
    test function using various inputs using:
    checkSolutions.functionSolutions['example#'](function, test#, test#)
'''
def ex2(a, b):
    c = None
    return c
checkSolutions['example2'](ex2, randInt(), randInt())


'''
Example 3: 
    Code the function: a / b = c
'''
def ex3(a, b):
    c = None
    return c
checkSolutions['example3'](ex3, randInt(), randInt())


'''
Example 4: 
    Code the function: a^(b) = c
    google search "exponent in python" 
    Hint: do not use ^
'''
def ex4(a, b):
    c = None
    return c
checkSolutions['example4'](ex4, randInt(), randInt())


'''
Example 5: 
    Code the function: square_root(a) = c
    Hint: look at intro above at "operations learned"
'''
def ex5(a):
    b = None
    return b
checkSolutions['example5'](ex5, abs(randInt()))


'''
Example 6: 
    Code the function: remainder of a/b = c
    Hint: look at intro above at "operations learned"
'''
def ex6(a, b):
    c = None
    return c
checkSolutions['example6'](ex6, randInt(), randInt())


'''
Example 7: 
    Code the function: absolute_value a = b
    Hint: look at intro above at "operations learned"
'''
def ex7(a):
    b = None
    return b
checkSolutions['example7'](ex7, randInt())


'''
Example 8: 
    Code the function: e^a = b
    the e we want is: ln(e) = 1
    Hint: look at intro above at "operations learned"
'''
def ex8(a):
    b = None
    return b
checkSolutions['example8'](ex8, randInt())


'''
Example 9: 
    Code the function: y= mx+b
'''
def ex9(m, x, b):
    y = None
    return y
checkSolutions['example9'](ex9, randInt(), randInt(), randInt())


'''
Example 10: 
    Code the function: 
        Given sides a and b of a right triangle, find hypotenuse c
'''
def ex10(a, b):
    c = None
    return c
checkSolutions['example10'](ex10, randInt(), randInt())


'''
Example 11: 
    Code the function: 
        Potential Energy = mass * gravity * height
        use 9.8 for gravity
'''
def ex11(m, h):
    pe = None
    return pe
checkSolutions['example11'](ex11, randInt(), randInt())


'''
Example 12: 
    Code the function: 
        Kinetic Energy = 1/2 * mass * velocity^2
'''
def ex12(m, v):
    ke = None
    return ke
checkSolutions['example12'](ex12, randInt(), randInt())


'''
Example 13: 
    Code the function: sigmoid
    sigmoid: y = e^x / (1 + e^x)
'''
def ex13(x):
    y = None
    return y
checkSolutions['example13'](ex13, randInt())


'''
Example 14: 
    Code the function: tanh
    tanh: y = (e^x - e^(-x))/(e^(x) + e^(-x))
'''
def ex14(x):
    y = None
    return y
checkSolutions['example14'](ex14, randInt())

