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