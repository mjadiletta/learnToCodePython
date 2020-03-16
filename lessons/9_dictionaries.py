"""
Practice Group 9: Dictionaries
Created: 3/15/2020

In this assignment we will learn to manipulate dictionaries in python.

Dictionaries are a python datastructure, similar to lists. They are
different for a number of reasons. First, instead of accessing elements
of a dictionary by index, we access elements of a dictionary by key's.
Every key has an associated value. A simple dictionary example is shown below:

Example:
    dict = {
              "key": "value",
              "key": "value",
              ...
            }

    car_dictionary = {
                        "toyota": ["corolla", "rav4", "camry"],
                        "honda" : ["civic", "fit", "accord"],
                        "ford": ["mustang", "explorer", "ranger", "F-150", "Fusion"]
                     }

    car_dictionary["toyota"] => ["corolla", "rav4", "camry"]
    car_dictionary["toyota"][1] => "rav4"
    car_dictionary["toyota"] + car_dictionary["ford"] => ["corolla", "rav4", "camry", "mustang", "explorer", "ranger", "F-150", "Fusion"]
    car_dictionary["toyota"][1] + car_dictionary["ford"][3] => "rav4F-150"


Learning Outcomes:
1) Understand what a dictionary is
2) Iterate over all key, values in a dictionary
3) Get a specific element from a dictionary
4) Add values to a dictionary
6) Remove value using a specific key from a dictionary
7) Combine dictionaries

Example 1 is completed as a template.
For each of the following examples, replace blank lines
with the correct functionality. If completed correctly, the checkSolutions
will print "Correct Solution" to the terminal.

After the imports, checkSolutions, and randInt, a bunch of arrays are
predefined. Do not edit these, but understand how the lists are created

"""

import numpy as np
import matplotlib.pyplot as plt
from solutions.CheckSolutions import CheckSolutions

checkSolutions = CheckSolutions().dictionarySolutions
randInt = lambda : np.random.randint(-100, 100)


'''
Example 1: 
    Create a dictionary that sorts the data shown below:
    "car", "wings", "6 wheels", "steering wheel", "4 doors"
    "2 wheels", "plane","no doors"
    "4 wheels", "motorcycle", "emergency exits"
'''
def ex1():
    sorted_dictionary = {"car": ["4 wheels", "steering wheel", "4 doors"],
                         "motorcycle": ["2 wheels", "no doors"],
                         "plane": ["6 wheels", "wings", "emergency exits"]}
    return sorted_dictionary

checkSolutions['example1'](ex1)


'''
Example 2: 
    Create a dictionary that sorts the data shown below:
    "pencil", "dinner", "eraser", "cheese",
    "milk", "pizza", "pen", "potatoes"
    "school_materials", "steak", "dairy"
'''
def ex2():
    sorted_dictionary = {}
    return sorted_dictionary

checkSolutions['example2'](ex2)


'''
Example 3:
    For this example, create a list of keys from the dictionary 
    you created in example2. To do this, first call ex2() to 
    create the dictionary. Then iterate over the dictionaries keys using:
    
    for key in dict.keys():
    
    append each key to a list and return the list
'''
def ex3():
    key_list = []


    return key_list

checkSolutions['example3'](ex3)



'''
Example 4:
    For this example, create a list of all values from the dictionary 
    you created in example2. To do this, first call ex2() to 
    create the dictionary. Then iterate over the dictionaries values using:

    for value in dict.values():

    Note that the value is actually an array, not each individual element. 
    You must iterate over each element of value and append that to a value_list
    return the value_list
'''
def ex4():
    value_list = []



    return value_list

checkSolutions['example4'](ex4)



'''
Example 5:
    For this example, create two lists. The first list is a list of all
    the keys and the second list is all the values from the dictionary 
    created in example1.
    
    Use only 2 loops total. You could just copy the code you wrote for 
    ex3 and ex4 but using the ex1 dictionary. Do not do this. Combine the two
    by using this for loop dictionary technique:
    
    for key, value in dictionary.items():
        - dictionary.items() returns key, value pairs. 
    
    return key_list, value_list
'''
def ex5():
    key_list = []
    value_list = []




    return key_list, value_list

checkSolutions['example5'](ex5)



'''
Example 6:
    Create a new dictionary that combines the dictionaries from ex1() and ex2()
    return the new dictionary
    
    There is no simple python trick for this. Use a loop, and build the new dictionary.
'''
def ex6():
    new_dict = {}




    return new_dict

checkSolutions['example6'](ex6)



'''
Example 7:
    In the data folder there are 4 numpy data sets:
        brian_damore200Meter.npy
        antoine_harris200Meter.npy
        tyler_hanson200Meter.npy
        alex_rus200Meter.npy
    Create a dictionary with the key being the name of the data set minus "200Meter.npy", 
    and the values being the list of dat points. 
    
    dict = {"brian_damore": [data points], "antoine_harris": [data points], 
            "tyler_hanson": [data points], "alex_rus": [data points]}
    
    return dict
'''
def ex7():
    track_dict = {}
    return track_dict

checkSolutions['example7'](ex7)


'''
Example 8:
    Using the dictionary you created for example 7, create a graph using matplotlib with four subplots
    displaying each athletes progression over time. That means use a line plot. 
    
    return the x, y points for each athlete.
    return (x_brian, y_brian, x_antoine, y_antoine, x_tyler, y_tyler, x_alex, y_alex)
    
    check the solution of your image: solutions/9_dictionariesSolutionsImages/example8Solution.png
'''
def ex8():

    x_brian = None
    y_brian = None
    x_antoine = None
    y_antoine = None
    x_tyler = None
    y_tyler = None
    x_alex = None
    y_alex = None

    figure, axes = plt.subplots(figsize=(8, 8), nrows=2, ncols=2)

    ax1 = axes[0][0]
    ax2 = axes[0][1]
    ax3 = axes[1][0]
    ax4 = axes[1][1]

    # Subplot 1 Brian--------------------------------------------------------------------------------
    ax1.plot(0, 0)
    ax1.set(xlabel='race', ylabel='time (s)', title='Brian 200m Dash Race Progression')
    ax1.grid()  # add a grid to the graph if you want

    # Subplot 2 Antoine------------------------------------------------------------------------------
    ax2.plot(0, 0)
    ax2.set(xlabel='race', ylabel='time (s)', title='Antoine 200m Dash Race Progression')
    ax2.grid()  # add a grid to the graph if you want

    # Subplot 3 Tyler--------------------------------------------------------------------------------
    ax3.plot(0, 0)
    ax3.set(xlabel='race', ylabel='time (s)', title='Tyler 200m Dash Race Progression')
    ax3.grid()  # add a grid to the graph if you want

    # Subplot 4 Alex---------------------------------------------------------------------------------
    ax4.plot(0, 0)
    ax4.set(xlabel='race', ylabel='time (s)', title='Rus 200m Dash Race Progression')
    ax4.grid()  # add a grid to the graph if you want

    figure.tight_layout(pad=1.5)
    #plt.show()
    plt.close()
    return (x_brian, y_brian, x_antoine, y_antoine, x_tyler, y_tyler, x_alex, y_alex)

checkSolutions['example8'](ex8)
