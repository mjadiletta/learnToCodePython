class classesSimpleSolutions:
    def __init__(self):
        self.classesSimpleSol = {}
        self.classesSimpleSol['example1'] = self.ex1

    def ex1(self, f):
        if f() == True:
            print("Example 1: Correct Solution")
        else:
            print("Example 1: Incorrect Solution")