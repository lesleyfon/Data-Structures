"""
Binary search trees are a data structure that enforce an ordering over
the data they store. That ordering in turn makes it a lot more efficient
at searching for a particular piece of data in the tree.

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
import random


class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BSTNode(value)
            else:
                self.left.insert(value)
        if value > self.value:
            if self.right is None:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)
        pass
    # Return True if the tree contains the value
    # False if it does not

    def contains(self, target):
        if self.value == target:
            return True

        found = False

        if self.value >= target:

            if self.left is None:
                return False
            found = self.left.contains(target)

        if self.value < target:

            if self.right is None:
                return False
            found = self.right.contains(target)

        return found
        pass

    # Return the maximum value found in the tree
    def get_max(self):

        if self.right is None:
            return self.value
        return self.right.get_max()
    # Call the function `fn` on the value of each nodex

    def for_each(self, fn):
        fn(self.value)

        if self.left:
            fn(self.left.value)
            self.left.for_each(fn)

        if self.right:
            fn(self.right.value)
            self.right.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal

    def in_order_print(self, node):
        # DFS
        # DFS
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass


def test_insert():
    bst = BSTNode(5)
    bst.insert(2)
    bst.insert(3)
    bst.insert(7)
    bst.insert(6)
    print(bst.left.right.value, 3)
    print(bst.right.left.value, 6)


test_insert()


def test_contains():
    bst = BSTNode(5)
    bst.insert(2)
    bst.insert(3)
    bst.insert(7)
    print(bst.contains(7), True)
    print(bst.contains(8), False)


test_contains()


def test_get_max():
    bst = BSTNode(5)
    print(bst.get_max(), 5)
    bst.insert(30)
    print(bst.get_max(), 30)
    bst.insert(300)
    bst.insert(3)
    print(bst.get_max(), 300)


test_get_max()


def test_for_each():

    bst = BSTNode(5)
    arr = []
    def cb(x): return arr.append(x)

    v1 = random.randint(1, 101)
    v2 = random.randint(1, 101)
    v3 = random.randint(1, 101)
    v4 = random.randint(1, 101)
    v5 = random.randint(1, 101)

    bst.insert(v1)
    bst.insert(v2)
    bst.insert(v3)
    bst.insert(v4)
    bst.insert(v5)

    bst.for_each(cb)

    print(5 in arr)
    print(v1 in arr)
    print(v2 in arr)
    print(v3 in arr)
    print(v4 in arr)
    print(v5 in arr)


test_for_each()
