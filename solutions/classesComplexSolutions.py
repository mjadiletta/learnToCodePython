from lessons.14_classesComplex import Book, Date, Chapter, Page


class ClassesComplexSolutions:
    def __init__(self):
        self.classesComplexSol = dict()
        self.classesComplexSol['example1'] = self.ex1

    def ex1(self, b):
        if b.title == "Python Tutorials" and b.author == "Brian" \
            and b.date.month == 3 and b.date.day == 17 and b.date.year == 2020:
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
                                                                   "some new functions."
                                        print("Example 1: Correct Solution")
                                else:
                                    print("Example 1: Incorrect Solution")
                                    print("     Page 1 was incorrectly defined")
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
