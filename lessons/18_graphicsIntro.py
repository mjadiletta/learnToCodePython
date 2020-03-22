"""
Practice Group 18: Graphics Introduction
Created: 3/21/2020

In this tutorial we will cover basic graphics in python.
We will use a python file "graphics.py" to draw points,lines, squares, etc.
This graphics file uses tkinter. This comes with default python 3.

The library provides the following graphical objects:
    * Point(x, y)
    * Line(Point(x, y), Point(x, y))
        - Line.setArrow(option) : options: "first", "last", "both", "none"
    * Circle(Point(x, y), radius)
    * Oval(Point(x, y), Point(x, y)) - corners of bounding box
    * Rectangle(Point(x, y), Point(x, y))
    * Polygon(vertices); vertices = [Point(x, y), Point(x, y), ... , Point(x, y)]

Graphics Operators:
    * obj.setFill( color ) - fills an object with a color
    * obj.setOutline( color ) - outlines an object with a color
    * obj.setWidth( width ) - sets an objects width
    * obj.setHeight( height ) - sets an objects height
    * obj.draw( window ) - draws an object on a window
    * obj.undraw() - removes an object from a window
    * obj.move( dx, dy ) - moves an object by one step of ( dx, dy )

Text Operators:
    * Text(Point(x, y), 'text string')
        - Text.setText( "text" )
        - Text.getText() - returns what's in a text
        - Text.setFace( face ) - face: "helvetica", "arial", "courier", "times roman"
        - setSize( size ) - font size: 5 <= size <= 36
        - setStyle( style ) - styles: "bold", "normal", "italic", "bold italic"
        - setColor( color ) - sets the color of the text

The library also provides the following user interfacing functions:
    * window.getMouse() - returns (x, y) of mouse
    * window.checkMouse() - returns Point of last mouse click, or None if no click
    * window.getKey() - waits for user to press a key
    * window.checkKey() - returns the last key press, or None if no key pressed

Other Useful Functions:
    * setBackground( color )
    * setCoords( x1, y1, x2, y2 ) - coordinates of window to run from (x1, y1) to (x2, y2)
    * flush() - update drawing to the window
    * getHeight() - returns height of window
    * getWidth() - returns width of window

Colors we can use: http://www.science.smith.edu/dftwiki/index.php/Tk_Color_Names

Learning Objectives:
    1. Draw objects on a canvas
    2. Make objects move on a canvas
    3. Connect user inputs to actions of canvas objects

use this website for help drawing objects: http://anh.cs.luc.edu/handsonPythonTutorial/graphics.html

Example 1 is completed as a template.
For each of the following examples, replace blank lines
with the correct functionality. If completed correctly, the checkSolutions
will print "Correct Solution" to the terminal.
"""

import numpy as np
from solutions.graphics import *
from solutions.CheckSolutions import CheckSolutions
checkSolutions = CheckSolutions().graphicsIntroSolutions

'''
Example 1: 
    In this example we will draw 3 items on a canvas
    1. Draw a circle at point x=250 y=250 with radius 100
        - set the fill of the circle to "lightblue"
    2. Draw a rectangle around the circle so there is no overlap
        - set the fill of the rectangle to "maroon"
    3. Draw a diagonal line at y = -x across both the entire circle and rectangle
        - set the outline of the line to "medium sea green"
        - set the width to 3
    
    return win.items
'''
def ex1():
    win = GraphWin("My Circle", 500, 500)  # name of window, width, height
    c = Circle(Point(250, 250), 100)
    c.setFill("lightblue")
    r = Rectangle(Point(150, 150), Point(350, 350))
    r.setFill("maroon")
    l = Line(Point(0, 0), Point(500, 500))
    l.setOutline("medium sea green")
    l.setWidth(3)
    r.draw(win)
    c.draw(win)
    l.draw(win)

    # Close window if the return/enter key is pressed
    while True:
        if win.checkKey() == "Return":
            win.close()
            break

    return win.items

checkSolutions['example1'](ex1)



