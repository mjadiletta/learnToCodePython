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

    def play(self):
        # this function runs through all the generations and returns the final gen

        return self.current_gen  # make sure to return the final generation of the colony in the same format as the seed


'''
Some HINTS:
    1. write a nice print function that will print out the current generation for you 
    2. figure out how you will store the current generation layout and the next generation layout 
    3. remember the edge cases... most cells will have 8 neighbors but those on the edges of the matrix (colony) 
        won't have as many
    4. each of the rules can be conditional statements...
'''


checkSolutions["project4"](Colony)
