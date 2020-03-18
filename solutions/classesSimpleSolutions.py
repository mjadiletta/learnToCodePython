class classesSimpleSolutions:
    def __init__(self):
        self.classesSimpleSol = {}
        self.classesSimpleSol['example1'] = self.ex1
        self.classesSimpleSol['example2'] = self.ex2
        self.classesSimpleSol['example3'] = self.ex3
        self.classesSimpleSol['example4'] = self.ex4
        self.classesSimpleSol['example5'] = self.ex5

    def ex1(self, obj):
        try:
            if obj.attribute1:
                print("Example 1: Correct Solution")
            else:
                print("Example 1: Incorrect Solution")
        except:
            print("Example 1: Incorrect Solution")

    def ex2(self, obj):
        try:
            if obj.name == "Sam":
                print("Example 2: Correct Solution")
            else:
                print("Example 2: Incorrect Solution")
        except:
            print("Example 2: Incorrect Solution")

    def ex3(self, obj):
        try:
            app = obj("0", "0", "0", "0")
            if app.name and app.dob and app.ssn and app.position:
                print("Example 3: Correct Solution")
            else:
                print("Example 3: Incorrect Solution")
        except:
            print("Example 3: Incorrect Solution")

    def ex4(self, obj):
        try:
            app = obj(name_in="Matt", dob_in=1998, ssn_in="000-00-0000", position_in="CEO")
            if app.calculate_applicant_age() == 2020 - 1998:
                print("Example 4: Correct Solution")
            else:
                print("Example 4: Incorrect Solution")
        except:
            print("Example 4: Incorrect Solution")

    def ex5(self, app):
        try:
            if app.name == "Shane" and app.dob == 1995 and app.ssn == "123-45-6789" and app.position == "Manager" and app.calculate_applicant_age() == 2020 - 1995:
                print("Example 5: Correct Solution")
            else:
                print("Example 5: Incorrect Solution")
        except:
            print("Example 5: Incorrect Solution")