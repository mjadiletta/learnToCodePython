"""
Practice Group 14: Classes
Created: 3/17/2020

In this tutorial we will cover more complex examples of object
oriented programming. We will also delve into some other OOP
topics including inheritance, interfaces, and polymorphism.

Learning Objectives:
    1. Create classes that reference each other
    2. Create an Abstract/Super class and subclasses
    3. Create your first interface
    4. Bring it all together and learn a little polymorphism


"""

from abc import ABC, abstractmethod, abstractproperty
from solutions.CheckSolutions import CheckSolutions
checkSolutions = CheckSolutions().classesComplexSolutions

'''
Example 1: Objects in classes in classes in classes ...

In this example we will explore applications of classes. We 
will also see that classes may build upon each other and reference 
one another in their definitions.

Let's write a book!

First, we will outline what this should look like. 

A book is made up of chapters, a table of contents, maybe some end notes. 
Each chapter has a title, a number, and a bunch of pages. Each of these 
pages also has a number, and some text. 

So for this example let's create three classes that reference each other 
and then lets write a short book!

DEFINITIONS:

Book:
    - Title
    - Author
    - Publication Date
    - Table of Contents
    - Multiple (variable number of) chapters
Chapter:
    - Title
    - Number
    - Multiple (variable number of) pages
Page:
    - Number
    - Text (limit the number of characters to 50 for now)

Date:
    - Month
    - Day 
    - Year

'''


class Date:
    def __init__(self, mm, dd, yyyy):
        self.day = dd
        self.month = mm
        self.year = yyyy

    '''
    The following method automatically converts the information stored in 
    this class to a string. So when you print an instance of this class (aka 
    an object) it will call this function to convert the class into a string 
    that may be printed. By default, this method is not defined, however, you 
    can define it for any of your custom classes. It may be useful to do so, 
    depending on your use case.
    '''
    def __str__(self):
        return str(self.month) + '/' + str(self.day) + '/' + str(self.year)


class Book:
    '''
    Notice the fact that I didn't need to have a table of contents or
    chapters input to the __init__ method. I have defined the class this
    way because it allows me to add chapters as I "write" them with the
    add_chapter method, instead of predefining all of the chapters before
    I create the book.
    '''
    def __init__(self, title_in, author_in, date_in):
        self.title = title_in
        self.author = author_in
        self.date = date_in
        self.chapters = list()

    '''
    For this method you should notice that one of the inputs looks different...
    Specifically, the "index" input is set equal to False. By writing this in the 
    function definition we have created an optional input argument to our method. 
    What does that mean? If someone chooses to run this method they may provide a 
    value for index, however, it is not necessary that they provide this value. 
    If they choose not to provide a value then the value of "index" will default to 
    "False". We handle both possible cases (index is False, or the user provides a value)
    in the method with a conditional statement.
    '''
    def add_chapter(self, chap, index=False):
        if not index:
            self.chapters.append(chap)
        else:
            self.chapters.insert(index, chap)

    '''
    For the table of contents (TOC or toc), we had two options for how it would be 
    represented. First, we could have an attribute to the class that is updated each 
    time a new chapter is added. Or, second, we could have a method that generates the 
    TOC each time we need it. I opted for using a method instead of an attribute because 
    the TOC does not contain data that is different from the list of chapters attribute. 
    Therefore, there is no reason to store a copy of the data stored in the chapter's 
    attribute, in a new TOC attribute. Instead we can create a method that simply manipulates 
    the data stored in the chapters attribute to give us what we need for a TOC.    
    '''
    def gen_toc(self):
        toc = list()

        for c in self.chapters:
            toc.append((c.title, c.get_first_page()))

        return toc


class Chapter:
    '''
    Just an FYI, you might see this more in these tutorials... the "pass" statement you see
    below is just a place holder. It basically tells the Python Interpreter (what builds and
    runs your code for you) to just "pass" this class or function because it doesn't do
    anything. So in here we use them as placeholders. You should delete the pass statement and
    write your own definition of the class.
    '''
    pass


class Page:
    pass


pub_date = Date(3, 17, 2017)
tutorials = Book("Python Tutorials", "Brian", pub_date)

# create three chapters below
# Chapter 1: Intro to Python
# Chapter 2: Intro to OOP
# Chapter 3: Game of Life

# for each of these chapters add 2 new pages
# Chapter #, Page #: TEXT ON THAT PAGE
# Chapter 1, Page 1: Welcome to Python! Time to create a Hello World application.
# Chapter 1, Page 2: Great job! Now lets start creating some new functions.
# Chapter 2, Page 3: Now that you know some python lets learn some OOP concepts.
# Chapter 2, Page 4: Classes, attributes, methods, objects, inheritance, etc.
# Chapter 3, Page 5: Lets create a game of life simulation!
# Chapter 3, Page 6: Here are all the rules your simulation needs to follow.


checkSolutions['example1'](tutorials)


