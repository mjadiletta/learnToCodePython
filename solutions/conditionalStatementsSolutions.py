import numpy as np

class conditionalStatementsSolutions:
    def ex1(self, f, a, b):
        if f(a, b) == max([a,b]):
            print("Example 1: Correct Solution")
        else:
            print("Example 1: Incorrect Solution")

    def ex2(self, f, a, b):
        if f(a, b) == min([a,b]):
            print("Example 2: Correct Solution")
        else:
            print("Example 2: Incorrect Solution")

    def ex3(self, f, a, b):
        if a == b:
            val = 0
        else:
            val = np.min([a, b])
        if f(a, b) == val:
            print("Example 3: Correct Solution")
        else:
            print("Example 3: Incorrect Solution")

    def ex4(self, f, a, b):
        if a**2/5 > b**3/3:
            val = a
        else:
            val = b
        if f(a, b) == val:
            print("Example 4: Correct Solution")
        else:
            print("Example 4: Incorrect Solution")