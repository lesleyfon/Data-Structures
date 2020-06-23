"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""

    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""

    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""

    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """Wraps the given value in a ListNode and inserts it
    as the new head of the list. Don't forget to handle
    the old head node's previous pointer accordingly."""

    def add_to_head(self, value):

        new_head_node = ListNode(value)
        if self.head is None:

            self.head = new_head_node
            self.tail = new_head_node
            self.length += 1
        else:

            new_head_node.next = self.head
            self.head = new_head_node
            self.length += 1

    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""

    def remove_from_head(self):

        if self.head is None:
            self.head = None
            self.tail = None
            return None

        old_head_value = self.head.value
        if self.head.next is None:
            self.length -= 1
            self.head = None
            self.tail = None

        if self.head is not None:
            self.length -= 1
            self.head = self.head.next

        return old_head_value

    """Wraps the given value in a ListNode and inserts it
    as the new tail of the list. Don't forget to handle
    the old tail node's next pointer accordingly."""

    def add_to_tail(self, value):
        self.length += 1
        if self.head is None:
            self.head = ListNode(value)
            self.tail = ListNode(value)
        else:
            self.tail.insert_after(value)
            self.tail = self.tail.next

    """Removes the List's current tail node, making the
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""

    def remove_from_tail(self):

        if self.tail:

            if self.tail is None:
                self.tail = None
                self.tail = None
                return None

            old_tail_value = self.tail.value
            if self.tail.prev is not None:
                self.length -= 1
                self.tail = None
                self.head = None

            if self.tail is not None:
                self.length -= 1
                self.tail = self.tail.prev

            return old_tail_value

    """Removes the input node from its current spot in the
    List and inserts it as the new head node of the List."""

    def move_to_front(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            ddl = self.head
            while True:
                if ddl == node:
                    ddl.delete()
                    self.head = node
                    self.head.next = ddl
                    ddl.prev = self.head
                    break
                else:
                    ddl = ddl.next

    """Removes the input node from its current spot in the
    List and inserts it as the new tail node of the List."""

    def move_to_end(self, node):
        pass

    """Removes a node from the list and handles cases where
    the node was the head or the tail"""

    def delete(self, node):
        pass
    """Returns the highest value currently in the list"""

    def get_max(self):
        if self.head is None:
            return None

        # If theres no next Node return the head nodes value
        if self.head.next is None:
            return self.head.value

        # Asign the head node to a variable called node
        # Create a var to hold the largest value
        node = self.head
        largest_value = 0

        # loop through the list
        while node is not None:
            # if the node value is greater than the previous largest number assign the node value to the largest number
            if node.value > largest_value:
                largest_value = node.value
            node = node.next

        # Return the largest number once the loop is done
        return largest_value


node = ListNode(1)
dll = DoublyLinkedList(node)
dll.remove_from_tail()
print(dll.head)
print(dll.tail)
print(len(dll), 0)


print(dir(dll))
dll.add_to_tail(33)


print(dll.head.value, 33)
print(dll.tail.value, 33)
print(len(dll), 1)
print(dll.remove_from_tail(), 33)
print(len(dll), 0)

dll.add_to_tail(68)
print(len(dll), 1)
print(dll.remove_from_tail(), 68)
print(len(dll), 0)