'''
Example 2: INHERITANCE

This is probably the MOST important topic of OOP. It is how you categorize with OOP! Think of 
it this way, inheritance is something that is inherited or passed down. What does that have to 
do with programming? Inheritance helps us categorize and organize data by using general 
characteristics to describe similar objects. 

For example, a vehicle may be a pretty general category (just go with it). A vehicle probably has 
a certain number of tires, a certain number of doors, a manufacturer, etc. These are all general 
characteristics that can be associated with a vehicle (lets disregard boats, planes, etc). 

So a subcategory, that inherits all of these vehicle characteristics may be a semi-truck. The 
semi-truck may have specific attributes like trailer storage space, number of trailers, sponsoring 
company, etc. Whereas another category may be motorcycles, which can have completely different specific 
attributes. 

However, they both inherit the same attributes from the general vehicle category. People with more 
knowledge might be able to split these two subcategories (motorcycles and semi-trucks) into more 
sub-categories, but that is not necessary for this example. 

Let's build an example using Python classes to represent some categories!
'''


class GeneralCategory:
    # You can define a BASE CLASS (general category) the same way you have learned to define classes
    def __init__(self, g_a):
        # this general attribute will be inherited by ALL subclasses
        #    aka you can access and define this attribute for any class that inherits this base class
        self.general_attribute = g_a

    def general_method(self):
        # this method will also be inherited by each subclass. In the subclass you can do:
        #    1. Nothing - calling this method on a subclass will just execute the code in this definition of the method
        #    2. Overload - overloading a method basically means rewriting the method with the same name, this allows
        #                  you to have the method do something different for each subclass - which is VERY useful
        return self.general_attribute > 0


class SubCategory1(GeneralCategory):
    # To define a SUBCLASS (sub-category) you must add the parenthesis after the class name and write
    #   the name of the BASE CLASS in those parenthesis - this ensures that your SUBCLASS "inherits"
    #   the attributes and methods defined by your BASE CLASS
    def __init__(self, s_a):
        self.specific_attribute = s_a
        GeneralCategory.__init__(self, g_a=1)
        # make sure to call the constructor for your BASE CLASS in the constructor for your SUBCLASS
        #   you can do this my writing a similar statement to what you see above "GeneralCategory.__init__(g_a=True)"

    def specific_method(self):
        # this method is specific to this subclass and may only be executed on this subclass
        return self.specific_attribute * 2


class SubCategory2(GeneralCategory):
    def __init__(self, ic=False, it=False):
        self.is_cool = ic
        self.is_tired = it
        GeneralCategory.__init__(self, g_a=-1)

    def general_method(self):
        # let's overload this method!
        print("      METHOD OVERLOADED!")
        # if you see this ^ print when you run it, then we have successfully overloaded an inherited method
        return 27  # for absolutely no reason

    def r_u_n_m_e(self):
        if self.is_cool:
            print("         I'm cool")
        else:
            print("         :(")
        return self.is_cool

    def r_u_n_m_e_2(self):
        if self.is_tired:
            print("            _                 _                 \n" +
                  "        ___| | ___  ___ _ __ (_)_ __   __ _     \n" +
                  "       / __| |/ _ \\/ _ \\ \'_ \\| | \'_ \\ / _` | \n" +
                  "       \\__ \\ |  __/  __/ |_) | | | | | (_| |  \n" +
                  "       |___/_|\\___|\\___| .__/|_|_| |_|\\__, | \n" +
                  "                       |_|            |___/     ")

        return self.is_tired


g_o = GeneralCategory(g_a=5)
s_o_1 = SubCategory1(s_a=10)
s_o_2 = SubCategory2(ic=False, it=True)

print("------ EXAMPLE 2 TESTING ------")

# 1. See what happens when you try to access the attribute defined in GeneralCategory, from the SubCategory1 Object...
print("    1.   " + str(s_o_1.general_attribute))

# 2. See what happens when you run the general method on the SubCategory1 Object...
print("    2.   " + str(s_o_1.general_method()))

# 3. See what happens when you run the specific method on the SubCategory1 Object...
print("    3.   " + str(s_o_1.specific_method()))

# 4. Let's see what happens when we do the same things for the SubCategory2 Object...
print("    4.1. " + str(s_o_2.general_attribute))
print("    4.2. " + str(s_o_2.general_method()))
print("    4.3. " + str(s_o_2.r_u_n_m_e()))
print("    4.4. " + str(s_o_2.r_u_n_m_e_2()))


'''
Using the example above, create your own categorization of vehicle, motorcycle, and truck below! We have included 
some definitions and general outlines so that we can test your solutions!

Vehicle:
    - num_wheels - int
    - num_passengers - int
    - drive()
    
Truck:
    - bed_size - int
    - cab_size - int
    - tow()
    
MotorCycle:
    - handlebar_type - String
    - side_cab - Boolean
    - skid()
'''


class Vehicle:

    def __init__(self, num_wheels, num_passengers):
        pass

    def drive(self):
        raise NotImplementedError()


class Truck(Vehicle):
    # default the value of num_wheels to 4 and num_passengers to 2

    def __init__(self, bed_size, cab_size, num_wheels=4, num_passengers=2):
        pass

    def tow(self):
        # make tow return "Towing..."
        pass

    # overload the drive method here and make it return 23
    def drive(self):
        pass


# class MotorCycle
# make the values of num_wheels and num_passengers inputs to __init__()
# overload the drive method here and make it return 56
# make skid return 123456


# ------- TESTING --------
# Uncomment the lines of code below...
# Make sure that the arguments to your methods are the same as those used in the lines of code below...

# v = Vehicle(num_wheels=5, num_passengers=1)
# t = Truck(bed_size=20, cab_size=10)
# m = MotorCycle(num_wheels=3, num_passengers=3, handlebar_type="Cross", side_cab=True)
# checkSolutions["example2"](v, t, m)


