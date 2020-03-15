"""
Practice Group 7: Introduction to Matplotlib
Created: 3/14/2020

In this assignment we will learn to use the python package matplotlib.
This package is incredibly useful for visualizations. Matplotlib
functionality includes building bar charts, scatter plots, line graphs,
and much more.

The specific API (Application Program Interface) we will use is matplotlib.pyplot
To see other API's matplotlib offers, just type "matplotlib." in pycharm and a list
of other possible options will appear.

Learning Outcomes:
1) Understand how to build various graphs using matplotlib
2) Use various customization features of matplotlib to create more visual graphs
3) Include more than one graph on a single matplotlib display

Online Documentation: https://matplotlib.org/

Notes: Looking at our imports, notice we are importing matplotlib.pyplot as plt. This
is similar to how we used numpy, where instead of having to write numpy.average()
we could just write np.average. For matplotlib, rather than writing matplotlib.pyplot.
evertime we need something from that package, we can use plt.

Example 1 is completed as a template.
For each of the following examples, replace blank lines
with the correct functionality. If completed correctly, the checkSolutions
will print "Correct Solution" to the terminal.


It is not possible to check the exact configuration of your graph so compare
your solutions to the correct images by looking at the images in:
    solutions/7_matplotlibIntroductionSolutionsImages
"""


import numpy as np
import matplotlib.pyplot as plt
from solutions.CheckSolutions import CheckSolutions

checkSolutions = CheckSolutions().matplotlibIntro

data_path = "../data/numpy60MeterDashEx.npy"

'''
Example 1: 
    Write a function that loads the data from "data/numpy60MeterDashEx.npy"
     and visualizes it using matplotlib. The intended graph is a scatter plot
     of the data. 
     
     return the x and y coordinates used for plotting (x, y)
'''
def ex1(path):
    '''
    Load data and setup x and y coordinates
    Note: notice that there are no x coordinates with this data
          We must make the x labels for this data.
          Since the data is already ordered temporally, we need the
          first label to be x=0, the second data point to be x=1, etc.

          To do this we use np.arange(num) which produces an ordered numpy array.
          Thus the result we are looking for:
              x = [   0,    1,    2,    3, ...   23]
              y = [7.13, 7.09, 7.21, 7.28, ... 7.14]
              plt.plot(x, y)
    '''
    data = np.load(path)
    number_data_points = np.shape(data)[0]  # 24
    x_coordinates = np.arange(number_data_points) # 0 1 2 3 ... 23
    y_coordinates = data

    #initialize the figure with 3 rows and 1 column of subplots.
    figure, axes = plt.subplots(nrows=3, ncols=1)
    ax1 = axes[0]
    ax2 = axes[1]
    ax3 = axes[2]

    # Subplot 1--------------------------------------------------------------------------------
    ax1.plot(x_coordinates, y_coordinates)
    ax1.set(xlabel='race', ylabel='time (s)', title='60m Dash Race Progression')
    ax1.grid() # add a grid to the graph if you want

    # Subplot 2--------------------------------------------------------------------------------
    ax2.plot(x_coordinates, y_coordinates, 'g')
    ax2.set(xlabel='race number', ylabel='time in seconds', title='60m Dash Race Progression (Green)')

    # Subplot 3--------------------------------------------------------------------------------
    ax3.plot(x_coordinates, y_coordinates, 'b^')
    ax3.grid()

    # show the window. The program only continues after we close the window
    # Comment out this line after you complete each assignment.
    # That way it stops popping up while you are debugging other examples.
    figure.tight_layout(pad=1.5)
    plt.show()
    plt.close()
    return (x_coordinates, y_coordinates)

checkSolutions['example1'](ex1, data_path)



'''
Example 2:
    Write a function that creates a figure with 2 subplots - 1 row, 2 columns. 
    The first subplot is a line graph of the data in "../data/numpy60MeterDashEx.npy". 
    The second subplot is a histogram of the same data with 10 bins 
        (look up with bins are from the documentation and try various bin sizes - kinda interesting) 
    Documentation for histogram: https://matplotlib.org/api/_as_gen/matplotlib.pyplot.hist.html#matplotlib.pyplot.hist
    
    return (x_line_graph, y_line_graph, values_of_histogram_bins)
'''
def ex2(path):
    data = None
    x_coordinates = None
    y_coordinates = None

    # initialize the figure with 1 row and 2 columns of subplots.
    figure, axes = plt.subplots(figsize=(10, 5), nrows=1, ncols=2)
    ax1 = axes[0]
    ax2 = axes[1]

    # Subplot 1--------------------------------------------------------------------------------
    ax1.plot(0, 0, color='skyblue')
    ax1.set(xlabel=None, ylabel=None, title=None)
    ax1.grid()  # add a grid to the graph if you want

    # Subplot 2--------------------------------------------------------------------------------
    n, b, p, = ax2.hist(0, bins=1, color='skyblue')
    ax2.set(xlabel=None, ylabel=None, title=None)

    figure.tight_layout(pad=1.5)  # so there is spacing between the subplots
    #plt.show()
    plt.close()
    return x_coordinates, y_coordinates, n

