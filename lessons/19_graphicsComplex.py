"""
Practice Group 19: Graphics Complex
Created: 3/22/2020

In the previous lecture we designed a track and then had a player run a 100m dash and 200m dash.
In this tutorial we will take a deeper look into graphics in python.

Specifically we will use our graphics tools to make a Tetris game, but with only one block.
Our user input will be the keyboard arrows.

We will use the same python file "graphics.py" to draw points, lines, squares, etc.
This graphics file uses tkinter. This comes with default python 3.

The library provides the following graphical objects:
    * obj = Point(x, y)
    * obj = Line(Point(x, y), Point(x, y))
        - Line.setArrow(option) : options: "first", "last", "both", "none"
    * obj = Circle(Point(x, y), radius)
    * obj = Oval(Point(x, y), Point(x, y)) - corners of bounding box
    * obj = Rectangle(Point(x, y), Point(x, y))
    * obj = Polygon(vertices); vertices = [Point(x, y), Point(x, y), ... , Point(x, y)]

Graphics Operators:
    * obj.setFill( color ) - fills an object with a color
    * obj.setOutline( color ) - outlines an object with a color
    * obj.setWidth( width ) - sets an objects width
    * obj.setHeight( height ) - sets an objects height
    * obj.draw( window ) - draws an object on a window
    * obj.undraw() - removes an object from a window
    * obj.move( dx, dy ) - moves an object by one step of ( dx, dy )

Text Operators:
    * txt = Text(Point(x, y), 'text string')
        - txt.setText( "text" )
        - txt.getText() - returns what's in a text
        - txt.setFace( face ) - face: "helvetica", "arial", "courier", "times roman"
        - txt.setSize( size ) - font size: 5 <= size <= 36
        - txt.setStyle( style ) - styles: "bold", "normal", "italic", "bold italic"
        - txt.setColor( color ) - sets the color of the text

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
"""

from solutions.graphics import *
from solutions.CheckSolutions import CheckSolutions
checkSolutions = CheckSolutions().graphicsComplexSolutions


'''
Example 1 and 2:
    Open each comment block one at a time and solve each problem sequentially
    The check solutions are below, do not edit those...
    Uncomment the check solutions as you go, and after solving the problem, comment it again. 
    
    You may want to copy the commented instructions into a separate text file 
        to read them better while you're coding
'''
'''
Example 1: 
    To start Tetris, lets make a single TetrisBlock class.
    If you forget what a class is look at lecture 13-16.
     
    We can use this block both for game purposes and 
    graphic design purposes later. 
    
    Example 1:
        This class stores 4 attributes:
            1. win: the window we can draw on
            1. x_topLeft: the x position for the top left of the block
            2. y_topLeft: the y position for the top left of the block
            3. blockColor: the color for the block
            
        Design a single Tetris block with dimensions: 
            Object 1.   Square with initial position self.x=x_topLeft self.y=y_topLeft
                            - Width = 45 pixels
                            - Set fill to blockColor
            
            Object 2.   An internal square that has a 7 pixel buffer between the outer block and itself
                            - Set the internal square fill color to blockColor 
            Object 3-6. 4 black lines extending from each internal corner to the closest external corner
            
        
        Note: we need to draw this on the screen in the init section.
        
        To visually check your solution look in "solutions/19_graphicsComplexSolutionImages/TetrisBlock.png"
'''
'''
    Example 2: 
        For example 2 we will write 2 methods
        1. moveBlock(dx, dy) 
            This will move each element of this object (dx, dy). 
            be sure to update self.x and self.y
        2. removeBlock()
            This method will remove every element of the TetrisBlock from the screen. 
                Use graphics method: obj.undraw()
                
        The check function for this example will create a TetrisBlock 
            and move it diagonally across the screen, then remove the block. 
            The check function will return true if the block has moved,
            but it does not check if the block was removed. You must check that yourself.  
'''
class TetrisBlock():
    def __init__(self, win, x_topLeft, y_topLeft, blockColor):
        self.win = win
        self.x = 0
        self.y = 0
        self.blockColor = None

        # Example -> It will say Object 1 is wrong unless you fix self.x and self.y
        self.block = Rectangle(Point(self.x, self.y), Point(self.x+45, self.y+45))
        self.block.setFill(blockColor)
        self.block.draw(win)


    def moveBlock(self, dx, dy):
        self.x += 0
        self.y += 0
        self.block.move(dx, dy)
        #...

    def removeBlock(self):
        self.block.undraw()
        #...

'''
    Test TetrisBlock()
    Do not edit: just use it to test your class
'''
def ex1(x, y, color):
    win = GraphWin("Tetris", 550, 700)
    tb = TetrisBlock(win, x, y, color)
    return win.items, win

checkSolutions['example1'](ex1, 200, 200, "lightblue")


'''
    Test TetrisBlock()
    Do not edit: just use it to test your class
'''
def ex2(x, y, color):
    win = GraphWin("Tetris", 550, 700)
    tb = TetrisBlock(win, x, y, color)

    for i in range(2000):
        tb.moveBlock(.1, .1)
    tb.removeBlock()
    return win.items, tb, win
