import numpy as np

class ticTacToe():
    def createBoard(self):
        gb = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]
        return gb

    def printGameBaord(self, gb):
        for row in gb:
            for i in range(len(row)):
                if i < len(row)-1:
                    print(" " + row[i] + " |", end='')
                else:
                    print(" " + row[i])


    def markBoardUser(self, gb):
        def row_sum(pgb, row):
            sum = np.sum(pgb[row])
            if sum == 4:
                sum = 8
            if sum == 6:
                sum = 12
            if sum == 5:
                sum = 1
            return sum
        def column_sum(pgb, col):
            sum = np.sum(pgb.T[col])
            if sum == 4:
                sum = 8
            if sum == 6:
                sum = 12
            if sum == 5:
                sum = 1
            return sum
        def back_horiz(pgb):
            sum = pgb[0][0] + pgb[1][1] + pgb[2][2]
            if sum == 4:
                sum = 8
            if sum == 6:
                sum = 12
            if sum == 5:
                sum = 1
            #if sum == 3 and pgb[2][0] == 2 and pgb[0][2] == 2:
            #    sum = 0
            return sum
        def for_horiz(pgb):
            sum = pgb[0][2] + pgb[1][1] + pgb[2][0]
            if sum == 4:
                sum = 8
            if sum == 6:
                sum = 12
            if sum == 5:
                sum = 1
            if sum == 3 and pgb[0][0] == 2 and pgb[2][2] == 2:
                sum = 0
            return sum
        pgb = np.zeros((3,3))
        pgbf = np.zeros((3,3))
        for r in range(3):
            for c in range(3):
                if gb[r][c] == 'X':
                    pgb[r][c] += 2
                if gb[r][c] == 'O':
                    pgb[r][c] += 3
        for r in range(3):
            for c in range(3):
                if gb[r][c] == '-':
                    pgbf[r][c] = row_sum(pgb, r)
                    pgbf[r][c] += column_sum(pgb, c)
                    if r == 0 and c == 0 or r == 1 and c == 1 or r == 2 and c == 2:
                        pgbf[r][c] += back_horiz(pgb)
                    if r == 2 and c == 0 or r == 1 and c == 1 or r == 0 and c == 2:
                        pgbf[r][c] += for_horiz(pgb)
        pgbf[1][1] += 1
        #print(pgbf)
        pgbf = pgbf.reshape(9,1)
        max = np.argmax(pgbf)
        r = int(max/3)
        c = max%3
        gb[r][c] = "O"

    def markBoardCPU(self, gb):
        def row_sum(pgb, row):
            sum = np.sum(pgb[row])
            if sum == 4:
                sum = 8
            if sum == 6:
                sum = 12
            if sum == 5:
                sum = 1
            return sum
        def column_sum(pgb, col):
            sum = np.sum(pgb.T[col])
            if sum == 4:
                sum = 8
            if sum == 6:
                sum = 12
            if sum == 5:
                sum = 1
            return sum
        def back_horiz(pgb):
            sum = pgb[0][0] + pgb[1][1] + pgb[2][2]
            if sum == 4:
                sum = 8
            if sum == 6:
                sum = 12
            if sum == 5:
                sum = 1
            #if sum == 3 and pgb[2][0] == 2 and pgb[0][2] == 2:
            #    sum = 0
            return sum
        def for_horiz(pgb):
            sum = pgb[0][2] + pgb[1][1] + pgb[2][0]
            if sum == 4:
                sum = 8
            if sum == 6:
                sum = 12
            if sum == 5:
                sum = 1
            if sum == 3 and pgb[0][0] == 2 and pgb[2][2] == 2:
                sum = 0
            return sum
        pgb = np.zeros((3,3))
        pgbf = np.zeros((3,3))
        for r in range(3):
            for c in range(3):
                if gb[r][c] == 'O':
                    pgb[r][c] += 2
                if gb[r][c] == 'X':
                    pgb[r][c] += 3
        for r in range(3):
            for c in range(3):
                if gb[r][c] == '-':
                    pgbf[r][c] = row_sum(pgb, r)
                    pgbf[r][c] += column_sum(pgb, c)
                    if r == 0 and c == 0 or r == 1 and c == 1 or r == 2 and c == 2:
                        pgbf[r][c] += back_horiz(pgb)
                    if r == 2 and c == 0 or r == 1 and c == 1 or r == 0 and c == 2:
                        pgbf[r][c] += for_horiz(pgb)
        pgbf[1][1] += 1
        #print(pgbf)
        pgbf = pgbf.reshape(9,1)
        max = np.argmax(pgbf)
        r = int(max/3)
        c = max%3
        gb[r][c] = "X"

    def checkTermination(self, gb):
        termination = True
        tieOrWin = "tie"
        for row in gb:
            for column in row:
                if column == "-":
                    termination = False
                    tieOrWin = None
        if  gb[0][0] == gb[1][0] and gb[0][0] == gb[2][0] and gb[0][0] != '-' or \
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


    def playGame(self, game_board):
        whose_turn = 0
        terminate_game = False
        self.printGameBaord(game_board)
        while not terminate_game:
            print("----------------------")
            if whose_turn == 0:
                print("CPU 1 Turn")
                self.markBoardUser(game_board)
                whose_turn = 1
            else:
                print("CPU 2 Turn")
                self.markBoardCPU(game_board)
                whose_turn = 0
            self.printGameBaord(game_board)
            terminate_game, tieOrWin = self.checkTermination(game_board)

        print("----------------------")
        if tieOrWin == "win":
            if whose_turn == 0:
                print("CPU 2 Winner")
            else:
                print("CPU 1 Winner")
        else:
            print("Tie Game")
        self.printGameBaord(game_board)

