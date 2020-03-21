import numpy as np
import copy

class project5Solutions:
    def __init__(self):
        self.projectSolutions = {}
        self.projectSolutions['project5'] = self.proj5


    def proj5(self, f):
        if f():
            print("Project 5: Correct Solution")
        else:
            print("Project 5: Incorrect Solution")