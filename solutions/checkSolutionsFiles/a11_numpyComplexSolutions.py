import numpy as np

class numpyComplexSolutions:
    def __init__(self):
        self.numpyComplexSol = {}
        self.numpyComplexSol['example1'] = self.ex1
        self.numpyComplexSol['example2'] = self.ex2
        self.numpyComplexSol['example3'] = self.ex3
        self.numpyComplexSol['example4'] = self.ex4
        self.numpyComplexSol['example5'] = self.ex5
        self.numpyComplexSol['example6'] = self.ex6
        self.numpyComplexSol['example7'] = self.ex7
        self.numpyComplexSol['example8'] = self.ex8
        self.numpyComplexSol['example9'] = self.ex9
        self.numpyComplexSol['example10'] = self.ex10
        self.numpyComplexSol['example11'] = self.ex11

    def ex1(self, f, a):
        if f(a) == np.shape(a):
            print("Example 1: Correct Solution")
        else:
            print("Example 1: Incorrect Solution")

    def ex2(self, f, a, b):
        try:
            if np.shape(a) == np.shape(b):
                sol = a + b
            else:
                sol = -1
            if np.ndarray.tolist(f(a, b)) == np.ndarray.tolist(sol):
                print("Example 2: Correct Solution")
            else:
                print("Example 2: Incorrect Solution")
        except:
            try:
                if sol == f(a, b):
                    print("Example 2: Correct Solution")
                else:
                    print("Example 2: Incorrect Solution")
            except:
                print("Example 2: Incorrect Solution")

    def ex3(self, f, a, b, c):
        if np.shape(a) == np.shape(b) and np.shape(a) == np.shape(c):
            sol = a * b + c.T
        else:
            sol = -1
        try:
            if np.ndarray.tolist(f(a, b, c)) == np.ndarray.tolist(sol):
                print("Example 3: Correct Solution")
            else:
                print("Example 3: Incorrect Solution")
        except:
            try:
                if sol == f(a, b, c):
                    print("Example 3: Correct Solution")
                else:
                    print("Example 3: Incorrect Solution")
            except:
                print("Example 3: Incorrect Solution")

    def ex4(self, f, a, b):
        try:
            if f(a, b) == np.dot(a, b):
                print("Example 4: Correct Solution")
            else:
                print("Example 4: Incorrect Solution")
        except:
            print("Example 4: Incorrect Solution")

    def ex5(self, f, a):
        try:
            if np.ndarray.tolist(f(a)) == np.ndarray.tolist(np.zeros(np.shape(a))):
                print("Example 5: Correct Solution")
            else:
                print("Example 5: Incorrect Solution")
        except:
            print("Example 5: Incorrect Solution")

    def ex6(self, f, a):
        try:
            if np.ndarray.tolist(f(a)) == np.ndarray.tolist(np.ones(np.shape(a)[0])):
                print("Example 6: Correct Solution")
            else:
                print("Example 6: Incorrect Solution")
        except:
            print("Example 6: Incorrect Solution")

    def ex7(self, f, A, alpha):
        try:
            if np.ndarray.tolist(f(A, alpha)) == np.ndarray.tolist((A + alpha * np.eye(np.shape(A)[0]))):
                print("Example 7: Correct Solution")
            else:
                print("Example 7: Incorrect Solution")
        except:
            print("Example 7: Incorrect Solution")

    def ex8(self, f, a, i, j):
        if f(a, i, j) == a[i][j]:
            print("Example 8: Correct Solution")
        else:
            print("Example 8: Incorrect Solution")

    def ex9(self, f, a, i):
        if f(a, i) == np.sum(a[i]):
            print("Example 9: Correct Solution")
        else:
            print("Example 9: Incorrect Solution")

    def ex10(self, f, a, c, d):
        intermediate = a[np.nonzero(a >= c)]
        if f(a, c, d) == np.mean(intermediate[np.nonzero(intermediate<=d)]):
            print("Example 10: Correct Solution")
        else:
            print("Example 10: Incorrect Solution")

    def ex11(self, f, A, x):
        try:
            if np.ndarray.tolist(f(A, x)) == np.ndarray.tolist(np.linalg.solve(A, x)):
                print("Example 11: Correct Solution")
            else:
                print("Example 11: Incorrect Solution")
        except:
            print("Example 11: Incorrect Solution")

