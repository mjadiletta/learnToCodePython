import numpy as np
from solutions.graphics import *

class graphicsComplexSolutions:
    def __init__(self):
        self.graphicsComplexSolutions = {}
        self.graphicsComplexSolutions['example1'] = self.ex1
        self.graphicsComplexSolutions['example2'] = self.ex2
        self.graphicsComplexSolutions['example3'] = self.ex3
        self.graphicsComplexSolutions['example4'] = self.ex4
        self.graphicsComplexSolutions['example5'] = self.ex5
        self.graphicsComplexSolutions['example6'] = self.ex6

    def ex1(self, f, x, y, c):
        items, win = f(x, y, c)
        try:
            correct_net = True
            for index, i in enumerate(items):
                shape = str(i).split("(")[0]
                correct = True
                if index == 0 and (shape != "Rectangle" or i.getP1().getX() != x or i.getP1().getY() != y
                                   or i.getP2().getX() != x+45 or i.getP2().getY() != y+45 or i.config[
                                       "fill"] != c):
                    correct = False
                if index == 1 and (shape != "Rectangle" or i.getP1().getX() != x+7 or i.getP1().getY() != y+7
                                   or i.getP2().getX() != x+38 or i.getP2().getY() != y+38 or i.config[
                                       "fill"] != c):
                    correct = False
                if (index == 2 or index == 3 or index == 4 or index == 5) and (shape != "Line" or
                                   not (
                                        (i.getP1().getX() == x and i.getP1().getY() == y
                                        and i.getP2().getX() == x+7 and i.getP2().getY() == y+7)
                                        or
                                        (i.getP1().getX() == x+7 and i.getP1().getY() == y+7
                                        and i.getP2().getX() == x and i.getP2().getY() == y)
                                        or
                                        (i.getP1().getX() == x + 45 and i.getP1().getY() == y
                                         and i.getP2().getX() == x + 38 and i.getP2().getY() == y + 7)
                                        or
                                        (i.getP1().getX() == x + 38 and i.getP1().getY() == y + 7
                                         and i.getP2().getX() == x + 45 and i.getP2().getY() == y)
                                        or
                                        (i.getP1().getX() == x and i.getP1().getY() == y +45
                                         and i.getP2().getX() == x + 7 and i.getP2().getY() == y + 38)
                                        or
                                        (i.getP1().getX() == x + 7 and i.getP1().getY() == y + 38
                                         and i.getP2().getX() == x and i.getP2().getY() == y + 45)
                                        or
                                        (i.getP1().getX() == x + 45 and i.getP1().getY() == y + 45
                                         and i.getP2().getX() == x + 38 and i.getP2().getY() == y + 38)
                                        or
                                        (i.getP1().getX() == x + 38 and i.getP1().getY() == y + 38
                                         and i.getP2().getX() == x + 45 and i.getP2().getY() == y + 45)
                                   )):
                    correct = False

                if correct == False:
                    correct_net = False
                    print("\tObject " + str(index + 1) + ": Incorrect")
                else:
                    print("\tObject " + str(index + 1) + ": Correct")

            if correct_net:
                print("Example 1: Correct Solution")
            else:
                print("Example 1: Incorrect Solution")

        except:
            print("Example 1: Incorrect Solution")

        # Close window if the return/enter key is pressed
        while True:
            if win.checkKey() == "Return":
                win.close()
                break


    def ex2(self, f, x, y, c):
        items, tb, win = f(x, y, c)
        try:
            x = x+200
            y = y+200
            correct_net = True

            if np.round(tb.x, 5) != x:
                correct_net = False
                print("TetrisBlock.x not updated correctly")
            if np.round(tb.y, 5) != y:
                correct_net = False
                print("TetrisBlock.y not updated correctly")

            for index, i in enumerate(items):
                shape = str(i).split("(")[0]
                correct = True
                x1_pos = np.round(i.getP1().getX(), 5)
                y1_pos = np.round(i.getP1().getY(), 5)
                x2_pos = np.round(i.getP2().getX(), 5)
                y2_pos = np.round(i.getP2().getY(), 5)

                if index == 0 and (shape != "Rectangle" or x1_pos != x or y1_pos != y
                                   or x2_pos != x+45 or y2_pos != y+45 or i.config[
                                       "fill"] != c):
                    correct = False
                if index == 1 and (shape != "Rectangle" or x1_pos != x+7 or y1_pos != y+7
                                   or x2_pos != x+38 or y2_pos != y+38 or i.config[
                                       "fill"] != c):
                    correct = False
                if (index == 2 or index == 3 or index == 4 or index == 5) and (shape != "Line" or
                                   not (
                                        (x1_pos == x and y1_pos == y
                                        and x2_pos == x+7 and y2_pos == y+7)
                                        or
                                        (x1_pos == x+7 and y1_pos == y+7
                                        and x2_pos == x and y2_pos == y)
                                        or
                                        (x1_pos == x + 45 and y1_pos == y
                                         and x2_pos == x + 38 and y2_pos == y + 7)
                                        or
                                        (x1_pos == x + 38 and y1_pos == y + 7
                                         and x2_pos == x + 45 and y2_pos == y)
                                        or
                                        (x1_pos == x and y1_pos == y + 45
                                         and x2_pos == x + 7 and y2_pos == y + 38)
                                        or
                                        (x1_pos == x + 7 and y1_pos == y + 38
                                         and x2_pos == x and y2_pos == y + 45)
                                        or
                                        (x1_pos == x + 45 and y1_pos == y + 45
                                         and x2_pos == x + 38 and y2_pos == y + 38)
                                        or
                                        (x1_pos == x + 38 and y1_pos == y + 38
                                         and x2_pos == x + 45 and y2_pos == y + 45)
                                   )):
                    correct = False

                if correct == False:
                    correct_net = False
                    print("\tObject " + str(index + 1) + " Moving: Incorrect")
                else:
                    print("\tObject " + str(index + 1) + " Moving: Correct")

            if correct_net:
                print("Example 2: Correct Solution")
            else:
                print("Example 2: Incorrect Solution")
        except:
            print("Example 2: Incorrect Solution")

        # Close window if the return/enter key is pressed
        while True:
            if win.checkKey() == "Return":
                win.close()
                break

    def ex3(self, f):
        items, game = f()
        try:
            correct_net = True
            for index, i in enumerate(items):
                shape = str(i).split("(")[0]
                correct = True
                if index == 0 and (shape != "Rectangle" or i.getP1().getX() != 47.5 or i.getP1().getY() != 47.5
                                   or i.getP2().getX() != 802.5 or i.getP2().getY() != 752.5 or i.config[
                                       "fill"] != "black" or i.config["outline"] != "dark slate blue" or i.config["width"] != 3):
                    correct = False
                if index == len(items)-5-19 and (shape != "Rectangle" or i.getP1().getX() != 97.5 or i.getP1().getY() != 97.5
                                   or i.getP2().getX() != 552.5 or i.getP2().getY() != 702.5 or i.config["fill"] != "lightblue"
                                   or i.config["outline"] != "gray13" or i.config["width"] != 5):
                    correct = False
                if index == len(items)-4 and (shape != "Rectangle" or i.getP1().getX() != 575 or i.getP1().getY() != 125
                                   or i.getP2().getX() != 775 or i.getP2().getY() != 175 or i.config["fill"] != "lightblue"
                                   or i.config["outline"] != "gray13" or i.config["width"] != 2):
                    correct = False
                if index == len(items)-3 and (shape != "Text" or i.getAnchor().getX() != 677.5 or i.getAnchor().getY() != 150
                                   or i.getText() != "Tetris Game!" or i.config["font"][2] != "bold"
                                   or i.config["font"][0] != "courier" or i.config["font"][1] != 18):
                    correct = False
                if index == len(items)-2 and (shape != "Rectangle" or i.getP1().getX() != 575 or i.getP1().getY() != 225
                                   or i.getP2().getX() != 710 or i.getP2().getY() != 265 or i.config["fill"] != "lightblue"
                                   or i.config["outline"] != "gray13" or i.config["width"] != 2):
                    correct = False
                if index == len(items) - 1 and (
                        shape != "Text" or i.getAnchor().getX() != 630 or i.getAnchor().getY() != 245
                        or i.getText() != "Score: " or i.config["font"][2] != "bold"
                        or i.config["font"][0] != "courier" or i.config["font"][1] != 14):
                    correct = False

                if correct == False:
                    correct_net = False
                    if index == 0 :
                        print("\tObject " + str(index + 1) + " : Incorrect")
                    if index > len(items)-6:
                        print("\tObject " + str(index - len(items) + 6 + 1) + " : Incorrect")
                else:
                    if index == 0:
                        print("\tObject " + str(index + 1) + " : Correct")
                    if index > len(items) - 6:
                        print("\tObject " + str(index - len(items) + 6 + 1) + " : Correct")

            if correct_net:
                print("Example 3: Correct Solution")
            else:
                print("Example 3: Incorrect Solution")

        except:
            print("Example 3: Incorrect Solution")

        # Close window if the return/enter key is pressed
        while True:
            if game.win.checkKey() == "Return":
                game.win.close()
                break

    def ex4(self, f):
        game = f()
        try:
            correct_net = True
            game.newBlock()
            correct = True
            try:
                array = game.gameState
                if np.shape(array) != (12,9):
                    correct = False
            except:
                correct = False

            if correct:
                print("Example 4 Setup gameState: Correct Solution")
            else:
                correct_net = False
                print("Example 4 Setup gameState: Incorrect Solution")

            correct = True
            try:
                tb = game.currentBlock
                if tb == None:
                    correct = False
                if game.gameState[0][4] == None:
                    print("\t gameState[0][4] Incorrectly Set")
                    correct = False
                if game.currentBlockRow != 0:
                    print("\t Current Block Row Incorrectly Set")
                    correct = False
                if game.currentBlockColumn != 4:
                    print("\t Current Block Column Incorrectly Set")
                    correct = False
            except:
                correct = False

            if correct:
                print("Example 4 newBlock : Correct Solution")
            else:
                correct_net = False
                print("Example 4 newBlock : Incorrect Solution")

            if correct_net:
                print("Example 4: Correct Solution")
            else:
                print("Example 4: Incorrect Solution")
        except:
            print("Example 4: Incorrect Solution")

        # Close window if the return/enter key is pressed
        while True:
            if game.win.checkKey() == "Return":
                game.win.close()
                break

    def ex5(self, f):
        try:
            correct_net = True
            game = f()
            game.newBlock()

            correct = True
            if game.CheckMoveLeft() == False:
                correct = False
            game.gameState[0][game.currentBlockColumn - 1] = 1
            if game.CheckMoveLeft() == True:
                correct = False
            game.gameState[0][game.currentBlockColumn - 1] = None
            temp = game.currentBlockColumn
            game.currentBlockColumn = 0
            if game.CheckMoveLeft() == True:
                correct = False
            game.currentBlockColumn = temp
            if correct:
                print("Example 5 CheckMoveLeft : Correct")
            else:
                correct_net = False
                print("Example 5 CheckMoveLeft : Incorrect")

            correct = True
            if game.CheckMoveRight() == False:
                correct = False
            game.gameState[0][game.currentBlockColumn + 1] = 1
            if game.CheckMoveRight() == True:
                correct = False
            game.gameState[0][game.currentBlockColumn + 1] = None
            temp = game.currentBlockColumn
            game.currentBlockColumn = 8
            if game.CheckMoveRight() == True:
                correct = False
            game.currentBlockColumn = temp
            if correct:
                print("Example 5 CheckMoveRight : Correct")
            else:
                correct_net = False
                print("Example 5 CheckMoveRight : Incorrect")


            correct = True
            if game.CheckMoveDown() == False:
                correct = False
            game.gameState[game.currentBlockRow + 1][game.currentBlockColumn] = 1
            if game.CheckMoveDown() == True:
                correct = False
            game.gameState[game.currentBlockRow + 1][game.currentBlockColumn] = None
            temp = game.currentBlockRow
            game.currentBlockRow = 11
            if game.CheckMoveDown() == True:
                correct = False
            game.currentBlockRow = temp
            if correct:
                print("Example 5 CheckMoveDown : Correct")
            else:
                correct_net = False
                print("Example 5 CheckMoveDown : Incorrect")

            if correct_net:
                print("Example 5: Correct Solution")
            else:
                print("Example 5: Incorrect Solution")

            game.gameState[0][4].removeBlock()
            game.gameState[0][4] = None

            game.UserMoveBlock()
        except:
            print("Example 5: Incorrect Solution")
        # Close window if the return/enter key is pressed
        while True:
            if game.win.checkKey() == "Return":
                game.win.close()
                break

    def ex6(self, f, tb):
        try:
            game = f()
            correct_net = True

            # Check Termination
            correct = True
            if game.CheckTermination():
                correct = False
            game.gameState[0][0] = 1
            if game.CheckTermination() == False:
                correct = False
            game.gameState[0][0] = None

            if correct == False:
                correct_net = False
                print("Example 6 CheckTermination : Incorrect")
            else:
                print("Example 6 CheckTermination : Correct")

            # Check Row Full
            correct = True
            temp = game.currentBlockRow
            game.currentBlockRow = 11
            if game.CheckRowFull():
                correct = False
            for i in range(len(game.gameState[game.currentBlockRow])):
                game.gameState[game.currentBlockRow][i] = tb(game.win, 1000, 1000, "orange")
            if game.CheckRowFull() == False:
                correct = False
            for i in range(len(game.gameState[game.currentBlockRow])):
                game.gameState[game.currentBlockRow][i] = None
            game.currentBlockRow = temp

            if correct == False:
                correct_net = False
                print("Example 6 CheckRowFull : Incorrect")
            else:
                print("Example 6 CheckRowFull : Correct")

            # Remove Row
            correct = True
            game.currentBlockRow = 11
            for i in range(9):
                game.gameState[game.currentBlockRow][i] = tb(game.win, 1000, 1000, "orange")
            game.gameState[game.currentBlockRow-1][1] = tb(game.win, 1000, 1000, "orange")
            game.RemoveRow()
            if game.gameState[10][1] != None:
                correct = False
            if game.gameState[11][1] == None:
                correct = False
            if game.gameState[11][0] != None:
                correct = False
            game.gameState[game.currentBlockRow][0] = None
            game.gameState[game.currentBlockRow][1] = None
            game.gameState[game.currentBlockRow - 1][1] = None
            if correct == False:
                correct_net = False
                print("Example 6 RemoveRow : Incorrect")
            else:
                print("Example 6 RemoveRow : Correct")

            correct = True
            import copy
            score = copy.deepcopy(game.scoreData)
            if game.scoreVal.getText() != str(game.scoreData):
                correct = False
            game.UpdateScore(10)
            if score + 10 != game.scoreData:
                correct = False
            if game.scoreVal.getText() != str(game.scoreData):
                correct = False

            if correct == False:
                correct_net = False
                print("Example 6 UpdateScore : Incorrect")
            else:
                print("Example 6 UpdateScore : Correct")

            game.scoreVal.setText("0")
            game.scoreData = 0

            if correct_net:
                print("Example 6: Correct Solution")
            else:
                print("Example 6: Incorrect Solution")

            game.UserMoveBlock()

        except:
            print("Example 6: Incorrect Solution")

        # Close window if the return/enter key is pressed
        while True:
            if game.win.checkKey() == "Return":
                game.win.close()
                break

