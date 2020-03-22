from solutions.graphics import *
import numpy as np

class graphicsIntroSolutions:
    def __init__(self):
        self.graphicsIntroSolutions = {}
        self.graphicsIntroSolutions['example1'] = self.ex1
        self.graphicsIntroSolutions['example2'] = self.ex2
        self.graphicsIntroSolutions['example3'] = self.ex3
        self.graphicsIntroSolutions['example4dy'] = self.ex4dy
        self.graphicsIntroSolutions['example4normdy'] = self.ex4normdy
        self.graphicsIntroSolutions['example4'] = self.ex4

    def ex1(self, f):
        correct = True
        items = f()
        for index, i in enumerate(items):
            shape = str(i).split("(")[0]
            if index == 0 and (shape != "Rectangle" or i.getP1().getX() < 150 or i.getP1().getY() < 150
                    or i.getP2().getX() > 350 or i.getP2().getY() > 350 or i.config["fill"] != "maroon"):
                correct = False
            if index == 1 and (shape != "Circle" or i.getCenter().getX() != 250 or i.getCenter().getY() != 250
                    or i.config["fill"] != "lightblue"):
                correct = False
            if index == 2 and (shape != "Line" or (i.getP1().getY() - i.getP2().getY())/(i.getP1().getX() - i.getP2().getX()) != 1
                    or i.config["width"] != 3 or i.config["fill"] != "medium sea green"):
                correct = False
        if correct:
            print("Example 1: Correct Solution")
        else:
            print("Example 1: Incorrect Solution")


    def ex2(self, f):
        correct_net = True
        items, win = f()
        if len(items) != 15:
            correct_net = False

        for index, i in enumerate(items):
            shape = str(i).split("(")[0]
            correct = True
            if index == 0 and (shape != "Oval" or i.getP1().getX() != 100 or i.getP1().getY() != 100
                or i.getP2().getX() != 468 or i.getP2().getY() != 464 or i.config["fill"] != "IndianRed4"):
                correct = False
            if index == 1 and (shape != "Oval" or i.getP1().getX() != 436 or i.getP1().getY() != 100
                or i.getP2().getX() != 804 or i.getP2().getY() != 464 or i.config["fill"] != "IndianRed4"):
                correct = False
            if index == 2 and (shape != "Rectangle" or i.getP1().getX() != 284 or i.getP1().getY() != 100
                or i.getP2().getX() != 620 or i.getP2().getY() != 464 or i.config["fill"] != "IndianRed4"
                or i.config["outline"] != "IndianRed4"):
                correct = False
            if index == 3 and (shape != "Line" or i.getP1().getX() != 284 or i.getP1().getY() != 100
                or i.getP2().getX() != 620 or i.getP2().getY() != 100):
                correct = False
            if index == 4 and (shape != "Line" or i.getP1().getX() != 284 or i.getP1().getY() != 464
                or i.getP2().getX() != 620 or i.getP2().getY() != 464):
                correct = False
            if index == 5 and (shape != "Oval" or i.getP1().getX() != 138 or i.getP1().getY() != 138
                or i.getP2().getX() != 430 or i.getP2().getY() != 426 or i.config["fill"] != "sea green"
                or i.config["outline"] != "white"):
                correct = False
            if index == 6 and (shape != "Oval" or i.getP1().getX() != 474 or i.getP1().getY() != 138
                or i.getP2().getX() != 766 or i.getP2().getY() != 426 or i.config["fill"] != "sea green"
                or i.config["outline"] != "white"):
                correct = False
            if index == 7 and (shape != "Rectangle" or i.getP1().getX() != 284 or i.getP1().getY() != 138
                or i.getP2().getX() != 620 or i.getP2().getY() != 426 or i.config["fill"] != "sea green"
                or i.config["outline"] != "sea green"):
                correct = False
            if index == 8 and (shape != "Line" or i.getP1().getX() != 284 or i.getP1().getY() != 138
                or i.getP2().getX() != 620 or i.getP2().getY() != 138 or i.config["fill"] != "white"):
                correct = False
            if index == 9 and (shape != "Line" or i.getP1().getX() != 284 or i.getP1().getY() != 426
                or i.getP2().getX() != 620 or i.getP2().getY() != 426 or i.config["fill"] != "white"):
                correct = False
            if index == 10 and (shape != "Line" or i.getP1().getX() != 284 or i.getP1().getY() != 100
                or i.getP2().getX() != 284 or i.getP2().getY() != 138 or i.config["width"] != 3):
                correct = False
            if index == 11 and (shape != "Text" or i.getAnchor().getX() != 284 or i.getAnchor().getY() != 80
                or i.getText() != "Finish Line"):
                correct = False
            if index == 12 and (shape != "Rectangle" or i.getP1().getX() != 620 or i.getP1().getY() != 100
                or i.getP2().getX() != 805 or i.getP2().getY() != 138 or i.config["fill"] != "IndianRed4"):
                correct = False
            if index == 13 and (shape != "Line" or i.getP1().getX() != 620 or i.getP1().getY() != 100
                or i.getP2().getX() != 620 or i.getP2().getY() != 138 or i.config["fill"] != "IndianRed4"):
                correct = False
            if index == 14 and (shape != "Line" or i.getP1().getX() != 620 or i.getP1().getY() != 138
                or i.getP2().getX() != 732 or i.getP2().getY() != 138 or i.config["fill"] != "white"):
                correct = False

            if correct == False:
                correct_net = False
                print("\tObject " + str(index + 1) + ": Incorrect")
            else:
                print("\tObject " + str(index + 1) + ": Correct")

        if correct_net:
            print("Example 2: Correct Solution")
        else:
            print("Example 2: Incorrect Solution")

    def ex3(self, f):
        correct_net = True
        items = f()
        if not (len(items) == 16 or len(items) == 17):
            correct_net = False

        shape = str(items[-1]).split("(")[0]

        if shape != "Circle" or (not items[-1].getCenter().getX() < 284):
            correct_net = False

        if correct_net:
            print("Example 3: Correct Solution")
        else:
            print("Example 3: Incorrect Solution")

    def ex4dy(self, f):
        correct_net = True
        a = 165
        b = 163
        x_vals = [0, 90, 165, 163]
        for x in x_vals:
            if x < 165:
                sol = -1 * (b ** 2 - b ** 2 / a ** 2 * x ** 2) ** (-1 / 2) * b ** 2 / a ** 2 * x
            if x == 165:
                sol = np.inf
            if sol != f(x, a, b):
                correct_net = False

        if correct_net:
            print("Example 4 Derivative y: Correct Solution")
        else:
            print("Example 4 Derivative y: Incorrect Solution")

    def ex4normdy(self, f1, f2):
        correct = True
        x_vals = [1, 90, 165, 163]
        y_vals = [-163, -150, 0, 20, 163]
        for y in y_vals:
            for x in x_vals:
                unnormalized_dy = f2(x, 165, 163)
                if unnormalized_dy == None or unnormalized_dy == np.inf:
                    if y < 0:
                        sol = -.001, -.999  # handle the inf case to get back on track
                    else:
                        sol = .001, -.999
                else:
                    sol = -1 * np.sign(y) * 1 / np.sqrt(unnormalized_dy ** 2 + 1), unnormalized_dy / np.sqrt(unnormalized_dy ** 2 + 1)
                out = f1(unnormalized_dy, y)
                if not (sol[0]-.01 < out[0] and sol[0]+.01 > out[0]) or not (sol[1]-.01 < out[1] and sol[1]+.01 > out[1]):
                    correct = False
        if correct:
            print("Example 4 Normalized dx dy: Correct Solution")
        else:
            print("Example 4 Normalized dx dy: Incorrect Solution")

    def ex4(self, f):
        correct_net = True
        items = f()
        if not (len(items) == 16 or len(items) == 17):
            correct_net = False

        shape = str(items[-1]).split("(")[0]

        if shape != "Circle" or (not items[-1].getCenter().getX() < 284):
            correct_net = False

        if correct_net:
            print("Example 4: Correct Solution")
        else:
            print("Example 4: Incorrect Solution")
