class classesComplexSolutions:
    def __init__(self):
        self.classesComplexSol = {}
        self.classesComplexSol['example1'] = self.ex1

    def ex1(self, f):
        if f() == True:
            print("Example 1: Correct Solution")
        else:
            print("Example 1: Incorrect Solution")