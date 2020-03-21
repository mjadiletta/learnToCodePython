import sys
import os
import numpy as np
from io import StringIO


class fileIOSolutions:
    def __init__(self):
        self.fileIOSolutions = {}
        self.fileIOSolutions['example1'] = self.ex1
        self.fileIOSolutions['example2'] = self.ex2

    def ex1(self, f):
        f()
        temp_out = sys.stdout
        sys.stdout = open("./temp.txt", "w")
        f()
        sys.stdout.close()
        sys.stdout = temp_out
        file1 = open("../fileIO/example1.txt")
        file2 = open("./temp.txt", "r")
        d1 = file1.read()
        d2 = file2.read()
        file1.close()
        file2.close()
        correct = True
        for i in range(len(d1)):
            if d1[i] != d2[i]:
                correct = False
        os.remove("./temp.txt")
        if correct:
            print("\nExample 1: Correct Solution")
        else:
            print("\nExample 1: Incorrect Solution")

    def ex2(self, f):
        f()
        temp_out = sys.stdout
        sys.stdout = open("./temp.txt", "w")
        f()
        sys.stdout.close()
        sys.stdout = temp_out
        file1 = open("../fileIO/example1.txt")
        file2 = open("./temp.txt", "r")
        d1 = file1.readlines(3)
        d2 = file2.readlines(3)
        file1.close()
        file2.close()
        correct = True
        for i in range(len(d1)):
            if d1[i] != d2[i]:
                correct = False

        os.remove("./temp.txt")
        if correct:
            print("\nExample 1: Correct Solution")
        else:
            print("\nExample 1: Incorrect Solution")