'''
Example 2: 
    In this example we will draw a 1 lane track with an infield on the canvas
    
    Object 1. Draw an oval at points x=100 y=100 to x=468 y=464
        - set the fill of the oval to "IndianRed4"
    Object 2. Draw an oval at points x=436 y=100 to x=804 y=464
        - set the fill of the oval to "IndianRed4"
    Object 3. Draw a rectangle at points x=284 y=100 to x=620 y=464
        - set the fill and outline of the rectangle to "IndianRed4"
    Object 4. Draw a line at points x=284 y=100 to x=620 y=100
    Object 5. Draw a line at points x=284 y=464 to x=620 y=464
    
    Object 6. Oval x=138 y=138 to x=430 y=426
        - set fill "sea green" Outline "white"
    Object 7. Oval x=474 y=138 to x=766 y=426
        - set fill "sea green" Outline "white"
    Object 8. Rectangle x=284 y=138 to x=620 y=426
        - set fill "sea green" Outline "IndianRed4"
    Object 9. Line at x=284 y=138 to x=620 y=138
        - set fill "white"
    Object 10. Line at x=284 y=426 to x=620 y=426
        - set fill "white"

    Object 11. Line at x=284 y=100 to x=284 y=138
        -set outline "black" width = 3

    Object 12. Textbox centered x = 284 y=80 saying "Finish Line"
    
    Object 13. Rectangle x=620 y=100 to x=805 y=138
    Object 14. Line x=620 y=100 to x=620 y=100
        - set fill "IndianRed4"
    Object 15. Line x=620 y=138 to x=732 y=138
        - set fill "white"
    
    You must draw the shapes in this order to get credit 
    - check answers needs to see this order of shapes
    
    return win.items, win
'''
def ex2(RequestClose=True):
    win = GraphWin("My Track", 904, 564)  # name of window, width, height




    # Close window if the return/enter key is pressed
    while RequestClose:
        if win.checkKey() == "Return":
            win.close()
            break

    return win.items, win

# uncomment once you are working on example2
#checkSolutions['example2'](ex2)



'''
Example 3: 
    Notice that in the last example, we returned two values, win.items and win. 
    win.items was only for check solution, but we also have the window. To get
    the window without closing it we need to set the function parameter: 
        RequestClose=False for ex2 so that the function never requests user input. 
        
    call ex2 like this: items, win = ex2(RequestClose=False)
        - giving you the window and items. 

    For this example, we are going to make a runner, sprint a 100m dash. 
        
    Use these steps to make a person sprint a 100m dash
    1. Draw a circle at coordinates x=824 y=119 with radius 16
        - set fill "NavajoWhite2" or "tan4" (your choice)
    
    2. Make the player move using a while loop:
        while the player's x < finish line (284),: move player in x direction
        
    Hint: use player.getCenter().getX() for x and player.getCenter().getY() for y
        use player.move(dx, dy) for moving the player each iteration - use a small dx < .2
        
    Optional: Make a second player accelerate while running the 100
        To do this: 
            1. draw another circle with the opposite color you originally chose
            2. In the same loop as the other player:
                - have a variable counting the number of loops
                - calculate player2's speed as max_speed * (loops/(loops+100))
            3. Change the condition on the while loop for player 2, because player 2 
                will be the last item drawn and we want player2 to be the person crossing the finish line
        
'''
def ex3(RequestClose=True):
    items, win = ex2(RequestClose=False)

    player = Circle(Point(1, 1), 1)
    speed = None

    while None:
        player.move(speed, 0)




    # Close window if the return/enter key is pressed
    while RequestClose:
        if win.checkKey() == "Return":
            win.close()
            break

    return items

#checkSolutions['example3'](ex3)



'''
Example 4:
    For this example, we are going to make a runner, sprint a 200m dash. 

    Use these steps to make the athlete sprint a 200m dash:
    1. Draw a circle at coordinates x=620 y=445 with radius 16
        - set fill "NavajoWhite2" or "tan4" (your choice)

    2. Make the player move along the turn using a while loop:
        while the player's y < the center value of the straightaway (119), move the player along curve
        
    3. Make the player move along the straightaway using a while loop:
        while the player's x < finish line, move player in x direction

    The hard part here isn't setting up the while loops or moving the player on the straightaway.
    The hard part is making the player move on a turn - this requires some calculus :) 
        - If you don't know/remember calculus, don't worry, it's mostly explained as we go
        
    As you noticed, when you created the track, you used two ovals for the turns.
    Ovals are elipses which follow the equation x^2/a^2 + y^2/b^2 = 1
        where a and b are the height and width of the elipse. 
        
    To make our guy travel on the elipse curve, we are going to need to get the slope
    of the elipse curve at the players (x,y) location. To do this we take the derivative
    of the above equation with respect to x. 
    
    Start example 4 with part 4a, solving for the derivative of y. 
'''

