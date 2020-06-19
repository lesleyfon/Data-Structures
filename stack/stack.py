"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order.

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when
   implementing a Stack?
"""


# class Stack:
#     def __init__(self):
#         self.size = 0
#         self.storage = []

#     def __len__(self):

#         return self.size

#     def push(self, value):
#         self.size += 1
#         self.size += 1
#         self.storage.insert(0, value)

#     def pop(self):
#         popped_value = None
#         if len(self.storage) >= 1:
#             self.size -= 1
#             popped_value = self.storage.pop(0)

#         return popped_value


class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node


class Stack:
    def __init__(self):
        self.size = 0
        self.head = None
        self.tail = None

    def __len__(self):
        return self.size

    def push(self, value):
        self.size += 1
        new_node = Node(value)
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next_node = self.head
            self.head = new_node

    def pop(self):

        popped_value = None
        if self.head is None:
            print(popped_value)
            return popped_value
        else:
            self.size -= 1
            popped_value = self.head.value
            self.head = self.head.next_node
            print(popped_value)
            return popped_value
