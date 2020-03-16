import numpy as np
import copy as cp

class dictionarySol:
    def ex1(self, f):
        correct_sol = {"car": ["4 wheels", "steering wheel", "4 doors"],
                         "motorcycle": ["2 wheels", "no doors"],
                         "plane": ["6 wheels", "wings", "emergency exits"]}
        out = f()
        correct = True
        for key, value in correct_sol.items():
            try:
                out[key]
            except:
                correct = False
                break
            for e_sol in correct_sol[key]:
                temp_correct = False
                for e in value:
                    if e_sol == e:
                        temp_correct = True
                if not temp_correct:
                    correct = False
                    break
        if correct:
            print("Example 1: Correct Solution")
        else:
            print("Example 1: Incorrect Solution")

    def ex2(self, f):
        correct_sol = {"school_materials": ["pencil", "pen", "eraser"], "dairy": ["milk", "cheese"], "dinner": ["steak", "pizza"]}
        out = f()
        correct = True
        for key, value in correct_sol.items():
            try:
                out[key]
            except:
                correct = False
                break
            for e_sol in value:
                temp_correct = False
                for arr in out.values():
                    for e in arr:
                        if e_sol == e:
                            temp_correct = True
                if not temp_correct:
                    correct = False
                    break

        if correct:
            print("Example 2: Correct Solution")
        else:
            print("Example 2: Incorrect Solution")

    def ex3(self, f):
        correct_sol = ["dairy", "school_materials",  "dinner"]
        if sorted(f()) == sorted(correct_sol):
            print("Example 3: Correct Solution")
        else:
            print("Example 3: Incorrect Solution")

    def ex4(self, f):
        correct_sol = ["pencil", "pen", "eraser", "milk", "cheese", "steak", "pizza"]
        if sorted(f()) == sorted(correct_sol):
            print("Example 4: Correct Solution")
        else:
            print("Example 4: Incorrect Solution")

    def ex5(self, f):
        correct_sol = (sorted(['car', 'motorcycle', 'plane']), sorted(['4 wheels', 'steering wheel', '4 doors', '2 wheels', 'no doors', '6 wheels', 'wings', 'emergency exits']))
        out = f()
        if (sorted(out[0]), sorted(out[1])) == correct_sol:
            print("Example 5: Correct Solution")
        else:
            print("Example 5: Incorrect Solution")

    def ex6(self, f):
        correct_sol = {'car': ['4 wheels', 'steering wheel', '4 doors'],
                       'motorcycle': ['2 wheels', 'no doors'],
                       'plane': ['6 wheels', 'wings', 'emergency exits'],
                       'school_materials': ['pen', 'pencil', 'eraser'],
                       'dairy': ['milk', 'cheese'],
                       'dinner': ['steak', 'pizza']}
        out = f()
        correct = True
        for key, value in correct_sol.items():
            try:
                out[key]
            except:
                correct = False
                break

            for e_sol in value:
                temp_correct = False
                for arr in out.values():
                    for e in arr:
                        if e_sol == e:
                            temp_correct = True
                if not temp_correct:
                    correct = False
                    break

        if correct:
            print("Example 6: Correct Solution")
        else:
            print("Example 6: Incorrect Solution")

    def ex7(self, f):
        correct_sol = {'brian_damore': np.array([24.49, 23.64, 24.67, 23.41, 23.53, 23.21,
                                              23.07, 22.63, 22.41, 22.12, 22.85, 22.82]),
                       'antoine_harris': np.array([22.82, 22.47, 22.14, 22.27, 22.25, 22.26,
                                                22.  , 22.7 , 21.79, 21.86, 21.49, 22.27]),
                       'tyler_hanson': np.array([22.4 , 22.39, 22.49, 22.5 , 22.17, 22.25,
                                              22.  , 22.05, 21.8 , 21.57, 21.43, 21.82]),
                       'alex_rus': np.array([22.68, 22.36, 22.25, 22.43, 22.26, 22.31,
                                          22.91, 21.83, 22.51, 22.3 , 22.39, 22.99])
                       }
        out = f()
        correct = True
        for key, value in correct_sol.items():
            try:
                out[key]
            except:
                correct = False
                break

            for e_sol in value:
                temp_correct = False
                for arr in out.values():
                    for e in arr:
                        if e_sol == e:
                            temp_correct = True
                if not temp_correct:
                    correct = False
                    break

        if correct:
            print("Example 7: Correct Solution")
        else:
            print("Example 7: Incorrect Solution")

    def ex8(self, f):
        correct_sol = ([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11],
                        [24.49, 23.64, 24.67, 23.41, 23.53, 23.21, 23.07, 22.63, 22.41,   22.12, 22.85, 22.82],
                        [ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11],
                        [22.82, 22.47, 22.14, 22.27, 22.25, 22.26, 22.  , 22.7 , 21.79, 21.86, 21.49, 22.27],
                        [ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11],
                        [22.4 , 22.39, 22.49, 22.5 , 22.17, 22.25, 22.  , 22.05, 21.8 , 21.57, 21.43, 21.82],
                        [ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11],
                        [22.68, 22.36, 22.25, 22.43, 22.26, 22.31, 22.91, 21.83, 22.51, 22.3 , 22.39, 22.99])
        out = f()

        correct = True
        try:
            for i in range(len(correct_sol)):
                for j in range(len(correct_sol[i])):
                    if (correct_sol[i][j] != out[i][j]):
                        correct = False
            if correct:
                print("Example 8: Correct Solution")
            else:
                print("Example 8: Incorrect Solution")
        except:
            print("Example 8: Incorrect Solution")

