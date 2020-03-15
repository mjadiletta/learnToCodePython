"""
Practice Group 0: Coding Introduction
Created: 3/14/2020

In this assignment we will learn to run a program in pyCharm and how to debug.

Learning Outcomes:
1) Run this program in python, and any other exercise in this program
2) Use print statements
3) How to set variables and make strings
4) How to use pyCharm in general!

Most examples are completed for you.
There are no correct or incorrect answers in this section.
Just learn how to print to the console and get comfortable with what is going on in the pyCharm environment.

Note:
    Python is a syntax langauge where "white space" matters
    white space is stuff like new lines and tabs.
    You must use white space correctly to make the code compile.
"""

'''
Example 1:
    print "hello world!" to the console
'''
print("hello world!")
# now you might be asking yourself how to run this program...
# In pyCharm we have a bunch of options
# 1. In the main select bar choose: Run -> Run and select 0_introductionToPython.py
#       If an error occurs that says "no python interpreter",
#       it is because you did not set up your environment correctly.
#       Reread the README and try again or text me :)
#    If you successfully ran this program, then a terminal window will pop up and display "hello world!"
# 2. If your terminal window is already open, there is a green triangle that runs the program titled by the window menu.
# 3. If your terminal window is not open, you can open it by going to the bottom left of the screen where it says,
#       "Python Console and Terminal" Select the terminal, not the console.

'''
Example 2: 
    move your terminal window around!
    Step 1: In your terminal, along the top bar there is a gear and a minus sign.
            The minus sign minimizes the terminal. 
    Step 2: Click the gear and select "Move to"
            Try out different spots on your pyCharm window and pick your favorite
            My favorite is "Right Top" because I can see the most in my terminal vertically. 
            Most people just like "Bottom Left". Pick your favorite.
'''

'''
Example 3: 
    Understanding what's going on in the left window
    The window on the left is the window that displays your project directory. 
    It has all the files you need in this lecture series.
    There are 3 main directories: data, lessons, and solutions. 
        The data has a bunch of files that are not viewable without properly loading them
        The lessons are all of the lessons you will be completing. To open a lesson, just double click on it
            and it will appear in the main window. 
            To close the window, press the x in the top right of the program window. 
        The solutions are mostly my code that I use to check your solutions. It has all the solutions coded into
            the solution program, however, extrapolating those solutions to use as your own / "cheating" is difficult.
            If you really need to "cheat" then go for it, but be warned, it won't make sense lol. 
            That said, there are folders inside solution that show what certain graphs will look like in certain lessons
            for example, in the 7_matplotlibIntroductionSolutionsImages directory, example4 shows the solution to the 
            graph you are asked to create. I cannot create a CheckSolutions guide that checks every little thing so
            you will need to check your own solutions to some degree. But in general, my check functions can check
            all your solutions to prove you are succeeding.  
    Lets say you press the minus on the left window by accident. To bring back the left column window, click the 
    vertical words that say "1:Project" and the window will reappear. 
    
    To create a new python file (which you don't need to do for this series) right click on a folder or main project,
    then navigate to New -> Python File. Give it a name and it will appear in the directory you selected.  
'''

'''
Example 4: 
    Delete the "exit()" command so that the program continues
    then store an integer to variable a and print the variable
'''
#exit()
a = None
print(a)

'''
Example 5:
    Create a string and print the string.
'''
print_this_string = "I love python"
print(print_this_string)


'''
Example 6:
    Create a string with a combined string and integer
'''
a = 10
print_this_string = "I love python"
print(print_this_string + str(a))
# note that python cannot print a string + int. The int must be converted to a string before it can be printed
# prove this by running: "print(print_this_string + a)" and get the error.

'''
Example 7:
    use special characters:
    \n and \t
'''
string = "This is a special string \nThe \\n character is the new line character in python\n" \
         "\tThe \\t character is the tab character"
print(string)


'''
Example 8: 
    Notice there are really only 2 types of variable we deal with in python: 
    numbers and strings.
    Numbers can be: integers or floating point numbers
    Strings are strings
    
    Numbers can be converted (cast) to strings using the str() function so they can be printed
    Strings cannot be converted to numbers tho :(  
'''
a = 10.02
print(str(a))

# Try this and see why it breaks :(
#print(int("test"))

'''
Example 9: 
    Notice the two types of line comments that I've been using:
    block line comments: '''  '''
    single line comment: # this is a single line comment
'''

'''
Continue trying various print statements!

Print statements are critical to debugging. I will not show you how to use print statements beyond 
this because pretty much anything can be printed. 
If you aren't sure what something is, just print it and find out!

Helpful Hints going forward: 
1. Use the print statement everywhere. If you can't print something, Google how to do it
2. Use the exit() statement. Sometimes these lectures get pretty long and using exit() stops the program 
    wherever you are expecting/telling it to stop
3. If you get lost with where a program is going, start from the very top of the code and 
    follow the line of logic the computer is using to run your program.
4. Never give up! The solution is right in front of you! Swearing at your laptop is totally normal
5. Text me if you are really stuck

Good Luck!
'''
