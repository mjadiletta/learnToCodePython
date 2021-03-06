import numpy as np

class codeFunctionsSolutions:
    def __init__(self):
        self.functionSolutions = {}
        self.functionSolutions['example1'] = self.ex1
        self.functionSolutions['example2'] = self.ex2
        self.functionSolutions['example3'] = self.ex3
        self.functionSolutions['example4'] = self.ex4
        self.functionSolutions['example5'] = self.ex5
        self.functionSolutions['example6'] = self.ex6
        self.functionSolutions['example7'] = self.ex7
        self.functionSolutions['example8'] = self.ex8
        self.functionSolutions['example9'] = self.ex9
        self.functionSolutions['example10'] = self.ex10
        self.functionSolutions['example11'] = self.ex11
        self.functionSolutions['example12'] = self.ex12
        self.functionSolutions['example13'] = self.ex13
        self.functionSolutions['example14'] = self.ex14

    def ex1(self, f, a, b):
        if f(a, b) == (a+b):
            print("Example 1: Correct Solution")
        else:
            print("Example 1: Incorrect Solution")

    def ex2(self, f, a, b):
        if f(a, b) == (a*b):
            print("Example 2: Correct Solution")
        else:
            print("Example 2: Incorrect Solution")

    def ex3(self, f, a, b):
        if f(a, b) == (a/b):
            print("Example 3: Correct Solution")
        else:
            print("Example 3: Incorrect Solution")

    def ex4(self, f, a, b):
        if f(a, b) == (a**b):
            print("Example 4: Correct Solution")
        else:
            print("Example 4: Incorrect Solution")

    def ex5(self, f, a):
        if f(a) == np.sqrt(a):
            print("Example 5: Correct Solution")
        else:
            print("Example 5: Incorrect Solution")

    def ex6(self, f, a, b):
        if f(a, b) == (a % b):
            print("Example 6: Correct Solution")
        else:
            print("Example 6: Incorrect Solution")

    def ex7(self, f, a):
        if f(a) == abs(a):
            print("Example 7: Correct Solution")
        else:
            print("Example 7: Incorrect Solution")

    def ex8(self, f, a):
        if f(a) == np.exp(a):
            print("Example 8: Correct Solution")
        else:
            print("Example 8: Incorrect Solution")

    def ex9(self, f, m, x, b):
        if f(m, x, b) == (m * x + b):
            print("Example 9: Correct Solution")
        else:
            print("Example 9: Incorrect Solution")

    def ex10(self, f, a, b):
        if f(a, b) == np.sqrt(a**2 + b**2):
            print("Example 10: Correct Solution")
        else:
            print("Example 10: Incorrect Solution")

    def ex11(self, f, m, h):
        if f(m, h) == (m*9.8*h):
            print("Example 11: Correct Solution")
        else:
            print("Example 11: Incorrect Solution")

    def ex12(self, f, m, v):
        if f(m, v) == (1/2*m*v**2):
            print("Example 12: Correct Solution")
        else:
            print("Example 12: Incorrect Solution")

    def ex13(self, f, x):
        if f(x) == (np.exp(x) / (1 + np.exp(x))):
            print("Example 13: Correct Solution")
        else:
            print("Example 13: Incorrect Solution")

    def ex14(self, f, x):
        if f(x) == (np.exp(x) - np.exp(-x))/(np.exp(x) + np.exp(-x)):
            print("Example 14: Correct Solution")
        else:
            print("Example 14: Incorrect Solution")



