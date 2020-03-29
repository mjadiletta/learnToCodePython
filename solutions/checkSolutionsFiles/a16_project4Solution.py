class project4Solutions:
    def __init__(self):
        self.projectSolutions = dict()
        self.projectSolutions['project4'] = self.proj4


    def proj4(self, c):
        correct = True
        if not (c(generations=50).play() == [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                             [0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
                                             [0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
                                             [0, 0, 0, 1, 0, 0, 0, 1, 1, 0],
                                             [0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
                                             [0, 0, 0, 1, 0, 0, 0, 1, 1, 0],
                                             [0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
                                             [0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
                                             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]):
            print("Project 4: Incorrect Solution")
            correct = False

        if not (c(generations=100).play() == [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                            [0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
                                            [0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
                                            [0, 0, 0, 1, 0, 0, 0, 1, 1, 0],
                                            [0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
                                            [0, 0, 0, 1, 0, 0, 0, 1, 1, 0],
                                            [0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
                                            [0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
                                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]):
            print("Project 4: Incorrect Solution")
            correct = False

        if correct:
            print("Project 4: Correct Solution")