checkSolutions['example2'](ex2, data_path)



'''
Example 3:
    Write a function that creates a figure with 4 subplots - 2 rows, 2 columns. 
    The top left subplot is a line graph of the first half of data in "../data/numpy60MeterDashEx.npy". 
    The top right subplot is a histogram of the first half of data with 6 bins 
    The bottom left subplot is a line graph of the second half of data in "../data/numpy60MeterDashEx.npy". 
    The bottom right subplot is a histogram of the second half of data with 6 bins 
        (look up with bins are from the documentation and try various bin sizes - kinda interesting) 
    Documentation for histogram: https://matplotlib.org/api/_as_gen/matplotlib.pyplot.hist.html#matplotlib.pyplot.hist

    basically doing the same thing as ex2 but with half the data, and four subplot instead of 2.

    return 6 values:
    return (x_line_graph_top_left, y_line_graph_top_left, values_of_histogram_bins_top, 
            x_line_graph_bottom_left, y_line_graph_bottom_left, values_of_histogram_bins_bottom)
'''
def ex3(path):
    data = None

    x_coordinates_top = None
    y_coordinates_top = None
    x_coordinates_bottom = None
    y_coordinates_bottom = None

    # initialize the figure with 2 rows and 2 columns of subplots.
    figure, axes = None, None # plt.subplots(figsize=(8, 8), nrows=__, ncols=__)
    ax1 = None
    ax2 = None
    ax3 = None
    ax4 = None

    # Subplot 1--------------------------------------------------------------------------------
    #ax1.plot(None, None, color='skyblue')
    #ax1.set(xlabel=None, ylabel=None, title=None)
    #ax1.grid()

    # Subplot 2--------------------------------------------------------------------------------
    n_top = None  # created from hist
    #n_top, b, p, = ax2.hist(None, bins=__, color='skyblue')
    #ax2.set(xlabel=None, ylabel=None, title=None)

    # Subplot 3--------------------------------------------------------------------------------
    #ax3.plot(None, None, color='skyblue')
    #ax3.set(xlabel=None, ylabel=None, title=None)
    #ax3.grid()  # add a grid to the graph if you want

    # Subplot 4--------------------------------------------------------------------------------
    n_bottom = None  # created from hist
    #n_bottom, b, p, = ax4.hist(None, bins=__, color='skyblue')
    #ax4.set(xlabel=None, ylabel=None, title=None)

    #figure.tight_layout(pad=1.5)
    #plt.show()
    #plt.close()
    return (x_coordinates_top, y_coordinates_top, n_top, x_coordinates_bottom, y_coordinates_bottom, n_bottom)

checkSolutions['example3'](ex3, data_path)



'''
Example 4:
    Write a function that creates a figure with 2 subplots - 1 row, 2 columns. 
    In the left subplot, draw a line graph of the first 12 datapoints in red, 
        then overlay a line graph of the second 12 datapoints in blue,
        then add a legend! do not forget this! It's not hard...
        use label='label' in the plt.plot function
        then call ax_.legend() 
        Documentation: https://matplotlib.org/api/_as_gen/matplotlib.pyplot.legend.html
        
    In the right subplot, create a histogram with 5 bins of the first 12 datapoints in red,
        then overlay a histogram with 5 bins of the second 12 datapoints in blue,
        then add a legend for the histogram
    
    When overlaying the histogram, make the graph semitransparent. 
        - The variable alpha = .5 sets color to 50% transparent

    basically doing the same thing as ex3 but plotting the two graphs on the same subgraphs.

    return 6 the same values from the last question:
    return (x_coordinates_red, y_coordinates_red, n_red, 
            x_coordinates_blue, y_coordinates_blue, n_blue)
'''
def ex4(path):
    # get data and separate correctly into:
    x_coordinates_red = None
    y_coordinates_red = None
    x_coordinates_blue = None
    y_coordinates_blue = None

    # initialize the figure with 3 rows and 1 column of subplots. Start with subplot 1
    figure, axes = plt.subplots(figsize=(10, 5), nrows=1, ncols=2)
    ax1 = axes[0]
    ax2 = axes[1]

    # Subplot 1--------------------------------------------------------------------------------
    # plot the line graphs on ax1


    # Subplot 2--------------------------------------------------------------------------------
    # plot the histograms on ax2 and return the correct vals from the histograms for the red and blue graphs
    n_red = None
    n_blue = None


    figure.tight_layout(pad=1.5)
    #plt.show()
    plt.close()
    return (x_coordinates_red, y_coordinates_red, n_red, x_coordinates_blue, y_coordinates_blue, n_blue)


checkSolutions['example4'](ex4, data_path)