'''
Example 4a: derivatve of an elipse with respect to x for our 200m problem

The range for x: 0<=x<=a
The range for y: -b<=y<=b

The formula for an elipse as previously stated: x^2/a^2 + y^2/b^2 = 1
Open up desmos and plug this in with a=165, b=163 https://www.desmos.com/calculator

Solving for y: y = sqrt( b^2 - (b^2/a^2) * x^2 )

Taking the derivative with respect to x: 
    y' = 1/2 (b^2 - (b^2/a^2) * x^2)^(-1/2) * (2*(b^2/a^2) * x)

Notice that if x = a, we get 1/2*(0)^(-1/2) * 2b^2 -> this is a division by zero... major problems
    In this formula we must check first if x < 165 to be able to apply the derivative
    If x=165, y=0 => y' = np.inf

return y' from this function
'''
def delta_y(x, a, b):
    return -1

#checkSolutions['example4dy'](delta_y)



'''
Example 4b: Normalization of the derivative

The gradient we just calculated works only if we aren't regulating "speed" as in, 
how fast the guy is moving at different (x, y) points. However, we do care 
so we really want our delta_y to be normalized (meaning we have a unit vector in direction dx, dy).

The gradient we calculated is interpreted as: 
    k steps in the y direction for one step in the x direction
We don't want this because we want sqrt(dy^2 + dx^2) = 1 so that all steps are of uniform size.  

Write an equation to return the normalized vectors dx, dy
    dx = 1 / sqrt(unnormalized_dy^2 + 1)
    dy = unnormalized_dy / sqrt(unnormalized_dy^2 + 1)

Now before you call it a day, we have one more issue we need to address with this function:
    Notice two things, first the unnormalized_dy we calculated is always negative 
        for the region we are in. If you don't know why, take a look at the formula again. 
        
    For the 200m problem, our x is always positive. 
        When y < 0 we want the slope to be positive " o/ " <-- an attempt at +slope against a circle
        When y > 0 we want the slope to be negative " o\ " <-- an attempt at -slope against a circle
        
        Since y is always increasing: we need to switch the direction of dx when y goes from
        negative to positive. In the previous problem we addressed when y == 0, this addresses
        how x changes as y switches from negative to positive.  
        
        if y < 0:
            dx = 1 / sqrt(unnormalized_dy^2 + 1)
            dy = unnormalized_dy / sqrt(unnormalized_dy^2 + 1)
        else:
            dx = -1 / sqrt(unnormalized_dy^2 + 1)
            dy = unnormalized_dy / sqrt(unnormalized_dy^2 + 1)
        
The last iss issue we will address occurs around y = 0. This happens because 
the unnormalized_dy == None or inf since our computer cannot calculate ~infinite slopes.
Therefore we need to manually set how our dx, dy should look if unnormalized_dy == None or inf
    
    if unnormalized_dy == None or inf and y < 0:
        dx = .001
        dy = -.999 (notice that dy is negative because on canvas, 
                    the top of the screen y = 0 and bottom is y = 500)
    if unnormalized_dy == None or inf and y > 0:
        dx = -.001
        dy = -.999 (notice that dy is negative because on canvas, 
                    the top of the screen y = 0 and bottom is y = 500)    

return dx, dy - for every situation looked at above. 

Hint: there are 4 cases: 
    if unnormalized_dy == None or unnormalized_dy == np.inf:
        if y > 0:
        if y < 0:
    else:
        if y > 0:
        if y < 0:
'''
def norm_grad(unnormalized_dy, y):
    return -1, -1

#checkSolutions['example4normdy'](norm_grad, delta_y)



'''
Example 4:
    Now for the fun part.
    Use these steps to make the athlete sprint a 200m dash:
    1. Draw a circle at coordinates x=620 y=445 with radius 16
        - set fill "NavajoWhite2" or "tan4" (your choice)

    2. Make the player move along the turn using a while loop:
        while the player's y < the center value of the straightaway (119), move the player along curve
        
        center = (620, 282) # this is the center of the elipse.
            
        algorithm to move: 
            player_x = x_pos - center[0]  # to mathematically center the origin at 0
            player_y = y_pos - center[1])  # the canvas is inverted so multiply by -1
            unnormalized_dy = delta_y(x, a, b)
            dx, dy = norm_grad(unnormalized_dy, y)
            player.move(speed*dx, speed*dy) -> speed <.1
        
    3. Make the player move along the straightaway using a while loop:
        while the player's x < finish line, move player in x direction
            - same as example 3
'''
def ex4(RequestClose=True):
    items, win = ex2(RequestClose=False)
    center = (620, 282)
    a = 165
    b = 163



    player = Circle(Point(1, 1), 1)
    speed = None

    while None:
        x = None
        y = None
        dy = delta_y(x, a, b)
        dx, dy = norm_grad(dy, y)
        player.move(speed * dx, speed * dy)

    while None:
        None



    # Close window if the return/enter key is pressed
    while RequestClose:
        if win.checkKey() == "Return":
            win.close()
            break

    return items

#checkSolutions['example4'](ex4)