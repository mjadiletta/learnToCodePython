import numpy as np
import copy

class projectSolutions:
    def __init__(self):
        self.projectSolutions = {}

        self.projectSolutions['project2p1'] = self.proj2p1
        self.projectSolutions['project2p2'] = self.proj2p2
        self.projectSolutions['project2p3a'] = self.proj2p3a
        self.projectSolutions['project2p3b'] = self.proj2p3b


    def proj2p1(self, f, x, B, alpha):
        if f(x, B, alpha) == (1 / (1 + np.exp(-B*(x-alpha)))):
            print("Project 2 P1: Correct Solution")
        else:
            print("Project 2 P1: Incorrect Solution")

    def proj2p2(self, f, sigmoid, start, end, step_size, B, alpha):
        list_x = []
        list_y = []
        for i in np.arange(start, end, step_size):
            list_x.append(i)
            list_y.append(sigmoid(i, B, alpha))
        if f(sigmoid, start, end, step_size, B, alpha) == (list_x, list_y):
            print("Project 2 P2: Correct Solution")
        else:
            print("Project 2 P2: Incorrect Solution")

    def proj2p3a(self, f, bpf, start, end, step_size):
        list_x = []
        list_y = []
        for i in np.arange(start, end, step_size):
            list_x.append(i)
            list_y.append(bpf(i))
        if f(bpf, start, end, step_size) == (list_x, list_y):
            print("Project 2 P3a: Correct Solution")
        else:
            print("Project 2 P3a: Incorrect Solution")

    def sigmoid(self, x, B, alpha):
        return 1 / (1 + np.exp(-B * (x - alpha)))

    def bandpass_filter(self, B, alpha1, alpha2):
        return lambda x: self.sigmoid(x, B, alpha1) - self.sigmoid(x, B, alpha2)

    def proj2p3b(self, f, b_vals, alpha1, alpha2, start, end, step_size):
        all_XY = []
        for i, b in enumerate(b_vals):
            bpf = self.bandpass_filter(b, alpha1, alpha2)
            list_x = []
            list_y = []
            for i in np.arange(start, end, step_size):
                list_x.append(i)
                list_y.append(bpf(i))
            all_XY.append((list_x, list_y))

        if f(b_vals, alpha1, alpha2, start, end, step_size) == all_XY:
            print("Project 2 P3b: Correct Solution")
        else:
            print("Project 2 P3b: Incorrect Solution")
