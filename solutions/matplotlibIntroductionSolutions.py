import numpy as np
import copy as cp
import matplotlib.pyplot as plt

class matplotlibIntroductionSol:
    def ex1(self, f, path):
        out = f(path)
        try:
            if out[0] == None or out[1] == None:
                None
            print("Example 1: Incorrect Solution")
        except:
            if (np.ndarray.tolist(out[0]), np.ndarray.tolist(out[1])) == (np.ndarray.tolist(np.arange(np.shape(np.load(path))[0])), np.ndarray.tolist(np.load(path))):
                print("Example 1: Correct Solution")
            else:
                print("Example 1: Incorrect Solution")

    def ex2(self, f, path):
        out = f(path)
        try:
            if out == None or out[0] == None or out[1] == None or out[2] == None:
                None
            print("Example 2: Incorrect Solution")
        except:
            if (np.ndarray.tolist(out[0]), np.ndarray.tolist(out[1]), np.ndarray.tolist(out[2])) == (np.ndarray.tolist(np.arange(np.shape(np.load(path))[0])), np.ndarray.tolist(np.load(path)), np.ndarray.tolist(plt.hist(np.load(path), bins=10)[0])):
                print("Example 2: Correct Solution")
            else:
                print("Example 2: Incorrect Solution")
        plt.close()

    def ex3(self, f, path):
        out = f(path)
        try:
            if out == None or out[0] == None or out[1] == None or out[2] == None or \
                    out[3] == None or out[4] == None or out[5] == None:
                None
            print("Example 3: Incorrect Solution")
        except:
            if (np.ndarray.tolist(out[0]),
                np.ndarray.tolist(out[1]),
                np.ndarray.tolist(out[2]),
                np.ndarray.tolist(out[3]),
                np.ndarray.tolist(out[4]),
                np.ndarray.tolist(out[5])) == \
                (np.ndarray.tolist(np.arange(np.shape(np.load(path)[0:12])[0])),
                 np.ndarray.tolist(np.load(path)[0:12]),
                 np.ndarray.tolist(plt.hist(np.load(path)[0:12], bins=6)[0]),
                 np.ndarray.tolist(np.arange(np.shape(np.load(path)[12:])[0])),
                 np.ndarray.tolist(np.load(path)[12:]),
                 np.ndarray.tolist(plt.hist(np.load(path)[12:], bins=6)[0])):
                print("Example 3: Correct Solution")
            else:
                print("Example 3: Incorrect Solution")
        plt.close()

    def ex4(self, f, path):
        out = f(path)
        try:
            if out == None or out[0] == None or out[1] == None or out[2] == None or \
                    out[3] == None or out[4] == None or out[5] == None:
                None
            print("Example 4: Incorrect Solution")
        except:
            if (np.ndarray.tolist(out[0]),
                np.ndarray.tolist(out[1]),
                np.ndarray.tolist(out[2]),
                np.ndarray.tolist(out[3]),
                np.ndarray.tolist(out[4]),
                np.ndarray.tolist(out[5])) == \
                    (np.ndarray.tolist(np.arange(np.shape(np.load(path)[0:12])[0])),
                     np.ndarray.tolist(np.load(path)[0:12]),
                     np.ndarray.tolist(plt.hist(np.load(path)[0:12], bins=5)[0]),
                     np.ndarray.tolist(np.arange(np.shape(np.load(path)[12:])[0])),
                     np.ndarray.tolist(np.load(path)[12:]),
                     np.ndarray.tolist(plt.hist(np.load(path)[12:], bins=5)[0])):
                print("Example 4: Correct Solution")
            else:
                print("Example 4: Incorrect Solution")
        plt.close()