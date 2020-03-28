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
import datetime
from solutions.graphics import *
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

    NOTE: make sure you define the title attribute and the get_first_page method because those
          are both used in the gen_toc method of the Book class
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


'''
Example 3: Interfaces

For this example we will briefly explain interfaces and why they are useful. However, you should know 
that Python does not implement interfaces the same way that other OOP languages (e.g., Java) do. In 
Python interfaces are implemented like a Base class, whereas in Java, interfaces are completely separate 
from classes.

What is an interface? An interface in basically a set of functions that are implemented by many different 
classes, while keeping the naming the same. This provides a common way to access and process data from 
different classes. 

What does this mean? Basically, with an interface you can write code that does not depend on a specific 
class to be used. Instead your code can be general, covering any class that extends the interface. This 
is a way to generalize the type of variable you are working with. For example, if you want to run the 
same three functions on different animals, you can create an animal interface. Any class that extends 
the animal interface (e.g., monkey, horse, duck, etc.) will be treated the same way by your code. And 
you won't have to account for some of the differences in how each subclass (e.g., monkey, horse, etc.) 
is implemented, because the interface you are using to interact with the objects is the same for all of 
the objects.

How do I create an interface and extend it? To create an interface in Python you will create a Base class. This Base 
class will define the interface methods that must be implemented by all of the classes that wish to extend 
this interface. 

Let's do a basic example below, then you can create an animal interface based on the simple example!
'''


class Interface:
    '''
    NOTE: each of the methods in this interface have this "raise NotImplementedError()" in their function bodies
          This is to ensure that any class that tries to extend/implement this interface has implemented all of
          the functions, when a method from the interface is not implemented then the NotImplementedError will
          occur when you try to run your code.

    Side-note: Extend and implement may be used interchangeably in these tutorials, both of them basically mean that
    whatever class you have created will need to implement all the methods defined in the interface.
    '''
    def interface_method_1(self, arg1, arg2):
        raise NotImplementedError()

    def interface_method_2(self, arg1, arg2):
        raise NotImplementedError()


class TestClass1(Interface):
    def __init__(self, attr):
        self.attr = attr

    def interface_method_1(self, arg1, arg2):
        return arg2 > self.attr > arg1

    def interface_method_2(self, arg1, arg2):
        return self.attr + arg1*arg2


class TestClass2(Interface):
    def __init__(self, attr2):
        self.attr1 = 5
        self.attr2 = attr2

    def interface_method_1(self, arg1, arg2):
        return self.attr1 * (self.attr2 + arg1 + arg2)

    # Note that I did not implement interface_method_2 in this class - WHICH IS WRONG!


# Now lets see what happens when we run these methods
print("\n----- EXAMPLE 3 TESTING ------")
# this is a completely useless statement because the interface is an outline for methods that your
# class must implement, the interface does not actually implement any of these methods
i = Interface()

t = TestClass1(1)

c = TestClass2(1)

print(t.interface_method_1(0, 2))  # should print out True
print(t.interface_method_2(1, 2))  # should print out 3
print(c.interface_method_1(0, 2))  # should print out 15
# print(c.interface_method_2(1, 2))  # should cause an Error (uncomment the code here)

# Now you know what happens when you don't implement all the methods in an interface...
#   SO, don't do that :)


'''
Now its your turn to create an animal interface below! Use the following specifications for the 
interface and the subclasses that extend the interface...


AnimalInterface:
    - mate(animal2)
    - die()
    - eat(calories)
    
Monkey:
    - type: string ("Ape", "Gorilla", "Chimp")
    - weight: int
    - mate should return a new Monkey object with a weight of 5 and a type that is equivalent to 
      monkey1.type + monkey2.type (e.g., "ApeChimp", "Ape") if they are the same then you should 
      not combine them, if they are different then you should combine them
    - die should set type to "" and weight to 0 
    - eat should add calories/10 to the weight of the monkey

Horse:
    - color: string ("Red", "Blue", "Brown", "Green")
    - max_speed: int 
    - mate should return a new Horse object with a max_speed of 5 and a color that is the combination
      of its parents (e.g., "RedBlue", "Brown", "GreenBrown") do not include duplicates (e.g., "RedRed")
    - die should set color to "" and max_speed to the average (int) of the two parents' max speeds
    - eat should add calories/50 to max_speed
'''


class AnimalInterface:
    def mate(self, animal2):
        raise NotImplementedError()

    def die(self):
        pass

    def eat(self, calories):
        pass

# I have given you the outline for the AnimalInterface above, however you must write the Monkey and Horse classes on
# your own, Good Luck!


# Testing your solution... uncomment each line of code to run the test

# m1 = Monkey(type="Ape", weight=500)
# m2 = Monkey(type="Ape", weight=200)
# m3 = Monkey(type="Chimp", weight=20)

# h1 = Horse(color="Red", max_speed=20)
# h2 = Horse(color="Brown", max_speed=15)
# h3 = Horse(color="Brown", max_speed=10)

# checkSolutions["example3"](m1, m2, m3, h1, h2, h3)



