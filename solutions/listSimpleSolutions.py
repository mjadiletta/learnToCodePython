import numpy as np
import copy as cp

class listSimpleSol:
    def __init__(self):
        self.listSimpleSolutions = {}
        self.listSimpleSolutions['example1'] = self.ex1
        self.listSimpleSolutions['example2'] = self.ex2
        self.listSimpleSolutions['example3'] = self.ex3
        self.listSimpleSolutions['example4'] = self.ex4
        self.listSimpleSolutions['example5'] = self.ex5
        self.listSimpleSolutions['example6'] = self.ex6
        self.listSimpleSolutions['example7'] = self.ex7
        self.listSimpleSolutions['example8'] = self.ex8
        self.listSimpleSolutions['example9'] = self.ex9
        self.listSimpleSolutions['example10'] = self.ex10

    def ex1(self, f, list):
        if f(list) == "You can learn python!":
            print("Example 1: Correct Solution")
        else:
            print("Example 1: Incorrect Solution")

    def ex2(self, f, list):
        if f(list) == 15:
            print("Example 2: Correct Solution")
        else:
            print("Example 2: Incorrect Solution")

    def ex3(self, f, list):
        if f(list) == 3:
            print("Example 3: Correct Solution")
        else:
            print("Example 3: Incorrect Solution")

    def ex4(self, f, list):
        if f(list) == 4:
            print("Example 4: Correct Solution")
        else:
            print("Example 4: Incorrect Solution")

    def ex5(self, f, list, new_num):
        if f(list, new_num) == sum(list) and list[-1] == new_num:
            print("Example 5: Correct Solution")
        else:
            print("Example 5: Incorrect Solution \n\t\t- make sure you are appending to the end of the list")

    def ex6(self, f, list, new_num):
        if f(list, new_num) == sum(list) and list[0] == new_num:
            print("Example 6: Correct Solution")
        else:
            print("Example 6: Incorrect Solution \n\t\t- make sure you are appending to the beginning of the list")

    def ex7(self, f, list):
        new_list = cp.deepcopy(list)
        if f(new_list) == sum(list[1:]) and list[1:] == new_list:
            print("Example 7: Correct Solution")
        else:
            print("Example 7: Incorrect Solution - make sure you are removing the first element.")

    def ex8(self, f, list):
        new_list = cp.deepcopy(list)
        if f(new_list) == sum(list[0:2] + list[3:]) and list[0:2] + list[3:] == new_list:
            print("Example 8: Correct Solution")
        else:
            print("Example 8: Incorrect Solution")

    def ex9(self, f, list_c, list_d):
        if f(list_c, list_d) == [5, 2, 3, 4, 1]:
            print("Example 9: Correct Solution")
        else:
            print("Example 9: Incorrect Solution")

    def ex10(self, f, list_b, list_c, list_d):
        if f(list_b, list_c, list_d) == sum(list_b+list_c+list_d):
            print("Example 10: Correct Solution")
        else:
            print("Example 10: Incorrect Solution")
