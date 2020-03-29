"""
Practice Group 15: File Organization and Separation
Created: 3/28/2020

In this tutorial we will cover a common use of OOP to create a "graph."

You may have heard of a binary search tree, or a heap, these are both
considered graphs in computer science. A graph is basically a collection
of nodes and edges. Nodes hold data and edges are the connections or paths
between nodes. OOP is a great way to implement different data structures,
including graphs. In this lecture you will be implementing a binary search
tree and learning about its effectiveness. This will give you a TON of practice
applying the OOP techniques you have learned, while also learning some new
sorting and searching algorithms and data structures.

Learning Objectives:
    1. Create a binary search tree using the node class
    2. Develop the BST insert algorithm
    3. Develop the BST search algorithm
    4. Big-O and the Effectiveness of BSTs
    5. What's the point?
"""

from solutions.CheckSolutions import CheckSolutions
checkSolutions = CheckSolutions().searchingSortingSolutions

'''
Example 1: Binary Search Tree

A binary search tree is a type of graph that allows us to reduce the search space by 
half after each node we visit. What does this mean? First look at the example below 
where we put the numbers 1 to 10 in a binary search tree with 5 as the root.

                              __5__
                             /     \
                            2       8     
                           / \     / \ 
                          1   3   6   9
                               \   \   \
                                4   7   10

As you can see 5 is at the top of this tree, in this case 5 is the root. We consider the 
root to be the node that has no parents, it is also the node that we start our search algorithms 
from. Starting at node 5 (root node), we can see that there are two branches (edges) that come out
of node 5, one that connects to node 2 and another that connects to node 8. In this case, node 2 
and node 8 are considered the CHILDREN or CHILD NODES of node 5. We can also say that node 5 is 
the PARENT NODE or PARENT of nodes 2 and 8. To help you remember this terminology, simply think of 
it as a family tree, where 5 represents the first relative on record (root) and then we can track the 
children that are related to 5 through the tree. 

All of the information we discussed above can be true for pretty much an search tree/graph in computer 
science, however, we want to work with BSTs or binary search trees. So we know what a search tree is, 
but what does the binary part of BST mean? Basically it denotes the maximum number of children each node 
can have. Binary means that each node in a BST can have AT MOST 2 children. It is perfectly fine if the 
node has 0 children or 1 child or 2 children, as long as it does not exceed 2 children then it works! 

Another feature of BSTs is how we add new nodes to the tree and how we search for nodes in the tree. These 
two operations are very similar because they both have to do with the organization of the tree. 

Look at the tree above. Starting at the root (node 5) you can see that all nodes on the right side of the 
tree have a value greater than the root node and all nodes on the left side of the tree have a value that is
less than the root node. THIS IS REALLY IMPORTANT! PLEASE REREAD THIS LIKE 2 MORE TIMES TO MAKE SURE 
YOU UNDERSTAND IT!

That was a lot of information so lets start by creating a BST with a predefined node class.
'''


class Node:
    def __init__(self, value):
        self.value = value
        self.right_child = None
        self.left_child = None

    def add_child(self, value):
        if value > self.value:
            if self.right_child is None:
                self.right_child = Node(value)
                return self.right_child
            else:
                return self.right_child.add_child(value)
        else:
            if self.left_child is None:
                self.left_child = Node(value)
                return self.left_child
            else:
                return self.left_child.add_child(value)

'''
Example 1: Build a tree
    The current tree is only has 3 numbers: 50, 25, 75.
    We want to add to the tree the following numbers: 1, 40, 60, 90, 35, 65, 80 added to it
    It is your job to add the rest of the nodes to the tree using the class above / method started below
'''
root = Node(50)
root.add_child(25)
root.add_child(75)

# SOLUTION BEGIN - DELETE
root.add_child(1)
root.add_child(40)
root.add_child(60)
root.add_child(90)
root.add_child(35)
root.add_child(65)
root.add_child(80)
# SOLUTION END - DELETE
checkSolutions["example1"](root)


