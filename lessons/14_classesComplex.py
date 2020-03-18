"""
Practice Group 14: Classes
Created: 3/17/2020

In this tutorial we will cover more complex examples of object
oriented programming. We will also delve into some other OOP
topics including inheritance, ASDF, and ASDF.

Learning Objectives:
    1. Create classes that reference each other


"""

from solutions.CheckSolutions import CheckSolutions
checkSolutions = CheckSolutions().ClassesComplexSolutions

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