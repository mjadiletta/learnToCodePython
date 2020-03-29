"""
Practice Project 4:
Created: 3/28/2020

In this project we will use what we learned from assignments 1-15 to
to code the Game of Life!

The game of life was created by a mathematician named John Conway. It revolves
around simulating the development of a colony based on some "rules of life."
The colony is represented by a 2 dimensional grid filled with dead cells and
living cells. The rules of life are as follows:

    1. Underpopulation - any cell with fewer than 2 live neighbors becomes a dead cell.
    2. Stasis - any live cell with 2 or 3 live neighbors lives to the next generation.
    3. Overpopulation - any live cell with more than 3 live neighbors becomes a dead cell.
    4. Reproduction - if a dead cell is surrounded by 3 live cells, it becomes a live cell.

    A cell and its neighbors is defined below, where the cell is "c" and its neighbors are enumerated.

                1 2 3
                4 c 5
                6 7 8

    This game of life must be implemented iteratively, where each of these rules are checked
    in the predefined order, for every cell, for each generation.

For your implementation you will create a Colony class that creates a colony of n by n cells
that will run for g generations. Each generation you will start by enforcing the first
rule on every cell in the colony, then the second rule on every cell in the colony, and
so on. After this you will return the final generation matrix. Use the following outline
for your code and do NOT edit any code provided to you. You may use any packages/modules or
techniques you want to implement the game of life as long as you do not change the provided
code. Note that you may add anything that you want to the existing code.
"""
from solutions.CheckSolutions import CheckSolutions
checkSolutions = CheckSolutions().project4Solutions


class Colony:
    DEFAULT_SEED = [[0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
                    [0, 0, 1, 0, 0, 1, 0, 1, 0, 0],
                    [0, 0, 1, 1, 0, 0, 0, 1, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                    [0, 0, 0, 0, 0, 1, 1, 0, 1, 1],
                    [0, 0, 0, 1, 0, 1, 0, 1, 0, 1],
                    [0, 0, 1, 1, 0, 1, 0, 0, 0, 1],
                    [0, 0, 1, 1, 1, 0, 0, 0, 0, 1],
                    [0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
                    [0, 0, 0, 0, 0, 1, 1, 1, 1, 0]]
    DEFAULT_SIZE = 10
    DEFAULT_GENS = 10

    def __init__(self, size=DEFAULT_SIZE, generations=DEFAULT_GENS, seed=DEFAULT_SEED):
        self.size = size
        self.gens = generations
        self.current_gen = seed
        self.next_gen = seed

    def print_gen(self, g=None):
        if g is not None:
            print("\nGeneration {}".format(g))
        for i in self.current_gen:
            line = ""
            for j in i:
                line += str(j) + " "
            print(line)

    def neighbors(self, x, y):
        total = 0

        # 1. top left
        if x - 1 >= 0 and y - 1 >= 0:
            if self.current_gen[x-1][y-1] == 1:
                total += 1

        # 2. top middle
        if y - 1 >= 0:
            if self.current_gen[x][y - 1] == 1:
                total += 1

        # 3. top right
        if x + 1 < self.size and y - 1 >= 0:
            if self.current_gen[x + 1][y - 1] == 1:
                total += 1

        # 4. middle left
        if x - 1 >= 0:
            if self.current_gen[x - 1][y] == 1:
                total += 1

        # 5. middle right
        if x + 1 < self.size:
            if self.current_gen[x + 1][y] == 1:
                total += 1

        # 6. bottom left
        if x - 1 >= 0 and y + 1 < self.size:
            if self.current_gen[x - 1][y + 1] == 1:
                total += 1

        # 7. bottom middle
        if y + 1 < self.size:
            if self.current_gen[x][y + 1] == 1:
                total += 1

        # 8. bottom right
        if x + 1 < self.size and y + 1 < self.size:
            if self.current_gen[x + 1][y + 1] == 1:
                total += 1

        return total

    def play(self):
        # this function runs through all the generations and returns the final gen
        for g in range(self.gens):
            self.print_gen(g)
            self.current_gen = self.next_gen
            for x, e1 in enumerate(self.current_gen):
                for y, e2 in enumerate(e1):
                    n = self.neighbors(x, y)
                    if e2 == 1 and (n < 2 or n > 3):
                        # alive
                        self.next_gen[x][y] = 0
                    elif e2 == 0 and n == 3:
                        # dead
                        self.next_gen[x][y] = 1

        self.current_gen = self.next_gen
        self.print_gen("Final")
        return self.current_gen


checkSolutions["project4"](Colony)
