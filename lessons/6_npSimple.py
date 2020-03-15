"""
Practice Group 6: Introduction Numpy
Created: 3/14/2020

In this assignment we will learn to manipulate lists from numpy in python.

Q and A:
Q: What makes python so powerful?
A: Python makes coding easier from a syntax perspective but it also
    has flexibility because there are lots of packages that can be imported
    that are super easy to use!

Q: What are packages in Python?
A: Packages are an easy way for programmers to use external code repositories
    in their own code. For example, if a user wanted to use a ping_pong package, the
    coder would import ping_pong and call certain methods such as: create_game
    add_player, hit_ball, etc. rather than coding the ping_pong class from scratch

Q: What is Numpy?
A: Numpy is a python package that has fundamental computing functions.
    Basic functionality of numpy includes mathematical formulas,
    multi-dimensional array objects, statistical operations, random simulations
    and more. For this tutorial we will mostly be using numpy's mathematical formulas
    and array objects. In this lesson, we will be exploring the array object functions
    to do the exact functions we used in the last tutorial.

Notes: We have used numpy before. At the beginning of each program, we import numpy as np.
        This means the numpy package can be used as np._something_. Previously we used
        np.random.randint(-100, 100) to generate random integers between -100 and 100.

Learning Outcomes:
1) Understand what a numpy array is
2) Iterate over all values in a numpy array
3) Get a specific index value from a numpy array
4) Add values to the end of a numpy array
5) Add values to the beginning of a numpy array
6) Remove value from specific indexes of a numpy array
7) Combine numpy arrays using numpy operators

Example 1 and 2 are completed as a template.
For each of the following examples, replace blank lines
with the correct functionality. If completed correctly, the checkSolutions
will print "Correct Solution" to the terminal.

After the imports, checkSolutions, and randInt, a bunch of arrays are
predefined. Do not edit these, but understand how the arrays are created

Note: What's nice about numpy rather than lists is that every time we append or delete
something from a numpy array, we create a new numpy array. That way we do not need to
use copy.deepcopy(list) like we did in the list section.
"""


import numpy as np
from solutions.CheckSolutions import CheckSolutions

checkSolutions = CheckSolutions().numpySimpleSolutions
randInt = lambda : np.random.randint(-100, 100)



# how to make various lists:
a = np.array(["You", " ", "can", " ", "learn", " ", "numpy!"])

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
    Code a loop that creates a string using the values from numpy array a
    Then return the string.
    
    Notice that numpy arrays act very similary to lists. There are much cooler 
    things that we can do with them though that makes our lives easier. 
'''
def ex1(a):
    string = ""
    for e in a:
        string += str(e)
    return string

checkSolutions['example1'](ex1, a)



'''
Example 2: 
    In one line, code a function that returns the sum of all the values in list b
'''
def ex2(b):
    return np.sum(b)

checkSolutions['example2'](ex2, b)



'''
Example 3: 
    Code a function that returns the third value in list b.
    
    Note 1: list index values start at index 0, not 1. 
    Note 2: the answer to this question based on the given list b is 3
            as observed from the list definition. Do not return 3, use the
            correct python syntax for accessing a value of an array by indexing.
    - Hint: same as before
'''
def ex3(b):
    return None

checkSolutions['example3'](ex3, b)



'''
Example 4: 
    Code a function that returns the sum of the 
    third value and fifth value of list b.
    
    Note 1: list index values start at index 0, not 1. 
    Note 2: the answer to this question based on the given list b is 3
            as observed from the list definition. Do not return 3, use the
            correct python syntax for accessing a value of an array by indexing.
    - Hint: same as before
'''
def ex4(b):
    return None

checkSolutions['example4'](ex4, b)



'''
Example 5: 
    Code a function that appends a new value to the end of b
    and calculate the sum of the values in b and returns the sum - do not use a loop. 

    Note: for help look up -> "Appending to numpy array in python."
    - Hint: np.append(_,_) np.sum()
'''
def ex5(b, new_number):
    return None

checkSolutions['example5'](ex5, b, 10)



'''
Example 6: 
    Code a function that inserts a new value to the front of list b
    and returns the sum of the new values in list b - do not use a loop to calculate the sum. 

    Note: for help look up -> "Inserting to numpy array in python."
    - Hing: np.insert(arr, index, num)
'''
def ex6(b, new_number):
    return None

checkSolutions['example6'](ex6, b, 10)



'''
Example 7: 
    Code a function that removes the first value from list b
    and returns the sum of the new values in list b - do not use a loop to calculate the sum. 

    Note: for help look up -> "delete element from numpy array in python."
    - Hint np.delete(arr, [indexes])
'''
def ex7(b):
    return None

checkSolutions['example7'](ex7, b)



'''
Example 8: 
    Code a function that removes the third value from list b
    and returns the sum of the new values in list b - do not use a loop to calculate the sum. 

    Note: for help look up -> "delete element from numpy array in python."
    - Hint np.delete(arr, [indexes])
