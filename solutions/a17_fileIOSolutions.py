class fileIOSolutions:
    def __init__(self):
        self.fileIOSolutions = {}
        self.fileIOSolutions['example1'] = self.ex1

    def ex1(self, f):
        if f() == True:
            print("Example 1: Correct Solution")
        else:
            print("Example 1: Incorrect Solution")