'''
Example 2: BST Insert

Now that you have created a BST, lets develop the insert algorithm for it!

First, lets create a new node class from scratch...

    1. Lets call this class BSTNode
    2. You can basically copy the constructor from the Node class above
    3. Now, lets write our own add_child method, however, this one should be called "insert" NOT "add_child"
        a. name of method: insert
        b. parameters/arguments to the method: value (an integer)
        c. now we have to think about where in the tree to add this new value
           
           Remember how the BST is organized and hopefully this will be pretty straight forward.
           1. Check if the value input to this method is greater than the current node's value
           2. If the input value is greater: check if the current node has a right_child 
                If it DOES have a child to the right then simply call the "insert" method on that child
                If it DOES NOT have a child to the right then create a new BSTNode and set right_child equal to it
           3. If the input value is less than or equal to (else): check if the current node has a left_child
                If it DOES have a child to the left then simply call the "insert" method on that child
                If it DOES NOT have a child to the left then create a new BSTNode and set left_child equal to it
                
        NOTE: the best way to understand this is to visualize it so I have included a link to a YouTube video below 
            https://www.youtube.com/watch?v=cv_KDQzZpHs
            start video at: 58 seconds   end video at: 1 minute 59 seconds
            
            I have also included a step by step example below, but I recommend you watch the 1 minute clip on YouTube
            
            
            Building a BST Example:
            
             _________________________________________________________________________________________________________
            |     OPERATION       |          UPDATED BINARY SEARCH TREE        |                 NOTES                |
            |---------------------+--------------------------------------------+--------------------------------------|
            |                     |                                            | You always start with nothing        |
            |---------------------+--------------------------------------------+--------------------------------------|
            | Insert(5)           |                      5                     | 5 is now your root node              |
            |---------------------+--------------------------------------------+--------------------------------------|
            |                     |                      5                     | Starting at our root node, we check  |
            | Insert(2)           |                     /                      | to see if 2 is less than or greater  |
            |                     |                    2                       | than 5, 2 < 5, so add it to the left |
            |---------------------+--------------------------------------------+--------------------------------------|
            |                     |                      5                     | Starting at our root node, we check  |
            | Insert(8)           |                     / \                    | to see if 8 < 5 or if 8 > 5, 8 > 5,  |
            |                     |                    2   8                   | so we add it to the right of 5       |
            |---------------------+--------------------------------------------+--------------------------------------|
            |                     |                      5                     | Starting at our root node, we check  |
            |                     |                     / \                    | to see if 6 < 5 or if 6 > 5, 6 > 5,  |
            | Insert(6)           |                    2   8                   | so we add it to the right of 5, but  |
            |                     |                       /                    | 8 is already to the right of 5, so   |
            |                     |                      6                     | we check if 6 < 8 or 6 > 8, 6 < 8 so |
            |                     |                                            | we add 6 to the left of 8            |
            |---------------------+--------------------------------------------+--------------------------------------|
            |                     |                      5                     | Starting at our root node, we check  |
            |                     |                   /     \                  | to see if 1 < 5 or if 1 > 5, 1 < 5,  |
            | Insert(1)           |                  2       8                 | so we add it to the left of 5, but   |
            |                     |                 /       /                  | 2 is already to the left of 5, so    |
            |                     |                1       6                   | we check if 1 < 2 or 1 > 2, 1 < 2 so |
            |                     |                                            | we add 1 to the left of 2            |
            |---------------------+--------------------------------------------+--------------------------------------|
            |                     |                      5                     | Starting at our root node, we check  |
            |                     |                   /     \                  | to see if 3 < 5 or if 3 > 5, 3 < 5,  |
            | Insert(3)           |                  2       8                 | so we add it to the left of 5, but   |
            |                     |                 / \     /                  | 2 is already to the left of 5, so    |
            |                     |                1   3   6                   | we check if 3 < 2 or 3 > 2, 3 > 2 so |
            |                     |                                            | we add 3 to the right of 2           |
            |---------------------+--------------------------------------------+--------------------------------------|
            |                     |                      5                     | Starting at our root node, we check  |
            |                     |                   /     \                  | to see if 7 < 5 or if 7 > 5, 7 > 5,  |
            |                     |                  2       8                 | so we add it to the right of 5, but  |
            |                     |                 / \     /                  | 8 is already to the right of 5, so   |
            | Insert(7)           |                1   3   6                   | we check if 7 < 8 or 7 > 8, 7 < 8 so |
            |                     |                         \                  | we add 7 to the left of 8, but 6 is  |
            |                     |                          7                 | already there, so we check if 7 < 6  |
            |                     |                                            | or 7 > 6, 7 > 6 so we add it to the  |
            |                     |                                            | right of 6                           |
            |---------------------+--------------------------------------------+--------------------------------------|
            |                     |                      5                     | Starting at our root node, we check  |
            |                     |                   /     \                  | to see if 9 < 5 or if 9 > 5, 9 > 5,  |
            |                     |                  2       8                 | so we add it to the right of 5, but  |
            | Insert(9)           |                 / \     / \                | 8 is already to the right of 5, so   |
            |                     |                1   3   6   9               | we check if 9 < 8 or 9 > 8, 9 > 8 so |
            |                     |                         \                  | we add 9 to the right of 8           |
            |                     |                          7                 |                                      |
            |---------------------+--------------------------------------------+--------------------------------------|
            |                     |                      5                     | Starting at our root node, we check  |
            |                     |                   /     \                  | to see if 4 < 5 or if 4 > 5, 4 < 5,  |
            |                     |                  2       8                 | so we add it to the left of 5, but   |
            |                     |                 / \     / \                | 2 is already to the left of 5, so    |
            | Insert(4)           |                1   3   6   9               | we check if 4 < 2 or 4 > 2, 4 > 2 so |
            |                     |                     \   \                  | we add 4 to the right of 2, but 3 is |
            |                     |                      4   7                 | already there, so we check if 4 < 3  |
            |                     |                                            | or 4 > 3, 4 > 3 so we add it to the  |
            |                     |                                            | right of 3                           |
            |_____________________|____________________________________________|______________________________________|
            

Hopefully after reading all of that you can identify repeated operations when you are trying to insert a number into 
a BST. Now you should implement the BSTNode class below!
'''


