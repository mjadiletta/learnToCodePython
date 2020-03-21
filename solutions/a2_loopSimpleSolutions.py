import numpy as np

class loopSimpleSolutions:
    def __init__(self):
        self.loopSolutions = {}
        self.loopSolutions['example1'] = self.ex1
        self.loopSolutions['example2'] = self.ex2
        self.loopSolutions['example3'] = self.ex3
        self.loopSolutions['example4'] = self.ex4
        self.loopSolutions['example5'] = self.ex5
        self.loopSolutions['example6'] = self.ex6
        self.loopSolutions['example7'] = self.ex7
        self.loopSolutions['example8'] = self.ex8
        self.loopSolutions['example9'] = self.ex9
        self.loopSolutions['example10'] = self.ex10
        self.loopSolutions['example11'] = self.ex11

    def ex1(self, f):
        if f() == "0 1 2 3 4 5 ":
            print("Example 1: Correct Solution")
        else:
            print("Example 1: Incorrect Solution")

    def ex2(self, f):
        if f() == "012345":
            print("Example 2: Correct Solution")
        else:
            print("Example 2: Incorrect Solution")

    def ex3(self, f):
        if f() == "6789":
            print("Example 3: Correct Solution")
        else:
            print("Example 3: Incorrect Solution")

    def ex4(self, f):
        if f() == 15:
            print("Example 4: Correct Solution")
        else:
            print("Example 4: Incorrect Solution")

    def ex5(self, f, a, b):
        sum = 0
        for i in range(a, b):
            sum += i
        if f(a, b) == sum:
            print("Example 5: Correct Solution")
        else:
            print("Example 5: Incorrect Solution")

    def ex6(self, f):
        if f() == "0 1 2 3 4 5 ":
            print("Example 6: Correct Solution")
        else:
            print("Example 6: Incorrect Solution")

    def ex7(self, f):
        if f() == "012345":
            print("Example 7: Correct Solution")
        else:
            print("Example 7: Incorrect Solution")

    def ex8(self, f):
        if f() == "6789":
            print("Example 8: Correct Solution")
        else:
            print("Example 8: Incorrect Solution")

    def ex9(self, f):
        if f() == 15:
            print("Example 9: Correct Solution")
        else:
            print("Example 9: Incorrect Solution")

    def ex10(self, f, a, b):
        sum = 0
        i = a
        while i < b:
            sum += i
            i += 1
        if f(a, b) == sum:
            print("Example 10: Correct Solution")
        else:
            print("Example 10: Incorrect Solution")

    def ex11(self, f, a, b):
        if f(a, b) == a*b:
            print("Example 11: Correct Solution")
        else:
            print("Example 11: Incorrect Solution")