"""
Practice Group 5: Introduction to Lists
Created: 3/13/2020

In this assignment we will learn to manipulate lists in python.

Learning Outcomes:
1) Understand what a list is
2) Iterate over all values in a list
3) Get a specific index value from a list
4) Add values to the end of a list
5) Add values to the beginning of a list
6) Remove value from specific indexes of a list
7) Combine lists using list operators

Example 1 is completed as a template.
For each of the following examples, replace blank lines
with the correct functionality. If completed correctly, the checkSolutions
will print "Correct Solution" to the terminal.

After the imports, checkSolutions, and randInt, a bunch of arrays are
predefined. Do not edit these, but understand how the lists are created

Note: before using a list, you must call the list using copy.deepcopy("list")
that way you do not alter the original list
"""

import numpy as np
import copy
from solutions.CheckSolutions import CheckSolutions

checkSolutions = CheckSolutions().listSimpleSolutions
randInt = lambda : np.random.randint(-100, 100)

# how to make various lists:
a = list()
a.append("You")
a.append(" ")
a.append("can")
a.append(" ")
a.append("learn")
a.append(" ")
a.append("python!")

b = [5, 2, 3, 4, 1]
c = b[0:2]
d = b[2:]

print("list a: " + str(a))
print("list b: " + str(b))
print("list c: " + str(c))
print("list d: " + str(d))

print("------------------------------")


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



'''
Example 2: 
    Code a function using a loop that returns the sum of all the values in list b
'''
def ex2(list_b):
    sum = 0



    return sum

checkSolutions['example2'](ex2, copy.deepcopy(b))



'''
Example 3: 
    Code a function that returns the third value in list b.
    
    Note 1: list index values start at index 0, not 1. 
    Note 2: the answer to this question based on the given list b is 3
            as observed from the list definition (line 45). Do not return 3, use the
            correct python syntax for accessing a value of an array by indexing.
            
    Hint: search "accessing list index python"
'''
def ex3(list_b):
    return None

checkSolutions['example3'](ex3, copy.deepcopy(b))



'''
Example 4: 
    Code a function that returns the sum of the 
    third value and fifth value of list b.
    
    Note 1: list index values start at index 0, not 1. 
    Note 2: the answer to this question based on the given list b is 3+1 = 4
            as observed from the list definition. Do not return 4, use the
            correct python syntax for accessing a value of an array by indexing.
'''
def ex4(list_b):
    return None

checkSolutions['example4'](ex4, copy.deepcopy(b))



'''
Example 5: 
    Code a function that appends a new value to the end of b
    and calculate the sum of the values in b and returns the sum - use a loop. 

    Note: for help look up -> "Appending to list in python."
'''
def ex5(list_b, new_number):
    sum = 0



    return sum

checkSolutions['example5'](ex5, copy.deepcopy(b), 10)



'''
Example 6: 
    Code a function that inserts a new value to the front of list b
    and returns the sum of the new values in list b - use a loop to calculate the sum. 

    Note: for help look up -> "Inserting to list in python."
    - Hint: list.insert(,)
'''
def ex6(list_b, new_number):
    sum = 0



    return sum

checkSolutions['example6'](ex6, copy.deepcopy(b), 10)



'''
Example 7: 
    Code a function that removes the first value from list b
    and returns the sum of the new values in list b - use a loop to calculate the sum. 

    Note: for help look up -> "pop element off list in python."
    - Hint list.pop(_)
'''
def ex7(list_b):
    sum = 0



    return sum

checkSolutions['example7'](ex7, copy.deepcopy(b))



'''
Example 8: 
    Code a function that removes the third value from list b
    and returns the sum of the new values in list b - use a loop to calculate the sum. 

    Note: for help look up -> "pop element off list in python."
    - Hint list.pop(_)
'''
def ex8(list_b):
    sum = 0



    return sum

checkSolutions['example8'](ex8, copy.deepcopy(b))



'''
Example 9: 
    Code a function that returns list c combined with list d. 
    ie. combine list c and d so the returned list looks like b

    Note: for help look up -> "Combining two lists in python."
'''
def ex9(list_c, list_d):
    return None

checkSolutions['example9'](ex9, copy.deepcopy(c), copy.deepcopy(d))



'''
Example 10: 
    Code a function that sums all values from list b, c, and d
    by combining list b, c, and d into a single list. 

    Note: for help look up -> "Combining two lists in python."
'''
def ex10(list_b, list_c, list_d):
    sum = 0



    return sum

checkSolutions['example10'](ex10, copy.deepcopy(b), copy.deepcopy(c), copy.deepcopy(d))