'''
Example 2.1: Recursion - Fibonacci

Just a side note... recursion is normally used to implement the insert function for a BST. Recursion is a tricky topic 
to understand at first but after seeing some examples you will understand. First we will look at the Fibonacci seq.
'''


def fib(n):
    if n == 0:  # BASE CASE 1
        return 0
    elif n == 1:  # BASE CASE 2
        return 1
    else:
        return fib(n - 1) + fib(n - 2)  # RECURSIVE STEP SINCE fib CALLS ITSELF


print("     Ex 2.1: The 5th number in the Fibonacci sequence is {}".format(fib(5)))
print("     Ex 2.1: The 10th number in the Fibonacci sequence is {}".format(fib(10)))
print("     Ex 2.1: The 20th number in the Fibonacci sequence is {}".format(fib(20)))



'''
Example 2.2: Recursion - Reverse a String

Another example would be to reverse a string. The base case for string reversal would be 
when you reach the end of the input string.
'''


def reverse(s, i):
    if i == len(s) - 1:
        return s[i]
    else:
        return reverse(s, i+1) + s[i]


print("     Ex 2.2: The string 'abcdef' reversed is '{}'".format(reverse("abcdef", 0)))
print("     Ex 2.2: The string 'I like to run.' reversed is '{}'".format(reverse("I like to run.", 0)))
print("     Ex 2.2: The string 'MATTHEW' reversed is '{}'".format(reverse("MATTHEW", 0)))


'''
Example 2.3: Recursion - Your Turn

Hopefully by now you understand that recursion involves a function calling 
itself in its own code (recursive step) and a specific case to stop recursing 
(base case).

Now you should try to write a recursive function for practice!

Define the factorial function using recursion.
    Example(s):
    
        | input | operation         | output |
        |-------+-------------------+--------|
        | 5     | 5 * 4 * 3 * 2 * 1 | 120    |
        | 4     | 4 * 3 * 2 * 1     | 24     |
        | 3     | 3 * 2 * 1         | 6      |
        | 2     | 2 * 1             | 2      |
        | 1     | 1                 | 1      |
        | 0     | 1                 | 1      |
'''


def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


checkSolutions["example2.3"](factorial)

'''
Now lets get back to the original exercise. Now that you know what recursion is and how the insert 
operation works for a BST, implement the BSTNode class below!
'''


