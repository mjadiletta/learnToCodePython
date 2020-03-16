import numpy as np

class numpyComplexSolutions:
    def __init__(self):
        self.numpyComplexSol = {}
        self.numpyComplexSol['example1'] = self.ex1

    def ex1(self, f, a):
        if f(a) == (a):
            print("Example 1: Correct Solution")
        else:
            print("Example 1: Incorrect Solution")