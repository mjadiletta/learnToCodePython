import numpy as np

class loopSimpleSolutions:
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