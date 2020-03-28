"""
Practice Group 15: File Organization and Separation
Created: 3/__/2020

In this tutorial we will cover a common use of OOP to create a "graph."

You may have heard of a binary search tree, or a heap, these are both
considered graphs in computer science. A graph is basically a collection
of nodes and edges. Nodes hold data and edges are the connections or paths
between nodes. OOP is a great way to implement different data structures,
including graphs. In this lecture you will be implementing a binary search
tree, a linked list, and a heap. This will give you a TON of practice
applying the OOP techniques you have learned, while also learning some new
sorting and searching algorithms and data structures.

Learning Objectives:
    1. Create a binary search tree using the node class
    2. Use the binary search tree and learn about its effectiveness
    3. Create a linked list and test some of your list sorting algorithms
    4. Create a heap
    5. Implement heap sort

"""

import numpy as np
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
        if value >= self.value:
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
                return self.right_child.add_child(value)


# we want a tree with the following numbers: 5, 23, 54, 63, 22, 17, 89, 100, 90, 3, 1 added to it
# I will start you off with the root node and one child node
# It is your job to add the rest of the nodes to the tree

root = Node(50)
root.add_child(25)

# SOLUTION BEGIN - DELETE
root.add_child(5)
root.add_child(23)
root.add_child(54)
root.add_child(63)
root.add_child(22)
root.add_child(17)
root.add_child(89)
root.add_child(100)
root.add_child(90)
root.add_child(3)
root.add_child(1)
# SOLUTION END - DELETE



'''
Example 2: BST Search

Now that you have created a BST, lets develop the search algorithm for it!


'''

class Node:
    def __init__(self):

