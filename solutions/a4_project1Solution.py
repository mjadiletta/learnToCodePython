import numpy as np
import copy

class project1Solutions:
    def __init__(self):
        self.projectSolutions = {}
        self.projectSolutions['project1'] = self.proj1

    def proj1(self, f1, f2, input_val, terminal_val):
        num_loops = 0
        iv = copy.deepcopy(input_val)
        while iv < terminal_val:
            iv += num_loops**2
            num_loops += 1

        if f1(f2, input_val, terminal_val) == num_loops:
            print("Project 1: Correct Solution")
        else:
            print("Project 1: Incorrect Solution")