class BSTNode:
    def __init__(self, value):
        self.value = value
        self.right_child = None
        self.left_child = None

    def insert(self, value):
        if value > self.value:
            if self.right_child is None:
                self.right_child = BSTNode(value)
                return self.right_child
            else:
                return self.right_child.insert(value)
        else:
            if self.left_child is None:
                self.left_child = BSTNode(value)
                return self.left_child
            else:
                return self.left_child.insert(value)


checkSolutions["example2"](BSTNode)


'''
Example 3: BST Search

Now lets implement the search method for our BST! 

The search method is very similar to the insert method. Basically you act like 
you are going to insert a new node, but you check if the current node is equal 
to the input value before you recurse. Ill add some sudo code below to help you out.

Definitions:
    current node: S
    right child: r
    left child: l
    value: v

SEARCH(n)
    if S.v equals n, then return True
    else if S.v is greater than n, then
        if S.l exists, then S.l.SEARCH(n)
        else return False
    else if S.v is less than n, then
        if S.r exists, then S.r.SEARCH(n)
        else return False
'''


class BNode:
    def __init__(self, value):
        # pass  # copy your code from the BSTNode class
        self.value = value
        self.right_child = None
        self.left_child = None

    def insert(self, value):
        # pass  # copy your code from the BSTNode class
        if value > self.value:
            if self.right_child is None:
                self.right_child = BNode(value)
                return self.right_child
            else:
                return self.right_child.insert(value)
        else:
            if self.left_child is None:
                self.left_child = BNode(value)
                return self.left_child
            else:
                return self.left_child.insert(value)

    def search(self, value):
        # pass  # implement your search method here
        if value == self.value:
            return True
        elif value > self.value:
            if self.right_child is None:
                return False
            else:
                return self.right_child.search(value)
        else:
            if self.left_child is None:
                return False
            else:
                return self.left_child.search(value)


checkSolutions["example3"](BNode)


'''
Example 4: Effectiveness of BSTs

To measure the effectiveness of BSTs we will look at the time it takes to search them. 

Specifically we will be looking at the worst case time relative to the number of nodes visited 
during a search - this is also called Big O notation, written as O([some function of n here]).

For example, a simple search through a list would have O(n) time because in the worst case the 
number you are looking for does not exist in the list and you must check all n numbers in your 
list before you realize that. Therefore, the upper-bound for this simple search function would be 
n - we right this as O(n).
'''


'''
Example 4.1: Big O simple search

In this example we will show an example of simple search and demonstrate the worst case.
'''


def simple_search(list_in, search_int):
    counter = 0
    for element in list_in:
        counter += 1
        if element == search_int:
            return True, counter
    return False, counter


a = list()
a.append([0 for x in range(10)])
a.append([0 for x in range(15)])
a.append([0 for x in range(38)])
a.append([0 for x in range(45)])
a.append([0 for x in range(54)])
a.append([0 for x in range(63)])
a.append([0 for x in range(72)])
a.append([0 for x in range(87)])
a.append([0 for x in range(99)])

print("     List # | Big-O | List Length (N) | Iterations | Found?")
print("     -------+-------+-----------------+------------+-------")
for idx, el in enumerate(a):
    found, iterations = simple_search(el, 1)
    print("     {: ^6} | {: ^5} | {: ^15} | {: ^10} | {: ^6}"
          .format(idx, "O(N)", len(el), iterations, str(found)))


# Run the code and notice that the number of iterations is always equal to
#   the length of the list input to the search function... this means that
#   this function is of O(N) time complexity


'''
Now lets test our binary search method and see if we get the same numbers.

For this example, use the predefined BST class below.
'''


class BST:
    def __init__(self, value, in_arr=None):
        self.value = value
        self.r = None
        self.l = None
        if in_arr:
            for i in in_arr:
                self.insert(i)

    def insert(self, v):
        if v > self.value:
            if self.r is not None:
                self.r.insert(v)
            else:
                self.r = BST(v)
        else:
            if self.l is not None:
                self.l.insert(v)
            else:
                self.l = BST(v)

    def search(self, v):
        counter = 1
        if v == self.value:
            return True, counter
        elif v > self.value:
            if self.r:
                flag, c = self.r.search(v)
                return flag, counter + c
            else:
                return False, counter
        else:
            if self.l:
                flag, c = self.l.search(v)
                return flag, counter + c
            else:
                return False, counter


