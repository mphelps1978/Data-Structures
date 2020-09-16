# TODO a class that represents the individual elements in our LL

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
        if self.tail is None:  # empty list
            return None

        elif self.head == self.tail:  # only one node
            old_tail = self.tail
            self.head = None
            self.tail = None
            return old_tail

        else:  # more than one node
            current = self.head
            new_tail = current
            while current is not self.tail:
                new_tail = current
                current = current.next_node
            self.tail = new_tail
            self.tail.set_next_node(None)

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