'''
Example 4: Bring it all together (with a little polymorphism)

For this example we will review what we have learned for OOP so far and briefly discuss polymorphism, so that if
someone asks you what it is, you can give them a quick correct answer. Polymorphism probably won't be very useful 
for you right now, so we won't spend too much time on it.

Review of Object Oriented Programming (OOP):

    What is OOP?
        OOP is a programming paradigm in which data and code are 
        organized into classes and used in the form of objects.
        
    What is a class?
        A class is an outline/template of a object that includes 
        attributes (data) and methods (code).
        
    What is an object?
        An object is an instance of a class.
        
    What is an attribute?
        An attribute is a piece of data associated with an object. 
        This data is instantiated in the class's constructor method 
        (mostly).
        
    What is a method?
        A method is a block of code (function) that is defined in an 
        object's class and may be executed on any object of that class.
        
    How do I make an object?
        First you need to define the template (class) for that object. 
        Make sure you have defined a constructor method! Then you 
        can create an object by calling the class constructor like so...
        MyNewClass(attr1=1, attr2=2)
        
    How do I call/invoke methods on an object?
        Assume you have an object stored in the "var1" variable. And also 
        assume that you have defined a method called "m1(in1, in2)" in the 
        object's class. To call the method on the object, simply us a "."
        var1.m1(in1=2, in2=3)
        

Now, what is polymorphism?
    Basically it means having the same function signature (the name of your 
    function), but having different implementations of that function, potentially 
    for different types (e.g., different classes, int, String, char, byte, etc.)
    
What are the uses of polymorphism?
    If you are really interested then visit this link: https://stackify.com/oop-concept-polymorphism/
    That article has a pretty good explanation of polymorphism, using Java for examples.
    
    You can think of polymorphism in the same way we defined an interface, with fewer restrictions.
    Writing polymorphic code for two classes (e.g., implementing a method with the same signature (name) 
    for both classes) does not require the use of an interface. You could simply write a method with 
    the same name in each class and that would be polymorphic. However, if you are trying to generalize 
    the type for these two classes, then you SHOULD use an interface or super/abstract class. This will 
    force you to implement all the necessary methods, whereas, just trying to remember to write the correct 
    methods is not very effective and is error prone. 
    
    Another interesting use of polymorphism is defining the same method multiple times for a class. 
    This is most useful in Java because you need to define the type of data that the method will 
    return. In Python, you don't need to define the type of output data, and you can also define 
    optional input arguments quite easily. Python also does NOT allow you to define a method twice 
    for a class, so this use case isn't very useful in Python. 
    
    Overall, you can probably just stick to interfaces and super classes and you should be all set.
    

For this example you should pick an interesting application of OOP and write a few classes for it. 
By that I mean, pick a topic like a family tree and create the appropriate classes to define a family 
tree. I will include an example definition of a family tree below, which will be used in Project 4.   

Feel free to edit the code below :) or write your own new code! Just play around with it
'''


class Person:
    def __init__(self, first_name, middle_name, last_name, birth_year, gender, mother=None, father=None):
        """
        Person: a person with a linked mother and father
        :param first_name: the name of this Person
        :param middle_name: the middle name of this person
        :param last_name: the last name of this person
        :param birth_year: the year this Person was born
        :param gender: the gender of this Person (0 = MALE, 1 = FEMALE)
        :param mother: the mother of this Person (must also be a Person)
        :param father: the father of this Person (must also be a Person)
        """

        self.fname = first_name
        self.mname = middle_name
        self.lname = last_name
        self.dob = birth_year
        self.dod = None
        self.gender = gender

        if isinstance(mother, Person):
            self.mother = mother
        else:
            self.mother = None

        if isinstance(father, Person):
            self.father = father
        else:
            self.father = None

    def die(self, year=None):
        if not year:
            year = datetime.datetime.now().year
        self.dod = year

    def generate_family_tree(self ):
        if self.mother is not None:
            self.mother.generate_family_tree()
        if self.father is not None:
            self.father.generate_family_tree()

        self.generate_tag()

    def generate_tag(self):
        if self.mother is not None or self.father is not None:
            print("             |            ")
            print("             |            ")
        print(self.fname + " " + self.lname)

    def add_mom(self, person):
        if isinstance(person, Person):
            self.mother = person

    def add_dad(self, person):
        if isinstance(person, Person):
            self.father = person


me = Person("Brian", None, "Finnegan", 1995, 0)
wifey = Person("Angela", None, "Hart", 1995, 1)

kid1 = Person("Jamal", None, "Finnegan", 2015, 0, father=me, mother=wifey)

kid1wife = Person("Jamie", None, "Norvig", 2017, 1)
vikki = Person("Vikki", None, "Pearson", 1990, 1)
jordan = Person("Jordan", None, "Norvig", 1992, 0)

kid1wife.add_dad(jordan)
kid1wife.add_mom(vikki)

gkid = Person("Toni", None, "Finnegan", 2030, 1, mother=kid1wife, father=kid1)


gkid.generate_family_tree()
