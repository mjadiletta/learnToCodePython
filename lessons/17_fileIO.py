"""
Practice Group 17: File Input and Output
Created: 3/__/2020

Reading and writing to files in python is crucial for creating programs that
require external data, output lots of data, etc. There are a number of ways
to read and write files in python. We will talk about two. The most common way
is to use python's open() function which will return a "file object". The second
way is to use "with open() as file:"

In either case, there are 3 modes you can use to open a file.
    1. Read only: "r"
    2. Write only: "w"
        - Write deletes everything that was originally in the file.
    3. Append to File: "a"
        - Append writes to the end of the file, leaving everything in the file originally.

Open Function:
    open("filename", "mode")

    General Read Structure:
        file = open("filename", "r")
        for line in file:
            # do something with the line
        file.close()

        Other read functions:
            file.read()  # returns the whole file
            file.readlines()  # returns a list of lines in the file
            file.readline(3)  # returns line 3


    General Write Structure:
        file = open("filename", "w")
        file.write("Whatever you want")
        file.close()

        Other write / append functions:
            file.writelines(list of lines to write)

With Open Function:
    with open("filename", "mode"):
    The benefit of the with open method is that you don't need to remember to
    close() the file, because as long as you're in the "with open" tab space,
    then the file is open. But if you leave the "with open" tab space, then the
    file closes automatically.

    General Read Structure:
        with open("filename", "r") as file:
            data = file.readlines()

    General Write Structure:
        with open("filename", "w") as file:
            file.write("Whatever you want")

Another thing we need to look at is string parsing. When we read from a file
we are reading "strings." The following is a list of string methods python
offers that are necessary to parse data from a file.

string_a = "test this string"
string)b = "second string\n"
    *   string_a.split(" ")      ->      ["test", "this", "string"]
    *   string_a.split("t")      ->      ["est ", "his ", "s", "ring"]
    *   string_b.rstrip("\n")    ->      "second string"
    *   string_b.replace("s", "S") ->    "Second String\n"

    *   joining_string = "."
    *   joining_string.join(string_a.split(" "))    ->      "test.this.string"

Other string methods: https://www.w3schools.com/python/python_ref_string.asp


In this tutorial we will cover how to open a file and close a file in python.

Learning Objectives:
    1. Read the text file as input to a program
        - Create a text parser
    2. Create a new text file in pyCharm
    3. Write to a text file as output of a program
    4. Re-direct print statements to a file rather than the console
    5. Understand what std.in and std.out are and how they can be used for fileIO

Example 1 is completed as a template.
For each of the following examples, replace blank lines
with the correct functionality. If completed correctly, the checkSolutions
will print "Correct Solution" to the terminal.
"""

import numpy as np
from solutions.CheckSolutions import CheckSolutions
checkSolutions = CheckSolutions().fileIOSolutions

print("----------------------------")

'''
Example 1: 
    Read the file "../fileIO/example1.txt" and print the contents to the terminal.
'''
def ex1():
    file = open("../fileIO/example1.txt")
    print(file.read())
    file.close()

checkSolutions['example1'](ex1)
print("----------------------------")


'''
Example 2: 
    Read the file "../fileIO/example1.txt" and print the third line to the terminal as a string, not list.
'''
def ex2():
    file = open("../fileIO/example1.txt")
    print(file.readlines(3)[0])
    file.close()

checkSolutions['example2'](ex2)
print("----------------------------")