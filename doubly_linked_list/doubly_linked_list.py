"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next

    # Done in class
    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""
Our doubly-linked list class. It holds references to
the list's head and tail nodes.
"""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """
    Wraps the given value in a ListNode and inserts it
    as the new head of the list. Don't forget to handle
    the old head node's previous pointer accordingly.
    """

    def add_to_head(self, value):
        # create new node
        new_node = ListNode(value, None, None)
        # add to empty list
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
            self.length += 1

        # add to non-empty list
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            self.length += 1

    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """

    def remove_from_head(self):
        # if the node isn't the head
        if not self.head:
            return None

        # if there's only one node
        elif self.length == 1:
            old_head = self.head
            self.head = None
            self.tail = None
            self.length -= 1
            return old_head.value

        # otherwise
        else:
            old_head = self.head
            new_head = self.head.next
            new_head.prev = None
            self.head = new_head
            self.length -= 1
            return old_head.value

    """
    Wraps the given value in a ListNode and inserts it
    as the new tail of the list. Don't forget to handle
    the old tail node's next pointer accordingly.
    """

    def add_to_tail(self, value):
        # let's create the new node first and update our list length
        new = ListNode(value, None, None)
        self.length += 1

        # if the list is empty
        if not self.head and not self.tail:
            self.head = new
            self.tail = new

        # otherwise the list has stuff in it, so let's add the new node to the tail
        else:
            # new node previous pointer to current tail
            new.prev = self.tail
            # current tail's next pointer to new node
            self.tail.next = new
            # move tail to new node
            self.tail = new

    """
    Removes the List's current tail node, making the
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """

    def remove_from_tail(self):
        # if there's more than one node
        if self.length > 1:
            old_tail = self.tail
            new_tail = self.tail.prev
            self.tail.prev = None
            self.tail = new_tail
            self.length -= 1
            return old_tail.value

        # if there's only one node
        elif self.length == 1:
            old_tail = self.tail
            self.tail = None
            self.head = None
            self.length -= 1
            return old_tail.value

        # empty list
        else:
            return None

    """
    Removes the input node from its current spot in the
    List and inserts it as the new head node of the List.
    """

    def move_to_front(self, node):
        # Delete node from current position
        # add_to_head passing the node's value
        self.delete(node)
        self.add_to_head(node.value)

    """
    Removes the input node from its current spot in the
    List and inserts it as the new tail node of the List.
    """

    def move_to_end(self, node):
        # delete node from current position
        # add_to_tail passing in node's value
        self.delete(node)
        self.add_to_tail(node.value)

    """
    Deletes the input node from the List, preserving the
    order of the other elements of the List.
    """

    def delete(self, node):
        # Don't need to return value
        # Do need to update head and tail

        # Empty List
        if self.length == 1:
            self.head = None
            self.tail = None
            self.length = 0

        # if it's the head
        elif node == self.head:
            self.remove_from_head()

        # if it's the tail
        elif node == self.tail:
            self.remove_from_tail()

        # otherwise it's somewhere in the middle, so we need to update the pointers
        else:
            next_node = node.next
            prev_node = node.prev
            prev_node.next = next_node
            next_node.prev = prev_node
            self.length -= 1

    """
    Finds and returns the maximum value of all the nodes
    in the List.
    """

    def get_max(self):
        # if the list has something in it
        # define a current max value
        # loop through the list, and compare max value to current value
        # update max value as needed
        if self.length > 0:
            max_value = self.head.value
            current = self.head
            while current.next is not None:
                if current.value > max_value:
                    max_value = current.value
                current = current.next
            if max_value > current.value:
                return max_value
            else:
                return current.value

        # if the list is empty
        else:
            return None
