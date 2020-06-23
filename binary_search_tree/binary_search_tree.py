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


class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # Create a node is there is no node in the tree
        if self.value is None:
            self.value = BSTNode(value)

        else:
            # If there is a node then we want to do a couple of checks to determine where to add the node.

            # Check if the value of the node is greater than the root node or less than the root node
            # If it is less than the root node we want to make sure we are creating a node on the left side of the tree.

            if value < self.value:
                # Check to see if there is a node on the left side of the tree already.
                # If so then we want to recursively call the self.insert method to go over this process again to continously determine where to add the value as a node
                if self.left:
                    # The recursive function
                    self.left.insert(value)
                else:
                    # There is no value and we want to create a node and add it to the left side of the tree
                    self.left = BSTNode(value)
                pass
            else:
                # Else the value is greater than or equal to the root node so we want to create the node on the right  side of the tree
                if self.right:
                    self.right.insert(value)
                else:
                    self.right = BSTNode(value)

        pass

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value is None:
            return False
        else:
            # Create a variable that will keep track of the what we want to return.

            if target < self.value:
                # If the target is less than the current node value we want to discard the right side of the tree and search only on the left side
                left_node = self.left
                # Now we are looking at the next node. If the node is truthy then we want to do some checks and see if the value is in the left side of the node
                if left_node:
                    # Check is left_node.value is equal to the current target then we return true else we call call contains again to go over this process recursively
                    if left_node.value == target:
                        return True
                    else:
                        left_node.contains(target)
                else:
                    # That means we didn't find a match and we want to return false
                    return False
            else:
                # The target is greater than the root node value and we want to check on the right side of the tree
                right_node = self.right
                # If the right node is true then we want to essentially do some work
                if right_node:
                    # That means we have found a match and we want we return true
                    if right_node.value == target:
                        return True
                    else:
                        # call the function recursively and keep checking until we have exhausted all our options
                        right_node.contains(target)
                    pass
                else:
                    # else we have hit the leaf node and want to just return false
                    return False

        pass

    # Return the maximum value found in the tree
    def get_max(self):
        pass

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        pass

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
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
