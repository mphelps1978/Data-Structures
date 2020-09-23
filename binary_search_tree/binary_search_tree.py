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
    # value comparison
    # if there's nothing to the left or right, we've reached the bottom and can insert
    # (dupes to right)
    def insert(self, value):

        # RECURSIVE

        # if value is <  root
        if value < self.value:
            # to the left we go
            if self.left:  # if there's a left hand node,
                self.left.insert(value)  # recursive call, start the process over again at the left node
            else:
                # there's nothing to the left, so we can insert
                self.left = BSTNode(value)

        # if value is > root
        elif value > self.value:
            # to the right we go
            if self.right:  # there is a right side node
                self.right.insert(value)  # recursive call - start the process over again with the current node
            else:
                # Nothing to the right, so insert
                self.right = BSTNode(value)

        elif value == self.value:  # dupliicates to the right
            if not self.right:  # if there's nothing already to the right
                # we can insert it here
                self.right = BSTNode(value)
            else:
                # we need to make that call again
                self.right.insert(value)

        return self

    # Return True if the tree contains the value
    # False if it does not

    def contains(self, target):
        # check if self.value is target
        # if yes return true
        if self.value == target:
            return True

        if target > self.value:
            # go right
            if not self.right:  # if there's no right hand node, our target isn't in the BST
                return False
            else:
                return self.right.contains(target)  # Recursive call - start over again with the right hand node

        if target < self.value:
            # to the left we go
            if not self.left:  # if there's no left hand node, our target isn't in the BST
                return False
            else:
                return self.left.contains(target)  # recursive call - start over again with the left hand node

    # Return the maximum value found in the tree

    def get_max(self):
        # go right until you can't anymore
        # return value of far right
        pass

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        # one side then the other
        # call the function on every value in the tree
        pass

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal

    def in_order_print(self):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self):
        pass

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self):
        pass


# """
# This code is necessary for testing the `print` methods
# """
# bst = BSTNode(1)

# bst.insert(8)
# bst.insert(5)
# bst.insert(7)
# bst.insert(6)
# bst.insert(3)
# bst.insert(4)
# bst.insert(2)

# bst.bft_print()
# bst.dft_print()

# print("elegant methods")
# print("pre order")
# bst.pre_order_dft()
# print("in order")
# bst.in_order_dft()
# print("post order")
# bst.post_order_dft()
