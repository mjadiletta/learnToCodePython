import sys
import os
import numpy as np
from io import StringIO


class fileIOSolutions:
    def __init__(self):
        self.fileIOSolutions = {}
        self.fileIOSolutions['example1'] = self.ex1
        self.fileIOSolutions['example2'] = self.ex2
        self.fileIOSolutions['example3'] = self.ex3
        self.fileIOSolutions['example4'] = self.ex4
        self.fileIOSolutions['example5'] = self.ex5
        self.fileIOSolutions['example6'] = self.ex6
        self.fileIOSolutions['example7'] = self.ex7
        self.fileIOSolutions['example8a'] = self.ex8a
        self.fileIOSolutions['example8b'] = self.ex8b

    def ex1(self, f):
        f()
        temp_out = sys.stdout
        sys.stdout = open("./temp.txt", "w")
        f()
        sys.stdout.close()
        sys.stdout = temp_out
        file1 = open("../fileIO/text1.txt")
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
        file1 = open("../fileIO/text1.txt")
        file2 = open("./temp.txt", "r")
        d1 = file1.readlines()[2]

        correct = True
        try:
            d2 = file2.readlines()
            d2 = d2[0]
            for i in range(len(d1)):
                if d1[i] != d2[i]:
                    correct = False
        except:
            correct = False

        file1.close()
        file2.close()

        os.remove("./temp.txt")
        if correct:
            print("Example 2: Correct Solution")
        else:
            print("Example 2: Incorrect Solution")

    def ex3(self, f):
        f()
        temp_out = sys.stdout
        sys.stdout = open("./temp.txt", "w")
        f()
        sys.stdout.close()
        sys.stdout = temp_out
        file1 = open("../fileIO/text1.txt")
        file2 = open("./temp.txt", "r")
        d1 = file1.readlines()[1].split(" ")

        correct = True
        try:
            d2 = file2.readlines()
            d2 = d2[0]
            d2 = d2.replace("'", "").replace("]", "").replace("[", "").replace(",", "").replace("\\n", "").split(" ")
            for i in range(len(d1)):
                if d1[i] != d2[i]:
                    correct = False
        except:
            correct = False

        file1.close()
        file2.close()


        os.remove("./temp.txt")
        if correct:
            print("\nExample 3: Correct Solution")
        else:
            print("Example 3: Incorrect Solution")

    def ex4(self, f):
        f()
        temp_out = sys.stdout
        sys.stdout = open("./temp.txt", "w")
        f()
        sys.stdout.close()
        sys.stdout = temp_out
        file1 = open("../fileIO/text1.txt")
        file2 = open("./temp.txt", "r")
        d1 = file1.readlines()[3].replace("t", "!").split(" ")
        correct = True
        try:
            d2 = file2.readlines()[0].replace("'", "").replace("]", "").replace("[", "").replace(",", "").replace("\n", "").split(" ")
            for i in range(len(d1)):
                if d1[i] != d2[i]:
                    correct = False
        except:
            correct = False

        file1.close()
        file2.close()


        os.remove("./temp.txt")
        if correct:
            print("\nExample 4: Correct Solution")
        else:
            print("Example 4: Incorrect Solution")

    def ex5(self, f):
        f()
        temp_out = sys.stdout
        sys.stdout = open("./temp.txt", "w")
        f()
        sys.stdout.close()
        sys.stdout = temp_out
        file1 = open("../fileIO/text1.txt")
        file2 = open("./temp.txt", "r")
        d1 = file1.readlines()[0].replace("R", "r").split(" ")
        d1[2] = "useless"
        d1.insert(0, "You")
        d1 = ' '.join(d1)

        correct = True
        try:
            d2 = file2.readlines()[0]
            for i in range(len(d1)):
                if d1[i] != d2[i]:
                    correct = False
        except:
            correct = False
        file1.close()
        file2.close()


        os.remove("./temp.txt")
        if correct:
            print("Example 5: Correct Solution")
        else:
            print("Example 5: Incorrect Solution")

    def ex6(self, f):
        f()
        file1 = open("../fileIO/text1.txt", 'r')
        file2 = open("../fileIO/out1.txt", "r")
        d1 = file1.readlines()
        d2 = file2.readlines()
        file1.close()
        file2.close()
        correct = True
        try:
            for i in range(len(d1)):
                if d1[i] != d2[i]:
                    correct = False
        except:
            correct = False

        if correct:
            print("Example 6: Correct Solution")
        else:
            print("Example 6: Incorrect Solution")

    def ex7(self, f):
        tempMe = sys.stdout
        f()
        file = open("./temp.txt", "w")
        sys.stdout = file
        f()
        file.close()
        sys.stdout = tempMe

        f = open("./temp.txt", 'r')
        d = f.readlines()
        f.close()

        correct = True
        try:
            if d[0] != "Printing to the Terminal!\n" or d[1] != "Printing Back to the Terminal!\n":
                correct = False
        except:
            correct = False

        f = open("../fileIO/out1.txt", 'r')
        d = f.readlines()
        f.close()
        try:
            if d[0] != "Printing to the Out1.txt File!\n":
                correct = False
        except:
            correct = False

        if correct:
            print("Example 7: Correct Solution")
        else:
            print("Example 7: Incorrect Solution")

    def ex8a(self, f):
        gb = f()
        game_board = []
        inputFile = open("../fileIO/ticTacToeBoard1.txt", 'r')
        data = inputFile.readlines()
        for d in data:
            game_board.append(d.replace("| ", "").replace("\n", "").replace(" ", "", 1).split(" "))
        if gb == game_board:
            print("Example 8a: Correct Solution")
        else:
            print("Example 8a: Incorrect Solution")

    def ex8b(self, f, gb):
        temp_out = sys.stdout

        f()

        sys.stdout = open("./temp.txt", "w")

        from solutions.ticTacToeSolution import ticTacToe
        tTT = ticTacToe()

        correct = True
        try:
            tTT.playGame(gb)
        except:
            correct = False

        sys.stdout.close()
        sys.stdout = temp_out

        f1 = open("../fileIO/ticTacToeOut.txt", 'r')
        f2 = open("./temp.txt")

        d2 = f1.readlines()
        d1 = f2.readlines()
        try:
            for row_num in range(len(d1)):
                if d1[row_num] != d2[row_num]:
                    correct = False
        except:
            correct = False

        f1.close()
        f2.close()

        temp_out = sys.stdout
        sys.stdout = open("./temp.txt", "w")
        f()
        sys.stdout.close()
        sys.stdout = temp_out
        f = open("./temp.txt")
        d = f.readlines()
        f.close()
        try:
            if d[-1] != "Fixed the output!\n":
                correct = False
        except:
            correct = False

        if correct:
            print("Example 8b: Correct Solution")
        else:
            print("Example 8b: Incorrect Solution")

        os.remove("./temp.txt")