'''
def ex8(b):
    return None

checkSolutions['example8'](ex8, b)



'''
Example 9: 
    Code a function that returns list c combined with list d. 
    ie. combine list c and d so the returned list looks like b

    Note: for help look up -> "Combining two numpy arrays in python."
    - Hint np.hstack( (_,_) ) or np.vstack( (_,_) )
'''
def ex9(c, d):
    return None

checkSolutions['example9'](ex9, c, d)



'''
Example 10: 
    Code a function that sums all values from list b, c, and d
    by combining list b, c, and d into a single list. 

    Note: for help look up -> "Combining two lists in python."
'''
def ex10(b, c, d):
    return None

checkSolutions['example10'](ex10, b, c, d)


print("------------------------------")


'''
This next section is a little more involved, exposing us to the real purpose of numpy.
Up to this point, everything we used could have been accomplished with lists, 
instead of numpy arrays. 

Learning Objectives: 
1. Loading Data from a numpy module
2. Get the shape of numpy arrays
3. Reshape numpy arrays
4. Use basic numpy operators for matrix transformations
5. Using basic numpy operators for matrix multiplication
'''

data_path = "../data/numpy60MeterDashEx.npy"

'''
Example 11: 
    Load the data from data/numpy60MeterDashEx.npy 
    and return the data.
    
    The data represented by this data set is a set of 60m sprint times.
'''
def ex11(path):
    return np.load(path)

checkSolutions['example11'](ex11, data_path)



'''
Example 12: 
    Using the function created in ex11, get the data from data_path
    then return (average_time, most_frequent_time, min_time, max_time)
    
    the most_frequent_time is the most difficult to derive:
    - Hints: 
        average_time -> np.average
        most_frequent_time -> np.bincount(data).argmax() 
                                the issue here is all the data must be integers, 
                                so start by converting the data from floating point 
                                numbers to integers by multiplying all data by 100.
                                Then converting the numpy array to an integer array using
                                .astype(int)
        to return more than one piece of data -> return (avg, mode, min, max)
'''
def ex12(path):
    data = ex11(path)
    return None

checkSolutions['example12'](ex12, data_path)



'''
Example 13: 
    Follow the same procedure from example 12, but instead of using the entire dataset
    use only the first 12 data points. You must use data slicing. 
    ex:     a = np.array([1, 2, 3, 4, 5])
            b = a[0:2]      =>      b: [1, 2]
            c = a[2:]       =>      c: [3, 4, 5]
    return the average, mode, min, and max of this data
'''
def ex13(path):
    return None

checkSolutions['example13'](ex13, data_path)



'''
Example 14: 
    Compare the first 12 races to the second 12 races and determine
    which 12 races were faster. 
    
    Use the metrics average, min and max. 
        Weight the average time as 12x, the min time as 6x, and max time as 3x
    Sum these three to get the "cost" of the set of 12 times. 
    
    ex:     avg_first_12 = 7.5      min = 7.0       max = 7.9   cost = 7.5*12 + 7.0*6 + 7.9*3
            avg_second_12 = 7.2     min = 7.0       max = 7.4   cost = 7.2*12 + 7.0*6 + 7.4*3
        in this case, the lower the cost, the better the set of races. 
    return the numpy array of data that was faster, and the cost of that dataset
'''
def ex14(path):
    first_12 = ex11(path)[0:12]
    second_12 = None
    cost_1 = 0
    cost_2 = 0
    if(cost_1 < cost_2):
        return (None, None)
    else:
        return (None, None)

checkSolutions['example14'](ex14, data_path)



'''
Example 15: 
    The last few questions were kind of tricky. Lets take a step back 
    and learn a few more numpy functions. 
    
    return the shape of the data
    np.shape(data)
'''
def ex15(path):
    return None

checkSolutions['example15'](ex15, data_path)



'''
Example 16: 
    Reshape the data from its current shape so that it has two dimensions of equal size (2, 12)
    np.reshape(data, shape)
'''
def ex16(path):
    return None

checkSolutions['example16'](ex16, data_path)




'''
Example 17: 
    Calculate the dot product of the first 12 datapoints with the second 12 datapoints
    np.dot(arr, arr)
    result is a single number - look up how dot product works if you forget
    
    return the dot product scalar
'''
def ex17(path):
    return None

checkSolutions['example17'](ex17, data_path)



'''
Example 18: 
    Calculate the outer product of the first 12 datapoints with the second 12 datapoints
    must use np.outer operator
    result is a (12x12) array
    
    return the 12x12 array
'''
def ex18(path):
    return None

checkSolutions['example18'](ex18, data_path)



'''
Example 19: 
    Calculate the inner product of the first 12 datapoints with the second 12 datapoints
    must use np.multiply or the * operator
    result is a 12x1 array
    
    return the inner product vector (12, 1)
'''
def ex19(path):
    return None

checkSolutions['example19'](ex19, data_path)



'''
Example 20: 
    Calculate the matrix product between the outer product (12x12) * inner_product (12x1) 
        all scaled by the dot product. 
        Calcluate the outer, inner, and dot products using the first 12 with the second 12
        datapoints. Use the functions from ex17, 18, 19. 
'''
def ex20(path):
    return None

checkSolutions['example20'](ex20, data_path)

