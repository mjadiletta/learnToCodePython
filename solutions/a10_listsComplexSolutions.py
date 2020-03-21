import numpy as np
import copy

class listComplexSolutions:
    def __init__(self):
        self.listComplexSol = {}
        self.listComplexSol['example1'] = self.ex1
        self.listComplexSol['example2'] = self.ex2
        self.listComplexSol['example3'] = self.ex3
        self.listComplexSol['example4'] = self.ex4
        self.listComplexSol['example5'] = self.ex5
        self.listComplexSol['example6'] = self.ex6
        self.listComplexSol['example7'] = self.ex7

    def ex1(self, f, a):
        if f(a) == [1, 2, 3, 4, 5, 6, 7, 8, 9]:
            print("Example 1: Correct Solution")
        else:
            print("Example 1: Incorrect Solution")

    def ex2(self, f, a):
        if f(a) == [9, 8, 7, 6, 5, 4, 3, 2, 1]:
            print("Example 2: Correct Solution")
        else:
            print("Example 2: Incorrect Solution")

    def ex3(self, f, num):
        if len(f(num)) == num:
            print("Example 3: Correct Solution")
        else:
            print("Example 3: Incorrect Solution")

    def ex4(self, f, random_list, insert_number):
        sorted_list = sorted(random_list)
        for index in range(len(sorted_list)):
            if sorted_list[index] > insert_number:
                sorted_list.insert(index, insert_number)
                break
        out = f(random_list, insert_number)
        if len(out) > 0 and out == sorted_list:
            print("Example 4: Correct Solution")
        else:
            print("Example 4: Incorrect Solution")

    def ex5(self, f, random_list):
        if len(random_list) % 2 == 0:  # even number
            elements_visited = (len(random_list) + 1) * len(random_list)/2
        else:
            elements_visited = len(random_list) * (int(len(random_list)/2)+1)
        out = f(random_list)
        if out[1] > 0 and out == (sorted(copy.deepcopy(random_list)), int(elements_visited)):
            print("Example 5: Correct Solution")
        else:
            print("Example 5: Incorrect Solution")

    def ex6(self, f, random_list):
        sort_list = copy.deepcopy(random_list)  # must include this so we don't mess up the original random_list
        swap_flag = True
        new_elements_visited = 0
        sorted_elements = 0
        while (swap_flag):
            swap_flag = False
            for i in range(len(sort_list) - 1 - sorted_elements):
                if i == 0:
                    new_elements_visited += 2
                else:
                    new_elements_visited += 1
                if sort_list[i] > sort_list[i + 1]:
                    sort_list[i], sort_list[i + 1] = sort_list[i + 1], sort_list[i]
                    swap_flag = True
            sorted_elements += 1
        out = f(random_list)
        if len(out[0]) > 0 and out == (sort_list, new_elements_visited):
            print("Example 6: Correct Solution")
        else:
            print("Example 6: Incorrect Solution")

    def ex7(self, f):
        if f() == [self.ex5_sol(self.ex3_sol(10))[1], self.ex5_sol(self.ex3_sol(20))[1], self.ex5_sol(self.ex3_sol(30))[1], self.ex5_sol(self.ex3_sol(40))[1], self.ex5_sol(self.ex3_sol(50))[1]]:
            print("Example 7: Correct Solution")
        else:
            print("Example 7: Incorrect Solution")


    def ex3_sol(self, number_items):
        random_list = []
        for i in range(number_items):
            random_list.append(np.random.randint(-100, 100))
        return random_list

    def ex5_sol(self, random_list):
        sort_list = copy.deepcopy(random_list)  # must include this so we don't mess up the original random_list
        start_index = 0
        elements_visited = 0
        for number_sorted in range(len(sort_list)):
            min_index = start_index
            for index in range(start_index, len(sort_list)):
                if (sort_list[index] < sort_list[min_index]):
                    min_index = index
                elements_visited += 1

            sort_list[start_index], sort_list[min_index] = sort_list[min_index], sort_list[start_index]
            start_index += 1
        return sort_list, elements_visited
