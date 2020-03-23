class classesComplexSolutions:
    def __init__(self):
        self.classesComplexSol = dict()
        self.classesComplexSol['example1'] = self.ex1
        self.classesComplexSol['example2'] = self.ex2

    def ex1(self, b):
        if b.title == "Python Tutorials" and b.author == "Brian" \
                and b.date.month == 3 and b.date.day == 17 and b.date.year == 2017:
            if len(b.gen_toc()) == 3:
                if b.chapters[0].title == "Intro to Python" \
                        and b.chapters[0].get_first_page() == 1:
                    if b.chapters[1].title == "Intro to OOP" \
                            and b.chapters[1].get_first_page() == 3:
                        if b.chapters[1].title == "Intro to OOP" \
                                and b.chapters[1].get_first_page() == 3:
                            if b.chapters[0].pages[0].number == 1 and \
                                b.chapters[0].pages[0].text == "Welcome to Python! Time to create " \
                                                               "a Hello World application.":
                                if b.chapters[0].pages[1].number == 2 and \
                                    b.chapters[0].pages[1].text == "Great job! Now lets start creating " \
                                                                   "some new functions.":
                                    if b.chapters[1].pages[0].number == 3 and \
                                        b.chapters[1].pages[0].text == "Now that you know some python lets " \
                                                                       "learn some OOP concepts.":
                                        if b.chapters[1].pages[1].number == 4 and \
                                                b.chapters[1].pages[1].text == "Classes, attributes, methods, " \
                                                                               "objects, inheritance, etc.":
                                            if b.chapters[2].pages[0].number == 5 and \
                                                    b.chapters[2].pages[0].text == "Lets create a game of life " \
                                                                                   "simulation":
                                                if b.chapters[2].pages[1].number == 6 and \
                                                        b.chapters[2].pages[1].text == "Here are all the rules your " \
                                                                                       "simulation needs to follow.":
                                                    print("Example 1: Correct Solution")
                                                else:
                                                    print("Example 1: Incorrect Solution")
                                                    print("     Page 6 was incorrectly defined")
                                            else:
                                                print("Example 1: Incorrect Solution")
                                                print("     Page 5 was incorrectly defined")
                                        else:
                                            print("Example 1: Incorrect Solution")
                                            print("     Page 5 was incorrectly defined")
                                    else:
                                        print("Example 1: Incorrect Solution")
                                        print("     Page 3 was incorrectly defined")
                                else:
                                    print("Example 1: Incorrect Solution")
                                    print("     Page 2 was incorrectly defined")
                            else:
                                print("Example 1: Incorrect Solution")
                                print("     Page 1 was incorrectly defined")
                        else:
                            print("Example 1: Incorrect Solution")
                            print("     Chapter 3 was incorrectly defined")
                    else:
                        print("Example 1: Incorrect Solution")
                        print("     Chapter 2 was incorrectly defined")
                else:
                    print("Example 1: Incorrect Solution")
                    print("     Chapter 1 was incorrectly defined")

            else:
                print("Example 1: Incorrect Solution")
                print("     You didn't add all the three chapters")
        else:
            print("Example 1: Incorrect Solution")
            print("     Why did you change the tutorials object?")

    def ex2(self, v, t, m):
        flag = True

        if not v.num_wheels == 5 or not v.num_passengers == 1:
            flag = False
            print("Example 2: Incorrect Solution")
            print("           Check your definition of the vehicle class.")

        if not t.num_wheels == 4 or not t.num_passengers == 2:
            flag = False
            print("Example 2: Incorrect Solution")
            print("           Check your definition of the Truck class.")

        if not t.bed_size == 20 or not t.cab_size == 10:
            flag = False
            print("Example 2: Incorrect Solution")
            print("           Check your definition of the Truck class.")

        if not t.tow() == "Towing..." or not t.drive() == 23:
            flag = False
            print("Example 2: Incorrect Solution")
            print("           Check your definition of the Truck class.")

        if not m.num_wheels == 3 or not m.num_passengers == 3 or not m.handlebar_type == "Cross" or not m.side_cab == True:
            flag = False
            print("Example 2: Incorrect Solution")
            print("           Check your definition of the MotorCycle class attributes.")

        if not m.skid() == 123456 or not m.drive() == 56:
            flag = False
            print("Example 2: Incorrect Solution")
            print("           Check your definition of the MotorCycle class methods.")

        if flag:
            print("Example 2: Correct Solution")
