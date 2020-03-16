"""
Practice Group 11: Using Numpy for matrix multiplication
Created: 3/16/2020
Adopted from Prof. Whitehill CS 453x HW1 and CS/DS 541

Matrix multiplication is a fundamental component to all Machine Learning Algorithms
and most problems in general. We explored numpy in lecture 6 previously. In this
lecture, we will explore numpy matrix multiplication.

learning objectives:
1) matrix addition and subtraction
2) matrix multiplication and inverses
3) creating matrices in numpy
4) transposing matrices in numpy
5) accessing elements of multidimensional arrays
6) summing across rows of 2D arrays to create a 1D array

Example 1 is completed as a template.
For each of the following examples, replace blank lines
with the correct functionality. If completed correctly, the checkSolutions
will print "Correct Solution" to the terminal.
"""

import numpy as np
from solutions.CheckSolutions import CheckSolutions

checkSolutions = CheckSolutions().numpyComplexSolutions

a = np.array([[1, 2, 3], [6, 3, 2], [9, 9, 9]])  # 3x3
b = np.array([[2, 5, 3], [4, 4, 2], [1, 2, 3]])  # 3x3
c = np.array([[1, 2, 1], [4, 5, 5], [6, 7, 8]])  # 3x3
d = np.array([[1, 2, 3]])  # 1x3
cv1 = np.array([1, 2, 3])  # 3,
cv2 = np.array([4, 5, 6])  # 3,

'''
Example 1: 
    return the shape of a numpy array
'''
def ex1(array):
    return np.shape(array)

checkSolutions['example1'](ex1, a)



'''
Example 2: 
    return the sum of two arrays if their dimensions are the same. 
    if they are not the same, then do not sum them and return -1
'''
def ex2(a, b):
    if None:
        return None
    else:
        return None

checkSolutions['example2'](ex2, a, b)



'''
Example 3: 
    return the element-wise product of two arrays (a and b) and add the transpose of a third array (c)
    only do this if all their dimensions are the same. 
    if the dimensions are not the same, then do not sum them and return -1. 
'''
def ex3(a, b, c):
    if None:
        return None
    else:
        return None

checkSolutions['example3'](ex3, a, b, c)
checkSolutions['example3'](ex3, a, b, d)



'''
Example 4: 
    Given two column vectors (a, b) - a column vector is a 1 dimensional array
    compute the inner product, ie (dot product)
'''
def ex4(a, b):
    return None

checkSolutions['example4'](ex4, cv1, cv2)



'''
Example 5: 
    Given a matrix A, return a matrix of all zeros with the same dimensions.
    Hint: look up numpy.zeros 
'''
def ex5(A):
    return None

checkSolutions['example5'](ex5, a)



'''
Example 6: 
    Given a 2D matrix A, return a vector of all one of length (num rows in A).
    Hint: look up numpy.ones 
'''
def ex6(A):
    return None

checkSolutions['example6'](ex6, a)



'''
Example 7: 
    Given a square matrix A and a scalar alpha, 
    return A + alpha*I where I is the identity matrix of shape A
    Hint: look up numpy.eye
'''
def ex7(A, alpha):
    return None

checkSolutions['example7'](ex7, a, 5)



'''
Example 8: 
    Given a 2D matrix A 
    return the i, j where i is the ith row and j is the jth column
    Hint: look up indexing 2D numpy array
'''
def ex8(A, i, j):
    return None

checkSolutions['example8'](ex8, a, 1, 2)



'''
Example 9: 
    Given a 2D matrix A and integer i, 
    return the sum of all the entries in row i
    Note: do not use a loop! Use np.sum()
'''
def ex9(A, i):
    return None

checkSolutions['example9'](ex9, a, 1)



'''
Example 10: 
    Given matrix A and scalars c, d:
    compute the arithmetic mean over all entries of A that
    are between c and d (inclusive).
    
    ex: a = [[1, 2, 0], [4, 3, 1]]    c = 1       d = 3 
    ans = (1 + 2 + 3 + 1)/4 = 7/4
    
    Note: do not use a loop! 
    Hint: use np.nonzero and np.mean
'''
def ex10(A, c, d):

    return None

checkSolutions['example10'](ex10, a, 1, 3)



'''
Example 11: 
    Given matrix A and column vector x, 
    use np.linalg.solve to compute A^(-1)x
    Do not use np.linalg.inv or A**-1 because this is numerically unstable. 
        It can make a big difference!    
    
    read: https://docs.scipy.org/doc/numpy/reference/generated/numpy.linalg.solve.html
    
    Hint: 
        np.linalg.solve(a, b) = c such that a*c = b
        Note A^(-1)x = m    =>   A*m = x  
'''
def ex11(A, x):
    return None

checkSolutions['example11'](ex11, a, cv1)
