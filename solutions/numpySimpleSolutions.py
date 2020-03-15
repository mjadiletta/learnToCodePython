import numpy as np
import copy as cp

class numpySimpleSol:
    def ex1(self, f, list):
        if f(list) == "You can learn numpy!":
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
        if f(list, new_num) == sum(list) + new_num:
            print("Example 5: Correct Solution")
        else:
            print("Example 5: Incorrect Solution")

    def ex6(self, f, list, new_num):
        if f(list, new_num) == sum(list) + new_num:
            print("Example 6: Correct Solution")
        else:
            print("Example 6: Incorrect Solution")

    def ex7(self, f, list):
        new_list = cp.deepcopy(list)
        if f(new_list) == sum(list[1:]):
            print("Example 7: Correct Solution")
        else:
            print("Example 7: Incorrect Solution.")

    def ex8(self, f, list):
        new_list = cp.deepcopy(list)
        if f(new_list) == sum(list[0:2] + list[3:]):
            print("Example 8: Correct Solution")
        else:
            print("Example 8: Incorrect Solution")

    def ex9(self, f, list_c, list_d):
        try:
            if(f(list_c, list_d) == None):
                None
            print("Example 9: Incorrect Solution")
        except:
            if np.ndarray.tolist(f(list_c, list_d)) == [5, 2, 3, 4, 1]:
                print("Example 9: Correct Solution")
            else:
                print("Example 9: Incorrect Solution")

    def ex10(self, f, list_b, list_c, list_d):
        if f(list_b, list_c, list_d) == sum(list_b+list_c+list_d):
            print("Example 10: Correct Solution")
        else:
            print("Example 10: Incorrect Solution")

    def ex11(self, f, path):
        try:
            if(f(path) == None):
                None
            print("Example 11: Incorrect Solution")
        except:
            if np.ndarray.tolist(f(path)) == np.ndarray.tolist(np.load("data/numpy60MeterDashEx.npy")):
                print("Example 11: Correct Solution")
            else:
                print("Example 11: Incorrect Solution")


    def ex12(self, f, path):
        data = np.load("data/numpy60MeterDashEx.npy")
        if f(path) == (np.average(data), np.bincount((data*100).astype(int)).argmax()/100, np.min(data), np.max(data)):
            print("Example 12: Correct Solution")
        else:
            print("Example 12: Incorrect Solution")

    def ex13(self, f, path):
        data = np.load("data/numpy60MeterDashEx.npy")[0:12]
        if f(path) == (np.average(data), np.bincount((data * 100).astype(int)).argmax() / 100, np.min(data), np.max(data)):
            print("Example 13: Correct Solution")
        else:
            print("Example 13: Incorrect Solution")

    def ex14(self, f, path):
        first_12 = np.load("data/numpy60MeterDashEx.npy")[0:12]
        second_12 = np.load("data/numpy60MeterDashEx.npy")[12:]
        cost_1 = np.average(first_12) * 12 + np.min(first_12) * 6 + np.max(first_12) * 3
        cost_2 = np.average(second_12) * 12 + np.min(second_12) * 6 + np.max(second_12) * 3
        if (cost_1 < cost_2):
            ret = (np.ndarray.tolist(first_12), cost_1)
        else:
            ret = (np.ndarray.tolist(second_12), cost_2)
        try:
            if (f(path)[0] == None):
                None
            print("Example 14: Incorrect Solution")
        except:
            if (np.ndarray.tolist(f(path)[0]), f(path)[1]) == ret:
                print("Example 14: Correct Solution")
            else:
                print("Example 14: Incorrect Solution")


    def ex15(self, f, path):
        if f(path) == np.shape(np.load("data/numpy60MeterDashEx.npy")):
            print("Example 15: Correct Solution")
        else:
            print("Example 15: Incorrect Solution")

    def ex16(self, f, path):
        try:
            if (f(path) == None):
                None
            print("Example 16: Incorrect Solution")
        except:
            if np.ndarray.tolist(f(path)) == np.ndarray.tolist(np.reshape(np.load("data/numpy60MeterDashEx.npy"), [2, 12])):
                print("Example 16: Correct Solution")
            else:
                print("Example 16: Incorrect Solution")

    def ex17(self, f, path):
        if f(path) == np.dot(np.load("data/numpy60MeterDashEx.npy")[0:12], np.load("data/numpy60MeterDashEx.npy")[12:]):
            print("Example 17: Correct Solution")
        else:
            print("Example 17: Incorrect Solution")

    def ex18(self, f, path):
        try:
            if (f(path) == None):
                None
            print("Example 18: Incorrect Solution")
        except:
            if np.ndarray.tolist(f(path)) == np.ndarray.tolist(np.outer(np.load("data/numpy60MeterDashEx.npy")[0:12], np.load("data/numpy60MeterDashEx.npy")[12:])):
                print("Example 18: Correct Solution")
            else:
                print("Example 18: Incorrect Solution")

    def ex19(self, f, path):
        try:
            if (f(path) == None):
                None
            print("Example 19: Incorrect Solution")
        except:
            if np.ndarray.tolist(f(path)) == np.ndarray.tolist(
                    np.multiply(np.load("data/numpy60MeterDashEx.npy")[0:12],
                                np.load("data/numpy60MeterDashEx.npy")[12:])):
                print("Example 19: Correct Solution")
            else:
                print("Example 19: Incorrect Solution")

    def ex20(self, f, path):
        try:
            if (f(path) == None):
                None
            print("Example 20: Incorrect Solution")
        except:
            if np.ndarray.tolist(f(path)) == np.ndarray.tolist(
                    np.dot(np.outer(np.load("data/numpy60MeterDashEx.npy")[0:12],
                                    np.load("data/numpy60MeterDashEx.npy")[12:]),
                           np.multiply(np.load("data/numpy60MeterDashEx.npy")[0:12],
                                       np.load("data/numpy60MeterDashEx.npy")[12:])) *
                    np.dot(np.load("data/numpy60MeterDashEx.npy")[0:12], np.load("data/numpy60MeterDashEx.npy")[12:])):
                print("Example 20: Correct Solution")
            else:
                print("Example 20: Incorrect Solution")