#checkSolutions['example2'](ex2, 200, 200, "lightblue")



'''
Example 3 4 5 and 6:
    Open each comment block one at a time and solve each problem sequentially
    The check solutions are below, do not edit those...
    Uncomment the check solutions as you go, and after solving the problem, comment it again. 
    
    You may want to copy the commented instructions into a separate text file 
        to read them better while you're coding
'''
'''
    Example 3: Construct the Game Board
        Lets make another class called TetrisGame
            This class takes one attribute, the window
        
        This class is initialized by making the screen:
        Object 1. Create the game console at x=47.5 y=47.5, width=755 height=705
                    - set fill "black"
                    - outline "purple4" width=3 
                    
        Object Set 1: Use a for loop to draw "grey" TetrisBlocks over the game console 
                    - draw a TetrisBlock every 50 pixels.  
                    - 15 wide, 14 high
                    for i in range(15):
                        for j in range(14):
                            ~TetrisBlock(i*50+52.5, j*50+52.5)
                            
        Object 2. Create the game screen at x=97.5 y=97.5, width=455 height=605
                    - set fill to "lightblue"
                    - set outline "gray13" width=6
                    
        Object Set 2: Use a for loop to draw "pale turquoise" lines across the screen 
                    - at intervals of 50 both vertically and horizontally x->(100-700) and y->(100-550) 
                    - total of 8 vertical lines and 11 horizontal lines            
                    
        Object 3. Rectangle at x=575, y=125 width=200 height=50
                    - set fill to "lightblue"
                    - set outline to "grey13" width=2
        Object 4. Text at x=677.5 y=150 "Tetris Game!"
                    - set text size to 18 (setSize())
                    - set font to "courier" (setFace())
                    - set style to "bold" (setStyle())
        Object 5. Rectangle at x=575, y=225 width=135 height=40
                    - set fill to "lightblue"
                    - set outline to "grey13" width=2
        Object 6. Text at x=630 y=245 "Tetris Game!"
                    - set text size to 14 (setSize())
                    - set font to "courier" (setFace())
                    - set style to "bold" (setStyle()) 
        Check your game configuration with the image in the solutions folder
'''
'''
    Example 4: Setup Adding and Moving a Block
        In this example we will write code to track the state of the game. 
        That is, where TetrisBlocks are on the board.
        
        Our gameScreen size is 600x450 and a Tetris block is 50x50
            - this means we can stack 12 blocks high and 9 blocks wide 
        
        Do the following:        
        1. Add an attribute to TetrisGame() called "gameState"
            - Make gameState equal a numpy array size 12x9
            - use np.empty((sizeRows, sizeColumns), dtype=object)
        2. Add an atrribute to TetrisGame() called "currentBlock"
            - This will track the current TetrisBlock we are moving
            - initialize to None
        3. Add an attribute to TetrisGame() called "currentBlockRow"
            - This will track the current block row -> set to None
        4. Add an attribute to TetrisGame() called "currentBlockColumn"
            - This will track the current block row -> set to None
            
        Next we need a method to add blocks to the screen
            define newBlock() that creates a TetrisBlock:
                - Draw the TetrisBlock at position x=302.5 y=102.5 color="orange"
                - Store the TetrisBlock in the 4th horizontal position on the 1st row of gameState
                    * gameState[0][4] = TetrisBlock()
                - Set attribute currentBlock = gameState[0][4]
                - Set attributes currentBlockRow and currentBlockColumn to 0 and 4 respectively
'''
'''
    Example 5: Move Block using arrow keys (with constraints)
        For this example we are going to add an "Event Listener" which basically is a loop 
        that waits for user input. 
        
        1. Add a new method called UserMovesBlock() 
            - This method allows a user to move the block in directions: left, right and down 
                using the arrow keys
            - To do this:
                while True:
                    self.addBlock() # add a new block to the Tetris board
                    
                    while self.CheckMoveDown() == True: (see next for CheckMoveDown())
                        if win.checkKey() == "Left":
                            if self.checkMoveLeft(): (see next for CheckMoveLeft()
                                self.currentBlock.moveBlock(-50, 0) 
                                self.gameState[self.currentBlockRow][self.currentBlockColumn] = 0
                                self.currentBlockColumn -= 1
                                self.gameState[self.currentBlockRow][self.currentBlockColumn] = 1
                        repeat for "Right" and "Down"
                    
        
        2. Add 3 new methods called CheckMoveLeft(), CheckMoveRight(), CheckMoveDown()  
            - returns True if the block can move left and False if it can't
            - if we are in column 0 by self.currentBlockColumn == 0:
                * if we are in column 0, then we can't move left so return False
            - else if there is a block to our left
                * use self.gameState[self.currentBlockRow][self.currentBlockColumn - 1] == 1
                    if there is a block, return false
            - else
                return True because there is nothing to our left

'''
'''
    Example 6: Add a Termination Check and Row Removal and Score
    
    Currently, we can just add blocks and they will stack up and never stop stacking. 
    In this example we will code 3 methods
    1. CheckTermination()
        - check if a there are any blocks in gameState[0] -> the first row of the tetris board
            if gameState[0][1] != None -> then there's a TetrisBlock 
        - if this is true, terminate the game: game over
        - use this function in the outer while loop that is currently set to True
        - Outside the while loop put a print statement: "Game Over! Press Enter to Exit"
    2. CheckRowFull()
        - after a block is placed but before a new block is added, 
            check the row it was placed in to see if it became full
            * if all values in the row are 1:
                return True 
    3. RemoveRow()
        - if CheckRowFull():
            RemoveRow()
        - remove the row of tetris blocks that the currentBlock was placed in (currentBlockRow)
            * call gameState[row][col].removeBlock()
            * then set gameState[row][col] = None
        - Then shift all blocks on the screen down one.
            * Remember to move the block both on the screen and in the gameState
            * Note that since we are only using single tetris blocks, we can only ever remove the last row 
    4. UpdateScore(num_points)
        - Before writing this method we need to add another attribute in init that displays a score of 0
            * Add a text element called self.scoreVal at position x=675 y=245, courier, bold, size 14
            * Add an attribute to TetrisGame: self.scoreData = 0
        - In Update Score: 
            * add num_points to self.scoreData
            * call self.scoreVal.setText( text ) : where text is the stringified self.scoreData
        - Then we need to call UpdateScore in a few spots
            * Every time a block moves down, add 1 point to the score
                $ This occurs both when a key press occurs and the block moves down, 
                $ and when a row is removed and indivdual blocks are moved down
            * Every time a row is removed, add 101 points
    
    If you successfully complete all these examples, then you finished the Tetris Example! Congrats!!
    This project was a lot of work, but you learned a lot about how to use graphics, classes, and loops. 
'''
class TetrisGame:
    def __init__(self, win):
        self.win = win

        # Object 1 - Example
        self.gameBoarder = Rectangle(Point(47.5, 47.5), Point(802.5, 752.5))
        self.gameBoarder.setFill("black")
        self.gameBoarder.setOutline("dark slate blue")
        self.gameBoarder.setWidth(3)
        self.gameBoarder.draw(win)

        # Object Set 1 -> use 2 for loops with a Tetrus Block(win, x, y, "grey")

        # Object 2 - It probably says object 2 is correct
        #   It's not if you haven't coded anything for set 2 below... sorry to hard to fix...

        # Object Set 2 example:
        for i in range(8):
            vl = Line(Point(i*50 + 150, 100), Point(i*50 + 150, 700))
            vl.setFill("pale turquoise")
            vl.draw(win)

        # Do oppositely orientated lines here

        # Object 3

        # Object 4

        # Object 5

        # Object 6

        ###################### Example 6 Text Object ###################################
        self.scoreVal = Text(Point(0, 0), "")
        #self.scoreVal.setSize()
        #self.scoreVal.setStyle()
        #self.scoreVal.setFace()
        #self.scoreVal.draw()
        self.scoreData = None

        ###################### Example 4 ###################################
        self.gameState = None
        self.currentBlock = None
        self.currentBlockRow = None
        self.currentBlockColumn = None

    def newBlock(self):
        self.gameState[0][4] = None
        self.currentBlock = None
        self.currentBlockRow = None
        self.currentBlockColumn = None

    def UserMoveBlock(self):
        while True:
            self.newBlock()
            while True:
                key = self.win.getKey()
                if key == "Left":
                    if self.CheckMoveLeft():
                        self.currentBlock.moveBlock(-50, 0)
                        self.gameState[self.currentBlockRow][self.currentBlockColumn] = None
                        self.currentBlockColumn -= 1
                        self.gameState[self.currentBlockRow][self.currentBlockColumn] = self.currentBlock
                # Add Right and Down

    # Example for you to follow for Right and Down
    def CheckMoveLeft(self):
        if self.currentBlockColumn == 0:
            return False
        elif self.gameState[self.currentBlockRow][self.currentBlockColumn - 1] != None:
            return False
        else:
            return True

    def CheckMoveRight(self):
        None

    def CheckMoveDown(self):
        None

    def CheckTermination(self):
        None

    def CheckRowFull(self):
        None

    def RemoveRow(self):
        None

    def UpdateScore(self, num_points):
        self.scoreData += None
        self.scoreVal.setText(None)



'''
    Test TetrisGame()
    Do not edit: just use it to test your class
'''
def ex3():
    win = GraphWin("Tetris", 850, 800)
    game = TetrisGame(win)
    return win.items, game
#checkSolutions['example3'](ex3)


'''
    Test TetrisGame()
    Do not edit: just use it to test your class
'''
def ex4():
    win = GraphWin("Tetris", 850, 800)
    game = TetrisGame(win)
    return game
#checkSolutions['example4'](ex4)


'''
    Test TetrisGame()
    Do not edit: just use it to test your class
'''
def ex5():
    win = GraphWin("Tetris", 850, 800)
    game = TetrisGame(win)
    return game
#checkSolutions['example5'](ex5)


'''
    Test TetrisGame()
    Do not edit: just use it to test your class
'''
def ex6():
    win = GraphWin("Tetris", 850, 800)
    game = TetrisGame(win)
    return game

#checkSolutions['example6'](ex6, TetrisBlock)

