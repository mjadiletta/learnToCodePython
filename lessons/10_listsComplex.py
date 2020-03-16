"""
Practice Group 10: Using Lists for Sorting
Created: 3/16/2020

In this tutorial we will cover sorting algorithms.
We will start by allowing you to use any sorting algorithm you can
in order to sort lists by yourself. Just produce the correctly sorted list.

Later we will learn 7 types of sorting algorithms:
    1. Insertion Sort: ex4
    2. Selection Sort: ex5
    3. Bubble Sort: ex6

Sorting algorithms are fundamental to understanding how to code!
I provide explanations for each of these sorting methods, but more
detailed explanations can be found here: https://www.studytonight.com/data-structures/

Example 1 is completed as a template.
For each of the following examples, replace blank lines
with the correct functionality. If completed correctly, the checkSolutions
will print "Correct Solution" to the terminal.
"""

import numpy as np
import matplotlib.pyplot as plt
import copy
from solutions.CheckSolutions import CheckSolutions

checkSolutions = CheckSolutions().listComplexSolutions
randInt = lambda : np.random.randint(-100, 100)


list_a = [1, 9, 5, 3, 2, 7, 8, 4, 6]
print("list a: " + str(list_a))
print("--------------------------------")

'''
Example 1: Sort with what you know!
    Code a loop that sorts list_a from lowest value to highest value. 
    You are allowed to append lists to a new new_list 
    return the correctly sorted new_list
    
    The idea I'm using in this example is to iterate over list_a and find the lowest value
    every time. Then I remove that value from list_a and add it to new_list. This means we
    need to remove all values from list_a and add them to the new_list. 
        - this is why I have -> while len(list_a) > 0:
    Then I'm iterating over the remaining values in list_a
        - this is why I have -> for index in range(len(list_a)):
    Since list_a.pop(current_min_index) returns the value of the index we are "popping" 
    I append it to new_list directly -> new_list.append(list_a.pop(current_min_index))
    
    Note: I keep track of two values; current_min_value and current_min_index
        - the min value tracks the minimum value each iteration over the list
            as we test each element in the list, we want to see if the next element is less the 
                best minimum we've seen so far
                we start with np.inf so that we have the largest possible number our program can handle
        - the min index is so that once we have the minimum value, we can access it to remove it
        
    The general look for list_a and new_list each iteration of the while loop:
    
    Loop 1: 
        list_a = [9, 5, 3, 2, 7, 8, 4, 6]       -> current_min_value = 1; current_min_index = 0
        new_list = [1]
    Loop 2: 
        list_a = [9, 5, 3, 7, 8, 4, 6]          -> current_min_value = 2; current_min_index = 3
        new_list = [1, 2]
    Loop 3:
        list_a = [9, 5, 7, 8, 4, 6]             -> current_min_value = 3; current_min_index = 2
        new_list = [1, 2, 3]
    ...
    Loop 9:
        list_a = []                             -> current_min_value = 9; current_min_index = 0
        new_list = [1, 2, 3, 4, 5, 6, 7, 8, 9] 
'''
def ex1(list_a):
    list_a = copy.deepcopy(list_a)  # need to do this so that the original list_a isn't edited
    new_list = []

    while len(list_a) > 0:
        current_min_value = np.inf
        current_min_index = None
        for index in range(len(list_a)):
            if list_a[index] < current_min_value:
                current_min_value = list_a[index]
                current_min_index = index
        new_list.append(list_a.pop(current_min_index))
    return new_list

checkSolutions['example1'](ex1, list_a)
print("list a sorted: " + str(ex1(list_a)) + "\n")



'''
Example 2: Sort with what you know!
    Following the same procedure as ex1, sort list_a
    in reverse order. 
    
    return the new list
    
    Hint: the solution is [9, 8, 7, 6, 5, 4, 3, 2, 1] 
        - use sorting to derive this, not manually returning this list 
'''
def ex2(list_a):
    list_a = copy.deepcopy(list_a)  # need to do this so that the original list_a isn't edited
    new_list = []

    while len(list_a) > 0:
        current_max_value = -np.inf
        current_max_index = None
        for index in range(len(list_a)):
            if list_a[index] > current_max_value:
                current_max_value = list_a[index]
                current_max_index = index
        new_list.append(list_a.pop(current_max_index))
    return new_list

checkSolutions['example2'](ex2, list_a)
print("list a reverse sorted: " + str(ex2(list_a)) + "\n")



