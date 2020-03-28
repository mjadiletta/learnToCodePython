"""
Practice Project 5: Coronavirus Simulator
Created: 3/26/2020

In this project we will use what we learned from assignments 1-19 to
to code a Coronavirus Simulator.

The idea for this project comes from: https://www.washingtonpost.com/graphics/2020/world/corona-simulator/

There is no check solutions for this project. It's up to you to really get it working correctly.
I created a list of steps that you should implement to get the simulator working.

A high level overview of the important topics you've learned to get to this point:
    1. Conditional Statements and Functions
    2. Loops (for and while)
    3. Data Structures (Lists Dictionaries and Arrays)
    4. Classes and Searching Algorithms (inheritance and interfaces)
    5. Graphing and Graphics Libraries (matplotlib and graphics.py)

All of these tools are valuable in being a good programmer. Also, all of the tool we learned do
not just apply to python. All of these techniques can be implemented in every other coding
language with small changes in syntax.

Hopefully you've enjoyed the various projects so for :)
This is the last one! Good luck!
"""

import numpy as np
from solutions.graphics import *
from solutions.CheckSolutions import CheckSolutions
from solutions.CoronavirusPerson import Person
import matplotlib.pyplot as plt
checkSolutions = CheckSolutions().project5Solutions

NUM_PEOPLE = 100
PERSON_RADIUS = 6

LEFT = 50
RIGHT = 800
TOP = 50
BOTTOM = 600


TIME_SICK = 500