# generating some lists to convert to BSTs
a = list()
k = 10
a.append([k/2 + x*(-1)**(x % 2) for x in range(k)])
k = 15
a.append([k + x*(-1)**(x % 2) for x in range(k)])
k = 38
a.append([k/2 + x*(-1)**(x % 2) for x in range(k)])
k = 45
a.append([k + x*(-1)**(x % 2) for x in range(k)])
k = 54
a.append([k/2 + x*(-1)**(x % 2) for x in range(k)])
k = 63
a.append([k + x*(-1)**(x % 2) for x in range(k)])
k = 72
a.append([k/2 + x*(-1)**(x % 2) for x in range(k)])
k = 87
a.append([k + x*(-1)**(x % 2) for x in range(k)])
k = 99
a.append([k/2 + x*(-1)**(x % 2) for x in range(k)])

b = list()
for el in a:
    b.append((BST(el[0], el), len(el)))

print("\n\n      BST # | Big-O | BST Size (N)    | Iterations | Found?")
print("     -------+-------+-----------------+------------+-------")
for idx, el in enumerate(b):
    found, iterations = el[0].search(10000000000)
    print("     {: ^6} | {: ^5} | {: ^15} | {: ^10} | {: ^6}"
          .format(idx, "O(?)", el[1], iterations, str(found)))

# Uncomment the code above and run it...
# You should see that the number of iterations is consistently less than N
#   (the number of nodes in the BST) and that the number is never found

'''
Well, that did not help us figure out what the time complexity (O(?)) is for our 
BST search method... However, we do know that it probably isn't O(N)...

So we need to think about this a little bit differently.

Remember how our searching algorithm works? Each time we visit a node we ask a 
question: is the value we are searching for bigger than or smaller than this node's 
value? The answer to this question determines the direction that we continue 
searching in the BST (right or left). 

So, as I said in the first example, a binary search tree is a data structure that 
allows us to reduce the search space by half after each node we visit. We are able 
to reduce the search space by half because of the question we ask when we visit 
that node (see prev. paragraph). We make this binary BEFORE we visit any more nodes, 
so by doing so we no longer have to look at half of the nodes. An example may be 
easier to understand...

                        a
                       / \
                      b   c

Consider that we are at node a in the tree above and we are searching for "c" using 
alphabetical order to give value to the letters (a=1, b=2, c=3, ... , z=26). So while 
we are at node a there are 2 nodes left to possibly visit. Before visiting either node 
we check to see if a > c or if a < c. After we do this we only ever visit one of the 
two remaining nodes. So each time we make this decision it reduces our search space by 
half. You could also consider it divides by 2 each time. 

So if we start with N nodes then each time we visit a node we are dividing by 2, 
in other words --> ((((N/2)/2)/2)/...)/2 = N/(2^k) where k is the number of nodes 
we visit. SO the time complexity, or the worst case number of iterations, for the 
BST search would be log(N)  (in computer science we assume logs to be base 2).

So BST search would be O(log N) which is BETTER than O(N). These may also be called 
log time and linear time. There are a few more common time complexities, but you can 
always google them if you need to know.
'''


'''
So that was a lot of information that may not seem super useful, however, all of it 
will hopefully help you in some way while you are programming. 

When you are writing or debugging a program, one of the things you will need to 
consider is the speed of your program, especially if you are handling large amounts of 
data. When you do this you may need to examine how that data is stored.

There are many different ways to store data (Google "data structures"), we have introduced
a few in this lecture series including lists and binary search trees. Each have their own
advantages and disadvantages. Now you have some experience with these, so you will 
hopefully be able to make informed decisions about, at the very least, what to research 
and test. 

When you choose an algorithm, check to see if speed is a concern or if memory is a concern 
and choose an algorithm (e.g., search algorithm) that best suites your needs. You can pretty 
much find all of this information on the internet (Stack overflow is your friend). So 
knowing it off the top of your head is pretty much useless, however understanding basically 
what a graph is and what Big-O notation is and how to implement a data structure using 
classes is extremely important.

Regardless of your application this basic programming knowledge will be incredibly important 
for you to have. If you have any questions about this or want to learn more, feel free to 
reach out to us or you can always use the vast resources available online to learn some more 
or get some more practice. 
'''