'''
Example 3:
    Create a list of random integers between -100 and 100. 
    The function takes the number of random numbers to generate in the list
    return the list of length, number_items
    
    This is not a sorting algorithm, but we will use this function 
    in the upcoming examples. 
    
    Hint: Use the randInt() function I defined above to generate
    random numbers between -100 and 100. 
'''
def ex3(number_items):
    random_list = []
    for i in range(number_items):
        random_list.append(randInt())
    return random_list

checkSolutions['example3'](ex3, 25)

random_list = ex3(25)
print("random list: " + str(random_list))


'''
Example 4: Insertion Sort!
    Read this before starting: https://www.studytonight.com/data-structures/insertion-sorting
    
    Define a function that takes 2 parameters:
        1. an unsorted list (random_list)
        2. a number between -100 and 100
    
    Sort the random_list using ex1()
    Then insert the new number into the sorted random_list in the correct spot. 
    
    Return the sorted random_list
'''
def ex4(random_list, insert_number):
    sorted_list = ex1(random_list)
    for index in range(len(sorted_list)):
        if sorted_list[index] > insert_number:
            sorted_list.insert(index, insert_number)
            break
    return sorted_list

checkSolutions['example4'](ex4, random_list, randInt())



'''
Example 5: Selection Sort!
    Read this before starting: https://www.studytonight.com/data-structures/selection-sorting

    Define a function that takes 1 parameter:
        1. an unsorted list (random_list)

    Sort the list using the Selection Sort Methodology.
    General idea:
        ex: in a 4 element list: 
            Initiate Selection Sort:
                a = [2, 4, 1, 3]
            iteration 1: 
                - start searching for minimum number at index 0
                - swap numbers 2 and 1
                a = [1, 4, 2, 3] (4 numbers visited: 2, 4, 1, 3)
            iteration 2: 
                - start searching for minimum number at index 1
                - swap numbers 4 and 2
                a = [1, 2, 4, 3] (3 numbers visited: 4, 2, 3)
            iteration 3: 
                - start searching for minimum number at index 2
                - swap numbers 3 and 4
                a = [1, 2, 3, 4] (2 numbers visited: 4, 3)
            iteration 4:
                - start searching for minimum number at index 3
                - Do not swap numbers
                a = [1, 2, 3, 4] (1 number visited: 4)
            
            total number of items visited = 10
            return (a, 10)
            
    Return the sorted random_list and the total number of elements you checked
    Hint: the total number of elements for the random_list should be 50+49+48+...+3+2+1
'''
def ex5(random_list):
    sort_list = copy.deepcopy(random_list)  # must include this so we don't mess up the original random_list
    start_index = 0
    elements_visited = 0
    for number_sorted in range(len(sort_list)):
        min_index = start_index
        for index in range(start_index, len(sort_list)):
            if (sort_list[index] < sort_list[min_index]):
                min_index = index
            elements_visited += 1

        sort_list[start_index], sort_list[min_index] = sort_list[min_index], sort_list[start_index]
        start_index += 1
    return sort_list, elements_visited

checkSolutions['example5'](ex5, random_list)



