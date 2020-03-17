"""
Practice Group 13: Classes Simple
Created: 3/17/2020

In this tutorial we will cover some basic object oriented programming concepts.
Object oriented programming or OOP is a programming paradigm (way of writing
and organizing your code). OOP is based around these things called "objects."
What is an object? It's basically an abstract way to organize portions of your
code and store data that needs to be used by that code. In order to create an
object you first need to define a class. The class is like a template for the
object. Think of it like an empty job application. When you fill out the
job application you have just created an object, or an instance of the job
application class. Using OOP, our code will be easy to read and well organized.
Note that Python is not the only language that supports OOP. Other languages
like Java, C++, and JavaScript also support OOP. However, there are other
programming paradigms, and languages that support them, that we will not cover
in this lecture series. (Sorry for the block text)

Learning Objectives:
    1. Define a class
    2. Define class attributes
    3 Define a class method
    4. Create a constructor method


Example 1 is completed as a template.
For each of the following examples, replace blank lines
with the correct functionality. If completed correctly, the checkSolutions
will print "Correct Solution" to the terminal.
"""

from solutions.CheckSolutions import CheckSolutions
checkSolutions = CheckSolutions().classesSimpleSolutions

'''
Example 1: Define a class

In this example you will learn how to define a class in Python. Remember that 
the class is the template that you will use to create objects in your program. 
So everything must be generalized. We have included an example of a class 
definition below. Please use this example to create your own class called "Application"
NOTE: you can just copy the methods/functions from the example class.
'''


class Example:
    def __init__(self):
        self.attribute1 = 1

    def check(self):
        if self.attribute1 == 1:
            return True

# Please write your class below :)

#checkSolutions['example1'](ex1)


'''
Example 2: Class Attributes 

In the previous example you basically had to write one line of code and you 
copied a couple of functions from the example class. In this example we will 
introduce the concept of class attributes. An attribute is basically a variable 
that stores data for each object that you create. If you want to apply for a job 
you might need to put your name, address, date of birth, and some other information.
Each of these pieces of information may be considered an attribute of the Application 
class. We have already included the Application class you created in the previous 
example, with one attribute. Please add the DOB (date of birth - just the year 
the person was born), SSN (social security number), and position attributes to the 
Application class. 
NOTE: these attributes are all defined within this "__init__" function... just accept 
this for now, we will talk more about this later.
'''


class Application:
    def __init__(self, name_input):
        self.name = name_input

    def submit(self):
        print("Submitted " + self.name + "'s application!")


'''
Example 3: Class methods 

Now that you understand what an attribute is, we will discuss what a method is. 
In the introduction to this lecture we mentioned two things that were included 
in an object: code and data. Attributes represent the data stored in an object 
and methods represent the code that manipulates that data for the object. Specifically,
a method is a function contained within a class, that has access to the class attributes 
and may be "called on an object of that class." 

That phrase may have been confusing so lets break it down. To call a method or function 
just means to execute the function after you have defined it. In order to execute the 
function you need to write the function name and pass any inputs required by the function. 
E.g.: assume you have a function called walk defined that requires one integer input... 
To call the function you would write "walk(23)" in your code. 

Calling a function on an object is very similar, however, you need to be sure that the 
function you are calling was defined within the class. In the previous example, we 
defined a class Application, so if we created an object called "app1" based on the Application 
class we can call the "submit" function with the following code:
        app1.submit()

Ok, that's a lot of information. Hopefully you understood most of that. Please try to add 
another method to our Application class called "calculate_applicant_age." This function will
simply calculate the age (in years) of the applicant based on the DOB attribute (the year 
the applicant was born) and return that age. Assume the current year is 2020.
'''


class Application:
    def __init__(self, name_in, dob_in, ssn_in, position_in):
        self.name = name_in  # STRING: name of applicant
        self.dob = dob_in    # INT: year the applicant was born
        self.ssn = ssn_in    # STRING: social security number of the applicant (xxx-xx-xxxx)
        self.position = position_in  # STRING: name of the position being applied for

    def submit(self):
        print("Submitted " + self.name + "'s application!")

    # add the calculate_applicant_age method here. (Hint: use the submit method as a template)



'''
Example 4: Class constructor methods

In the previous three examples you have seen this "__init__" method, now you will find out 
exactly what it means. The "__init__" method is a constructor. This method constructs an 
object based on the class. When you try to make an object from a class you have defined the 
"__init__" method will be executed IMMEDIATELY. In Python the __init__ method is used to define 
class attributes. The inputs to the __init__ method are the data necessary for defining the 
attributes for that particular object. As you have seen, when you create a new attribute you need 
to add a new input to your __init__ method definition (e.g., name_in, dob_in, ssn_in, and position_in).

There may be some instances when you don't need any data to be input in order to define an attribute, 
but don't worry about that right now :)

Because you have already defined a constructor in the previous examples in this one you will create a 
new object. Please name the object "app2" and use the definition of "app1" below as a reference. 
Once you have created the object, call the calculate_applicant_age method and print the result.

Your applicant should have the following values for its application:
        NAME: Shane
        DOB: 1995
        SSN: 123-45-6789
        POSITION: Manager
'''


class Application:
    def __init__(self, name_in, dob_in, ssn_in, position_in):
        self.name = name_in  # STRING: name of applicant
        self.dob = dob_in  # INT: year the applicant was born
        self.ssn = ssn_in  # STRING: social security number of the applicant (xxx-xx-xxxx)
        self.position = position_in  # STRING: name of the position being applied for

    def submit(self):
        print("Submitted " + self.name + "'s application!")

    def calculate_applicant_age(self):
        return 2020 - self.dob


# MAKE SURE YOUR SPACING IS CORRECT
# YOU DON'T WANT TO ACCIDENTALLY INCLUDE YOUR
#    CODE IN YOUR CLASS AND CAUSE A BUNCH OF ERRORS

app1 = Application("Matt", 1998, "000-11-2222", "CEO")
app1.submit()

# Create your object here!