'''
The Simulator Class:
    For this project we will design a simulator.
    The idea is that in our simulator, we will simulate a real world by having people that interact with each other. 
    I wrote a class called Person. The person class has a variety of attributes I will talk about later but know
    that when a person is initialized to the screen, there's a 10% chance the person is sick. 
    
    The way the people interact are by moving around the environment. If a healthy person bounces off a sick person, 
    the healthy person becomes sick. After a certain number of time steps, a sick person will become recovered, 
    and change color and not be able to transmit the disease. 
    
    Once no person is sick in the simulation, the simulation should end and display a graph showing number of
    healthy, sick, and recovered over each time step. The total length of the simulation will be ~2000 time steps
    for a simulation space of 750x550 with 100 people of radius 6.  
    
    Your job is to create this simulation! Open up each of the steps below and complete in order.
'''
'''
    Step 1: Initialize the Simulation Space
        1. The Simulator takes a parameter of the window
            Save the window in an attribute called self.win
        2. Create a game window using the Rectangle graphics initialized with 
            - Points: LEFT, TOP, RIGHT, BOTTOM
                * These variables are declared at the top of the program so you can easily adjust the game size
            - Give the screen a color: I used "light cyan"
            - draw the screen
        3. Next initialize a person
            - for this step, just hard code a person's x, y position onto the screen
                * we will autogenerate people's locations later (we need to make sure they don't overlap)
            - to create a person use my class: p = Person(win, x, y, PERSON_RADIUS)
                * where win is the window, x and y are the x and y coordinates of the person and 
                    PERSON_RADIUS is a global variable
            - store this person in an attribute of the simulator called self.people = list()
                * append the person (p) to the list
'''
'''
    Step 2: Make the Person move with Constraints
        1. Code a non-terminating while loop: while True:
        2. In this loop, call p.move() where p = self.people[0]
            - The person should just fly off the screen because it's speed is too fast and we didn't constrain it
            - Set the speed of the person by p.speed = .03 (or whatever you like) and retry
        3. Add the window constraints:
            - After p.move() code a bunch of if / elif statements to make the player stay on the screen
                * We will use p.bounceWall(dx, dy) 
                    - where dx is the change in x of the the wall, and dy is the change in y of the wall
                    - make sure that dx, dy combine to make a unit vector
                * Example for bottom and top walls: p.bounceWall(1, 0)
                    - the bottom and top walls are changing in the x direction (1 unit), but not the y direction (0 units)
                * You will need 4 if statements, one for TOP, BOTTOM, LEFT, and RIGHT. 
                    - use p.x p.y and p.radius in the if statements. 
                    ex for bouncing off of the bottom wall: 
                        if p.x + p.radius > BOTTOM:
                            p.bounceWall(1, 0)
                    - repeat this for TOP, LEFT, and RIGHT using elif
            - If you run the simulation, the ball will bounce off of each wall
'''
'''
    Step 3: Initialize the Simulation with more people
        1. Notice one of the global variables in called NUM_PEOPLE
            - this will be the number of people we generate in this step
        2. Code a for loop that has the same number of loops as the number of people
            - we will add a person to self.people each iteration
            - for now, add a person to any random x, y position on the board using:
                x, y = np.random.randint(min, max),  np.random.randint(min, max)
                * note that min and max need to include both wall position and the persons radius
                    because we don't want half the person initialized in the simulaiton and half outside
            Test this and you should have 100 people all inside the simulation, but not interacting: and only 1 should move hopefully 
                - when initialized, some of the people will be overlapping
                - this is a problem we need to fix
        3. Make sure people are not initialized on top of each other. 
            - To do this, we need to check the random x, y points we just generated and
                make sure that the player we generate won't overlap with any other players
            - Use a while loop and initialize a variable no_position to True (the person dosn't have a position yet)
            Sudo code:
                no_position = True
                while no_position:
                    generate x, y
                    for each person p in people
                        if the distance between (p.x , p.y) and (x, y) is less than 2x a person's radius:
                            no_position = True  # the people are overlapping
                        else 
                            no_position = False
                generate the person using the x, y we found that doesn't overlap with anyone
                append the person to self.people
            
            If you correctly run this, then all the people should generate without overlapping.
'''
'''
    Step 4: Make People Bounce off each other
        1. Add an else statement in movePeople() after checking each of the 4 walls for colisions
            - this statement will check if two people are overlapping
            - to do this call the method: p.bouncePeople(people) 
                where people is a list of people you want to check against p to see if they're overlapping
                this method will return a person and make both p, and the person p is touching bounce off each other
            - if you run this, then one person will be moving and bouncing off of all the other people
                * Note make sure you pass a list that does not include the person you are checking
        2. Add a for loop to make all the people move
            - right now you should only have something like this in the while loop:
                p = self.people[0]
                p.move()
            - instead of only moving people[0], iterate over all people using a for loop 
                for p in self.people:
                    p.move()
                    ... # do the other 5 conditional statements (4 wall checks and the people overlapping check)
                    
                * Note, you don't want pass all the people to p.bouncePeople
                    this is for 2 reasons:
                        1. We don't want to bounce with ourselves, this will cause major problems
                        2. We don't want to bounce with anyone we already bounced with
                            Example: 
                            person 0 is passed people 1-99 and bounces with person 5
                            person 5 is passed people 0-3 and 5-99 and bounces with person 1
                                now both person 0 and person 5 are bouncing twice which doesn't work
                    - Solution, if we are checking person 5, only check people 6-99
                        * do this using list slicing: 
                            self.people[(current person index) + 1: len(people)] 
                        * there are a number of ways to keep track of what person index you're on, use your own idea
        3. Upon completion of this step, all the people should be moving and bouncing off each other and walls
            - if they are moving slowly, make sure didn't set their speed to less than 1.
            - if it's going super slow, decrease the global variable NUM_PEOPLE from 100 to ~50. 
                * That should still give good results
'''
'''
    Step 5: Make the Disease Transferable
        1. You may have noticed that some people are initialized to "MistyRose2" and others "firebrick3"
            - the people that are "MistyRose2" have an attribute called "condition" set to "healthy"
            - the people that are "firebrick3" have an attribute called "condition" set to "sick"
            - every person has a 10% chance of being initialized to "sick"
            - In this step, if a healthy person bounces off a sick person, the healthy person will become sick
        2. In the else statement we coded, we check p.bounces(people[i+1:]). 
                This function returns the person you bounced off of.
            - thus call the function like this: p2 =  p.bounces(people[i+1:])
            - if p doesn't bounce off of anything, it will return None, if it does bounce off a person, it returns the person
            1. Check if p2 isn't None:
                2. Check if p2 is "sick" using p2.condition:
                    If p2 is "sick" set p.condition to "sick"
                    set p2.time_sick = 0  # because p2 just became sick
                    p2.setFill("firebrick3")
                3. Check if p is "sick" using p1.condition :
                    If p is "sick" set p2.condition to "sick"
                    set p.time_sick = 0  # because p just became sick
                    p.setFill("firebrick3")
        3. At the end of this you should have people bouncing off each other and transferring the disease until 
            everyone has the disease and is colored "firebrick3"
'''
'''
    Step 6: Be able to Recover
    1. Every time we move we need to do two checks: 
            person.condition is "healthy"
            person.condition is "sick"
        - Set up an if, else statement with these two checks after p.move() but before checking bounces
    2. If "healthy" just pass for now
    3. If "sick":
        - increment p.time_sick by 1
        - set a variable called "virusAlive" to True 
            * we can use this for the while loop. Instead of just using while True
                - initialize virusAlive = True before entering the while loop 
                - then immediately set virusAlive = False as the first step in the while loop
                - in the else statement representing p.condition == "sick" we set this to True so as long 
                    as someone is "sick" the simulation will keep running, but once no one is sick, we will exit
    4. Add an elif statement after if p.condition == "healthy"
        - this checks if the person has been sick longer than TIME_SICK using p.time_sick > TIME_SICK
        - if it's true, change the condition of the person to "recovered"
        - change the fill to "SteelBlue4"
    5. After this step is complete, your program should model the coronavirus using hyperparameters:
        NUM_PEOPLE and TIME_SICK. 
        By adjusting these people we can adjust how long a person is sick, and how many people are in the simulation
'''
'''
    Step 6: Adding Statistics
        We want to know just how many people are healthy, sick, and recovered at each stage of this simulation
        - essentially we want to show the curve the Dr. Fauci has been talking about where if everyone is moving 
            around like regular life, everyone will get sick at once and overflow the hospitals immediately
        1. Initialize 3 empty lists for healthy, sick, and recovered before you enter the while loop of the simulation
            - sim_healthy = []
            2. create three counters after entering the while loop and set to zero: 
                - num_healthy = 0, num_sick = 0, num_recovered = 0
            3. In each of the condition checks: if p.condition == "healthy", ...
                - increment the appropriate variable
            4. After iterating over all the people in the for loop, append the number of healthy, sick and recovered
                to the correct lists
            5. Repeat until the simulation terminates
        6. After the while loop / the simulation ends, graph the three datasets using matplotlib
            - plt.title("Coronavirus Simulator")
            - plt.plot(np.arange(sim_healthy), sim_healthy, color="thistle", label="healthy")
            - ...
            - plt.legend()
            - plt.xlabel("Time Steps")
            - plt.ylabel("Number of People")
            - plt.show()
        7. At the end of this step you should be able to generate a graph that shows what happens in a society 
            where everyone is moving around and interacting.
            The curve should look the curve in "solutions/20_coronavirusSimulatorSolutionImages/coronavirusSimulatorResultsHIGH.png"
            where more than 80% of the population is sick at one time. Really bad, we need to flatten this curve...
'''
'''
    Step 7: Changing the curve
        1. There are a million ways we can change this curve. I will show you one that models people staying home if sick
        2. In the else statement where you increment the num_sick, add a line: p.speed = 0
            - now if the person is sick, the person won't move
        3. In the elif statement where you increment the num_recovered add a line: p.speed = 1
        Run the simulation and see how it changes the curve :)
        Check your solution with "/coronavirusSimulatorResultsLOW.png"
        Try your own variations by changing the population size, the time sick, and adding your own variables
            - One thing you can add is PROBABILITY_OF_TRANSMISSION where if a healthy person touches someone sick, 
                the healthy person has probability PROBABILITY_OF_TRANSMISSION of getting sick
            - Slow down how much healthy people move
            - As you're initializing people, give each person a probability of moving or staying home 
                PROBABILITY_OF_STAYING_HOME and see how that affects your results. 
'''
class Simulator:
    def __init__(self, win):
        self.win = win





    def movePeople(self):





        # press enter to exit window
        while True:
            key = self.win.getKey()
            if key == "Return":
                self.win.close()
                break

def proj5():
    win = GraphWin("Cooronavirus", RIGHT + 50, BOTTOM + 50)
    sim = Simulator(win)
    sim.movePeople()

proj5()