'''
Example 6: Bubble Sort!
    Read this before starting: https://www.studytonight.com/data-structures/bubble-sort

    Define a function that takes 1 parameter:
        1. an unsorted list (random_list)

    Sort the list using the Bubble Sort Methodology.
    General idea:
        ex: in a 4 element list: 
            Initiate Selection Sort:
                a = [2, 4, 1, 3]
                swap_flag = False
                sorted_elements_back = 0
            iteration 1:
                for index in range(len(a) - sorted_elements_back - 1):
                    check (index 0):
                        - since 2 < 4, do not swap
                        - swap_flag = False
                        a = [2, 4, 1, 3] (2 new numbers visited)
                    check (index 1):
                        - since 4 > 1, swap 4 and 1
                        swap_flag = True
                        a = [2, 1, 4, 3] (1 new number visited)
                    check (index 2):
                        - since 4 > 3, swap 4 and 3
                        - swap_flag = True
                        a = [2, 1, 3, 4] (1 new number visited)
                sorted_elements_back = 1 -> this means the last number is the largest 
                                            and we don't need to revisit it!
            iteration 2:
                reset swap_flag: swap_flag = False
                for index in range(len(a) - sorted_elements_back - 1):
                    check (index 0)
                        - since 2 > 1, swap 2 and 1
                        - swap_flag = True
                        a = [1, 2, 3, 4] (2 new numbers visited)
                    check (index 1)
                        - since 2 < 3, do not swap
                        - swap_flag = True
                        a = [1, 2, 3, 4] (1 new number visited)

                sorted_elements_back = 2 -> this means the last two numbers are the largest 
                                            and we don't need to revisit them!
            iteration 3:
                reset swap_flag: swap_flag = False
                for index in range(len(a) - sorted_elements_back - 1):
                    check (index 0)
                        - since 1 < 2, do not swap
                        - swap_flag = False
                        a = [1, 2, 3, 4] (2 new numbers visited)
                sorted_elements_back = 3 -> this means the last three numbers are the largest 
                                            and we don't need to revisit them!
                
                since swap_flag == False, we know the list is sorted.
            return the list

            total number of new items visited = 9
            return (a, 9)
'''
def ex6(random_list):
    sort_list = copy.deepcopy(random_list)  # must include this so we don't mess up the original random_list
    swap_flag = True
    new_elements_visited = 0
    sorted_elements_back = 0
    while(swap_flag):
        swap_flag = False
        for i in range(len(sort_list) - 1 - sorted_elements_back):
            if i == 0:
                new_elements_visited += 2
            else:
                new_elements_visited += 1
            if sort_list[i] > sort_list[i+1]:
                sort_list[i], sort_list[i+1] = sort_list[i+1], sort_list[i]
                swap_flag = True
        sorted_elements_back += 1
    return sort_list, new_elements_visited

checkSolutions['example6'](ex6, random_list)



'''
Example 7: Visualizing Selection Sort vs Bubble Sort

Selection Sort will always view a constant number of elements
Bubble Sort, depending on how sorted the original sequence is, will visit var fewer nodes.

Lets graph this relationship:
    1. Create a bar chart with 5 different paris of bars
        - The different pairs of bars represent different lengths of random_list
        - bar pair 1: len(random_list) = 10
        - bar pair 2: len(random_list) = 20
        - bar pair 3: len(random_list) = 50
        - bar pair 4: len(random_list) = 100
        - bar pair 5: len(random_list) = 1000
    2. Each pair of bars represents a Bubble Sort vs Selection Sort.
    3. The height of the bars represent the total number of elements visited by the algorithm 
        - the bubble sort will be less than or equal to the selection sort in all cases
        - the selection sort will not change with the random_list, but bubble sort will
    
    Since we have not yet covered bar charts, you will need to learn how to create them in matplotlib:
    basic bar charts are covered here: https://matplotlib.org/api/_as_gen/matplotlib.pyplot.bar.html
    grouped bar charts are covered here: https://matplotlib.org/gallery/lines_bars_and_markers/barchart.html#sphx-glr-gallery-lines-bars-and-markers-barchart-py

    call ex3(num) for a random list of size num
    call ex6(list) for bubble sort data 
    call ex5(list) for selection sort data
    
    Hint: 
        ex5(ex3(10))[1] return the number of elements visited for selection_sort of list size 10
        ex6(ex3(50))[1] return the number of elements visited for bubble_sort of list size 50
    
    return selection_sort 
    Check your graph solution against the solution in: "solutions/10_listComplexSolutionImages/example7.png"
    The numbers for bubble sort will be similar but not exact... just get close enough.
'''
def ex7():
    labels = ['10 elements', '20 elements', '30 elements', '40 elements', '50 elements']
    bubble_sort_means = None
    selection_sort_means = None

    x = np.arange(len(labels))  # the label locations
    width = 0.35  # the width of the bars

    figure, ax = plt.subplots(figsize=(9, 8))
    bubble_sort = ax.bar(x - width / 2, 0, width, label='Bubble Sort')
    selection_sort = ax.bar(x + width / 2, 0, width, label='Selection Sort')

    ######### Don't Edit Below Here ###########

    ax.set_ylabel('Average Number of Elements Visited')
    ax.set_title('Bubble Sort vs Selection Sort')
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.legend()

    def autolabel(rects):
        for rect in rects:
            height = rect.get_height()
            ax.annotate('{}'.format(height),
                        xy=(rect.get_x() + rect.get_width() / 2, height),
                        xytext=(0, 3),  # 3 points vertical offset
                        textcoords="offset points",
                        ha='center', va='bottom')
    autolabel(bubble_sort)
    autolabel(selection_sort)

    figure.tight_layout()
    plt.show()

    return selection_sort_means

checkSolutions['example7'](ex7)