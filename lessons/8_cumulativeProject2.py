"""
Practice Project 2: Functional Approximation
Created: 3/14/2020

In this project we will create a bandpass filter.
https://en.wikipedia.org/wiki/Band-pass_filter

The purpose of a band-pass filter is to allow certain frequencies
through, and ignore all other frequencies. For example, when we tune
our radio to 104.5 FM we are tuning the parameters of a band-pass filter
to allow radio frequencies of 104.4Hz - 104.6Hz through. All other frequencies
are ignored. But how does a radio accomplish this range?

Basically, radios have in input space of the entire frequency spectrum.
This input is passed to the band-pass filter where for all values < 104.4 MHz and > 104.6 MHz
the magnitude of the frequency is sent to zero,  while the values between 104.4 and 104.6
are allowed to pass through at their original magnitude.

A simple function that approximates a band-pass filter is a step function:
f(x) =  {
        0 : x < 104.4 or x > 104.6
        1 : 104.4 < x < 104.6
        }

The issue here is that there is a discontinuity at x = 104.4 and 104.6
The step function is not continuous, so it is a good approximation, however, it is
impossible to implement.

Instead what is used are two sigmoid functions (a and b) and we take the difference
of the two, where the sigmoid functions are shifted. We will look into this more in a second.

In assignment 1_codeFunctions.py we coded the sigmoid function in example 13.
We will use this code to outline how to create a band-pass function.

Then we will graph the band-pass function using matplotlib.
"""

import numpy as np
import matplotlib.pyplot as plt
from solutions.CheckSolutions import CheckSolutions
checkSolutions = CheckSolutions().projectSolutions


'''
Part 1: 
    Define a function that returns a sigmoid function.
    The function is defined using 3 parameters:
        x: the input x value
        B: the steepness of the sigmoid
        alpha: the shift in the x direction
    return: 1 / (1 + e^(-B(x-alpha))
'''
def sigmoid(x, B, alpha):
    return 0

checkSolutions['project2p1'](sigmoid, 2, 10, 1)



'''
Part 2: 
    matplotlib does not allow us to directly graph functions. 
    What we need to do is sample the function at set intervals and 
    build two lists, one of x values, one of y values. 
    
    To do this, code a function that takes 6 inputs:
    1. sigmoid
    2. start interval
    3. end interval
    4. step size
    5. sigmoid B - gain value
    6. sigmoid alpha - shift value
        
    Functionality:
    Graph test points of sigmoid using the start, end and stepsize values. 
    
    Initialize two lists - one for x, one for y
    Then use a counter that starts from start, 
        increments by step_size,
        until the counter is >= end

    use np.arange(start, end, step_size) to help with your loop
    
    Inside the loop, append x and y values to the x and y list respectively. 
    Then plot the x, y pairs using matplotlib
    return the (x, y) values you used to plot
    
    Check your plot against the solution in solutions/8_cumulativeProject2SolutionsImages/test_sigmoid.png
'''
def test_sigmoid(sigmoid, start, end, step_size, B, alpha):
    list_x = []
    list_y = []



    plt.plot(list_x, list_y)
    plt.show()
    plt.close()
    return None

checkSolutions['project2p2'](test_sigmoid, sigmoid, start=-5, end=5, step_size=.01, B=3, alpha=1)



'''--------------------------------------------------------'''
''' Do Not Edit: Just observe! '''
'''
This function visualizes some of the parameters we are using. 
For example, as we increase B for sigmoid, we increase
the sharpness of the cuttoff. This is seen along the columns of the graph.

For the visualization we did in part2 we see that the smaller the step size
the more curved the graph looks. Therefore, to better model our function, we 
need to choose a smaller step size.  
'''
def visualize_testing():
    start = -5
    end = 7
    alpha = 2

    colors = ['lightblue', 'darkblue']
    label_colors = ['gold', 'goldenrod']
    figure, axes = plt.subplots(figsize=(15, 15), nrows=len(np.arange(.1, 2, .4)), ncols=len(np.arange(1, 10, 2)))
    for col_num, B in enumerate(np.arange(1, 10, 2)):
        for ax_num, step_size in enumerate(reversed(np.arange(.1, 2, .4))):
            list_x = []
            list_y = []
            for i in np.arange(start, end, step_size):
                list_x.append(i)
                list_y.append(sigmoid(i, B, alpha))
            axes[ax_num][col_num].plot(list_x, list_y, c=colors[col_num%len(colors)])
            axes[ax_num][col_num].set_xlabel("step_size: %.1f"%step_size, color=label_colors[ax_num%len(colors)])

            if(ax_num == 0):
                axes[ax_num][col_num].set_title("sigmoid B: %.1f"%B, color=colors[col_num%len(colors)])
    figure.tight_layout(pad=3.0)
    plt.show()
    plt.close()

#visualize_testing()
'''--------------------------------------------------------'''



'''
Part 3: 
    Now use the same process from parts 1 and 2 to create the band-pass filter. 
    We will use a new technique called a "lambda" function.
    What's cool about a lambda function is that we intitially define the function using parameters,
    but then later calls can use new variables. Don't worry too much about this. 
    The bandpass_filter is already define for you using your sigmoid function. 
    All you need to do now is visualize the bandpass filter. 
    Follow the same procedure as part2 but for the bandpass_filter.
    
    Step 1: create a function called createXY_bpf 
        The function takes:
        1. bandpass_filter - B and alphas are already set
        2. start
        3. end
        4. step
        
        return a the (x, y) points that we can graph representing the bandpass_filter we passed.
        Very similar to test_sigmoid
    
    Step 2: create a function called sweepCutoff
        This function will produce a graph of 5 different plots showing
        the graphs for 5 different B values. 
        Use the same alpha1, alpha2, for all bpf 
        and the same start, end, and step_size for all graphs
        
        Input: 
            1. a list of 5 B values
            2. cuttoff alpha1
            3. cuttoff alpha2
            4. graph start 
            5. graph end
            6. step_size
        
        return:
            a list of all [(xb1, yb1), (xb2, yb2), (xb3, yb3), (xb4, yb4), (xb5, yb5)] pairs
        
        check your graph against the solution in sweepCutoffSolution.png
        
        What you will notice from your results are that the bandpass filter is more effective
        when the gain B is larger. 
'''
# DO NOT EDIT
def bandpass_filter(B, alpha1, alpha2):
    return lambda x: sigmoid(x, B, alpha1) - sigmoid(x, B, alpha2)
bpf = bandpass_filter(10, 2, 6)  # instantiation of a bandpass_filter


def createXY_bpf(bpf, start, end, step_size):
    list_x = []
    list_y = []



    return list_x, list_y

checkSolutions['project2p3a'](createXY_bpf, bpf, -5, 10, .01)


def sweepCutoff(b_vals, alpha1, alpha2, start, end, step_size):
    all_XY = []
    figure, axes = plt.subplots(figsize=(10, 2), nrows=1, ncols=len(b_vals))





    figure.tight_layout(pad=.5)
    plt.show()
    plt.close()
    return all_XY

b_vals = [.5, 1, 5, 10, 20]  # adjust this to test other b_vals
checkSolutions['project2p3b'](sweepCutoff, b_vals, 2, 6, -10, 15, .01)
