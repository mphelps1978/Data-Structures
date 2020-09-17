
class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next_node(self):
        return self.next_node

    def set_next_node(self, new_next):
        self.next_node = new_next


class LinkedList:
    def __init__(self):
        # what attributes do we need?
        self.head = None
        self.tail = None

    def add_to_head(self, value):
        # create new node
        # set the next_node of my new node to the head
        # update the head attribute

        new_node = Node(value)
        if self.head is None:  # if there's no nodes
            # update head and tail attributes
            self.head = new_node
            self.tail = new_node
        else:
            new_node.set_next_node(self.head)
            self.head = new_node

    def add_to_tail(self, value):
        # create new node
        new_node = Node(value)

        # if the list is empty
        # update head and tail attributes
        if self.head is None:
            self.head = new_node
            self.tail = new_node

        # otherwise the list is not empty
        else:
            # update next_node of tail
            # update self.tail
            self.tail.set_next_node(new_node)
            self.tail = new_node

    def remove_head(self):
        # empty list, we just need to return none
        if self.head is None:
            return None

        # otherwise, get the value of old head and store it
        else:
            ret_value = self.head.get_value()

            # if the list has 1 node
            # set the head and tail to none
            if self.head == self.tail:
                self.head = None
                self.tail = None

            # list with 2+ nodes
            else:
                # move the head to the next node
                self.head = self.head.get_next_node()
            # return the value of the OLD head
            return ret_value

    def remove_tail(self):
        """
        Remove last node
        (Head)1 -> 2 -> 3(Tail)
        (Head)1 -> 2(Tail)
        """
        # if we have an empty linked list
        if self.head is None:
            return None
        else:

            # if the list has 1 node, set head and tail to 'none'
            ret_value = self.tail.get_value()
            if self.head == self.tail:
                self.head = None
                self.tail = None

            # if we have 2 or more nodes
            # we have to start at the head and move down the linked list
            # until we get to the node right before the tail
            # iterate over our linked list
            else:
                pre = self.head
                temp = self.head.next_node
                while temp.next_node is not None:
                    pre = pre.next_node
                pre.next_node = None
                self.tail = pre
            return ret_value

        # print(f'New Tail is {self.tail.get_value()}') <-- debugging

    def contains(self, value):
        # loop through list until next pointer is none
        # if the value is the target return true
        # return false

        cur_node = self.head
        while cur_node is not None:
            if cur_node.get_value() == value:
                return True

        return False

    def get_max(self):
        # TODO time permitting
        pass


"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order.

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when
   implementing a Queue?

Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""


# class Queue:  # array
#     def __init__(self):
#         self.size = 0
#         self.storage = []

#     def __len__(self):
#         return self.size

#     def enqueue(self, value):
#         self.size += 1
#         return self.storage.append(value)

#     def dequeue(self):
#         if self.size > 0:
#             self.size -= 1
#             return self.storage.pop(0)
#         else:
#             return

class Queue:  # LL
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def __len__(self):
        return self.size

    def enqueue(self, value):
        self.size += 1
        return self.storage.add_to_tail(value)

    def dequeue(self):
        if self.size > 0:
            self.size -= 1
            return self.storage.remove_head()
        else:
            return
