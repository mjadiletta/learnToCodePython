"""
Practice Group 10: Using Lists for Sorting
Created: 3/16/2020

In this tutorial we will cover sorting algorithms.
We will start by allowing you to use any sorting algorithm you can
in order to sort lists by yourself. Just produce the correctly sorted list.

Later we will learn 7 types of sorting algorithms:
    1. Bubble Sort
    2. Insertion Sort
    3. Selection Sort
    4. Quick Sort
    5. Merge Sort
    6. Heap Sort
    7. Counting Sort

Sorting algorithms are fundamental to understanding how to code!
I provide explanations for each of these sorting methods, but more
detailed explanations can be found here: https://www.studytonight.com/data-structures/

Example 1 is completed as a template.
For each of the following examples, replace blank lines
with the correct functionality. If completed correctly, the checkSolutions
will print "Correct Solution" to the terminal.
"""

import numpy as np
import copy
from solutions.CheckSolutions import CheckSolutions

checkSolutions = CheckSolutions().listComplexSolutions
randInt = lambda : np.random.randint(-100, 100)

list_a = [1, 9, 5, 3, 2, 7, 8, 4, 6]


'''
Example 1: 
    Code a loop that sorts list_a from lowest value to highest value. 
    You are allowed to append lists to a new new_list 
    return the correctly sorted new_list
'''
def ex1(list_a):
    new_list = []
    for index_1 in range(len(list_a)):
        current_min_value = np.inf
        for index_2 in range(len(list_a)):
            None
    return new_list

# make a copy of a, not needed for this problem but in others is necessary
print(ex1(copy.deepcopy(list_a)))
checkSolutions['example1'](ex1, copy.deepcopy(list_a))