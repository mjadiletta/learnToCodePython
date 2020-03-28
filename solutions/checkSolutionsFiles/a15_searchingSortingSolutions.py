class searchingSortingSolutions:
    def __init__(self):
        self.searchingSortingSol = dict()
        self.searchingSortingSol['example1'] = self.ex1
        self.searchingSortingSol['example2.3'] = self.ex2_3
        self.searchingSortingSol['example2'] = self.ex2

    def ex1(self, n):
        correct = True

        if not (n.value == 50):
            correct = False
            print("Example 1: Incorrect Solution")
            print("     Why did you edit the root node?")
        elif not (n.left_child.value == 25):
            correct = False
            print("Example 1: Incorrect Solution")
            print("     Why did you edit the node 25?")
        elif not (n.right_child.value == 75):
            correct = False
            print("Example 1: Incorrect Solution")
            print("     Why did you edit the node 75?")
        elif not (n.left_child.left_child.value == 1):
            correct = False
            print("Example 1: Incorrect Solution")
            print("     Node 1 was added in the wrong order")
        elif not (n.left_child.right_child.value == 40):
            correct = False
            print("Example 1: Incorrect Solution")
            print("     Node 40 was added in the wrong order")
        elif not (n.left_child.right_child.left_child.value == 35):
            correct = False
            print("Example 1: Incorrect Solution")
            print("     Node 35 was added in the wrong order")
        elif not (n.right_child.left_child.value == 60):
            correct = False
            print("Example 1: Incorrect Solution")
            print("     Node 60 was added in the wrong order")
        elif not (n.right_child.right_child.value == 90):
            correct = False
            print("Example 1: Incorrect Solution")
            print("     Node 90 was added in the wrong order")
        elif not (n.right_child.left_child.right_child.value == 65):
            correct = False
            print("Example 1: Incorrect Solution")
            print("     Node 65 was added in the wrong order")
        elif not (n.right_child.right_child.left_child.value == 80):
            correct = False
            print("Example 1: Incorrect Solution")
            print("     Node 80 was added in the wrong order")
        elif correct:
            print("Example 1: Correct Solution")
        else:
            print("Example 1: Incorrect Solution")

    def ex2_3(self, f):
        if f(20) == 2432902008176640000:
            print("Example 2.3: Correct Solution")
        else:
            print("Example 2.3: Incorrect Solution")

    def ex2(self, n):
        correct = True
        root = n(23)
        root.insert(4)
        root.insert(44)
        root.insert(2)
        root.insert(23)
        root.insert(42)
        root.insert(43)
        if not (root.value == 23):
            correct = False
            print("Example 2: Incorrect Solution")
            print("     Check your constructor implementation")
        if not (root.left_child.value == 4):
            correct = False
            print("Example 2: Incorrect Solution")
            print("     Check your base case(s) for your insert method")
        elif not (root.right_child.value == 44):
            correct = False
            print("Example 2: Incorrect Solution")
            print("     Check your base case(s) for your insert method")
        elif not (root.right_child.left_child.value == 42):
            correct = False
            print("Example 2: Incorrect Solution")
            print("     Check your recursive step(s) for your insert method")
        elif not (root.left_child.right_child.value == 23):
            correct = False
            print("Example 2: Incorrect Solution")
            print("     Check your base case(s) conditions (>, <=) for your insert method")
        elif not (root.right_child.left_child.right_child.value == 43):
            correct = False
            print("Example 2: Incorrect Solution")
            print("     Check your recursive step(s) for your insert method")
        elif not (root.right_child.value == 44):
            correct = False
            print("Example 2: Incorrect Solution")
            print("     Check your base case(s) for your insert method")
        elif correct:
            print("Example 2: Correct Solution")
        else:
            print("Example 2: Incorrect Solution")


