import numpy as np
import copy

class projectSolutions:
    def __init__(self):
        self.projectSolutions = {}

        self.projectSolutions['project3p1a'] = self.proj3p1a
        self.projectSolutions['project3p2a'] = self.proj3p2a
        self.projectSolutions['project3p2b'] = self.proj3p2b
        self.projectSolutions['project3p3'] = self.proj3p3
        self.projectSolutions['project3p5'] = self.proj3p5


    def proj3p1a(self, f):
        try:
            gb = f()
            correct = True
            if np.shape(gb) != (3, 3):
                correct = False
            for r in range(3):
                for c in range(3):
                    if gb[r][c] != '-':
                        correct = False
            if correct:
                print("Project 3 P1a: Correct Solution")
            else:
                print("Project 3 P1a: Incorrect Solution")
        except:
            print("Project 3 P1a: Incorrect Solution")

    def proj3p2a(self, f):
        import os
        import sys
        from io import StringIO
        temp_in = sys.stdin
        sys.stdin = StringIO('1\n2\n')
        temp_out = sys.stdout
        sys.stdout = open("./temp.txt", "w")
        r, c = f()
        sys.stdout.close()
        os.remove("./temp.txt")
        sys.stdin = temp_in
        sys.stdout = temp_out
        if r == 1 and c == 2:
            print("Project 3 P2a: Correct Solution")
        else:
            print("Project 3 P2a: Incorrect Solution")

    def proj3p2b(self, f, game_board):
        import os
        import sys
        from io import StringIO
        game_board = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
        game_board[0][1] = 'O'
        game_board[0][2] = 'O'
        temp_in = sys.stdin
        sys.stdin = StringIO('0\n0\n4\n10\n1\n2\n1\n3\n2\n1\n')
        temp_out = sys.stdout
        sys.stdout = open("./temp.txt", "w")
        r, c = f(game_board)
        sys.stdout.close()
        os.remove("./temp.txt")
        sys.stdin = temp_in
        sys.stdout = temp_out
        if r == 2 and c == 1:
            print("Project 3 P2b: Correct Solution")
        else:
            print("Project 3 P2b: Incorrect Solution")

    def proj3p3(self, f, game_board):
        import os
        import sys
        from io import StringIO
        game_board = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
        game_board[0][1] = 'O'
        game_board[0][2] = 'O'
        temp_in = sys.stdin
        sys.stdin = StringIO('0\n0\n4\n10\n1\n2\n1\n3\n2\n1\n')
        temp_out = sys.stdout
        sys.stdout = open("./temp.txt", "w")
        f(game_board)
        sys.stdout.close()
        os.remove("./temp.txt")
        sys.stdin = temp_in
        sys.stdout = temp_out

        if game_board == [['-', 'O', 'O'], ['O', '-', '-'], ['-', '-', '-']]:
            print("Project 3 P3: Correct Solution")
        else:
            print("Project 3 P3: Incorrect Solution")

    def checkTermination(self, gb):
        termination = True
        tieOrWin = "tie"
        for row in gb:
            for column in row:
                if column == "-":
                    termination = False
                    tieOrWin = None
        if gb[0][0] == gb[1][0] and gb[0][0] == gb[2][0] and gb[0][0] != '-' or \
                gb[0][1] == gb[1][1] and gb[0][1] == gb[2][1] and gb[0][1] != '-' or \
                gb[0][2] == gb[1][2] and gb[0][2] == gb[2][2] and gb[0][2] != '-' or \
                gb[0][0] == gb[0][1] and gb[0][0] == gb[0][2] and gb[0][0] != '-' or \
                gb[1][0] == gb[1][1] and gb[1][0] == gb[1][2] and gb[1][0] != '-' or \
                gb[2][0] == gb[2][1] and gb[2][0] == gb[2][2] and gb[2][0] != '-' or \
                gb[0][0] == gb[1][1] and gb[0][0] == gb[2][2] and gb[0][0] != '-' or \
                gb[2][0] == gb[1][1] and gb[2][0] == gb[0][2] and gb[2][0] != '-':
            termination = True
            tieOrWin = "win"
        return termination, tieOrWin

    def proj3p5(self, f, game_board):
        correct = True
        gb_win_row_1 = [['O', 'O', 'O'], ['-', '-', '-'], ['-', '-', '-']]
        gb_win_row_2 = [['-', '-', '-'], ['O', 'O', 'O'], ['-', '-', '-']]
        gb_win_row_3 = [['-', '-', '-'], ['-', '-', '-'], ['O', 'O', 'O']]
        gb_win_column_1 = [['O', '-', '-'], ['O', '-', '-'], ['O', '-', '-']]
        gb_win_column_2 = [['-', 'O', '-'], ['-', 'O', '-'], ['-', 'O', '-']]
        gb_win_column_3 = [['-', '-', 'O'], ['-', '-', 'O'], ['-', '-', 'O']]
        gb_win_diag_b = [['O', '-', '-'], ['-', 'O', '-'], ['-', '-', 'O']]
        gb_win_diag_f = [['-', '-', 'O'], ['-', 'O', '-'], ['O', '-', '-']]

        if f(gb_win_row_1) != (True, "win") or\
                f(gb_win_row_2) != (True, "win") or\
                f(gb_win_row_3) != (True, "win") or\
                f(gb_win_column_1) != (True, "win") or\
                f(gb_win_column_2) != (True, "win") or\
                f(gb_win_column_3) != (True, "win") or\
                f(gb_win_diag_b) != (True, "win") or\
                f(gb_win_diag_f) != (True, "win"):
            correct = False

        chars = ["-", "X", "O"]
        randInt = lambda: np.random.randint(0, 2)
        for i in range(100):
            game_board = [[chars[randInt()], chars[randInt()], chars[randInt()]],
                          [chars[randInt()], chars[randInt()], chars[randInt()]],
                          [chars[randInt()], chars[randInt()], chars[randInt()]]]
            if f(game_board) != self.checkTermination(game_board):
                correct = False
        if correct:
            print("Project 3 P5: Correct Solution")
        else:
            print("Project 3 P5: Incorrect Solution")
