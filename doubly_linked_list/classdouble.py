

class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    def add_to_head(self, value):
        new_node = ListNode(value, None, None)
        self.length += 1
        #  If list is currently empty add Node
        #   set the head and tail to equal the new Node
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            # The list already has a node
            # Make new_node next point to new node
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def remove_from_head(self):
        # If Tail There is no node we create a node and point both head and tail to the new node
        pass

    def add_to_tail(self, value):
        pass

    def remove_from_tail(self):
        if self.tail is None:
            return None
        tail_node = self.tail.value
        self.delete(self.tail)
        return tail_node
        pass

    def move_to_front(self, node):
        if node is self.head:
            return

        old_node_value = node.value
        self.delete(node)
        self.add_to_head(old_node_value)

        pass

    def move_to_end(self, node):
        pass

    def delete(self, node):

        # 1. IF the linklist is empty, we do nothing
        if self.head is None and self.tail is None:
            return None
        # 2. IF theres just one Node
        # Check is the head is equal to the tail and if the node is equal to the self.head
        if self.head == self.tail and node == self.head:
            self.head = None
            self.tail = None
            self.length -= 1

        # 3. The node is the head node (We want to handle the head pointer correctly correctly )
        #  check is the node we are trying to remove is the head node
        if self.head == node:
            # MAKE THE HEAD POINT TO THE NEXT VALUE
            # THE REMOVE THE POINTER
            self.head = node.next
            node.delete()

        # 4. The node is the tail node ()
        if self.tail == node:
            self.tail = node.prev
            node.delete()

        else:
            node.delete()

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


class DoublyLinkedListTests(unittest.TestCase):
    def setUp(self):
        self.node = ListNode(1)
        self.dll = DoublyLinkedList(self.node)

    def test_list_remove_from_tail(self):
        self.dll.remove_from_tail()
        self.assertIsNone(self.dll.head)
        self.assertIsNone(self.dll.tail)
        self.assertEqual(len(self.dll), 0)

        self.dll.add_to_tail(33)
        self.assertEqual(self.dll.head.value, 33)
        self.assertEqual(self.dll.tail.value, 33)
        self.assertEqual(len(self.dll), 1)
        self.assertEqual(self.dll.remove_from_tail(), 33)
        self.assertEqual(len(self.dll), 0)

        self.dll.add_to_tail(68)
        self.assertEqual(len(self.dll), 1)
        self.assertEqual(self.dll.remove_from_tail(), 68)
        self.assertEqual(len(self.dll), 0)

    def test_list_remove_from_head(self):
        self.dll.remove_from_head()
        self.assertIsNone(self.dll.head)
        self.assertIsNone(self.dll.tail)
        self.assertEqual(len(self.dll), 0)

        self.dll.add_to_head(2)
        self.assertEqual(self.dll.head.value, 2)
        self.assertEqual(self.dll.tail.value, 2)
        self.assertEqual(len(self.dll), 1)
        self.assertEqual(self.dll.remove_from_head(), 2)
        self.assertEqual(len(self.dll), 0)

        self.dll.add_to_head(55)
        self.assertEqual(len(self.dll), 1)
        self.assertEqual(self.dll.remove_from_head(), 55)
        self.assertEqual(len(self.dll), 0)

    def test_list_add_to_tail(self):
        self.assertEqual(self.dll.tail.value, 1)
        self.assertEqual(len(self.dll), 1)

        self.dll.add_to_tail(30)
        self.assertEqual(self.dll.tail.prev.value, 1)
        self.assertEqual(self.dll.tail.value, 30)
        self.assertEqual(len(self.dll), 2)

        self.dll.add_to_tail(20)
        self.assertEqual(self.dll.tail.prev.value, 30)
        self.assertEqual(self.dll.tail.value, 20)
        self.assertEqual(len(self.dll), 3)

    def test_node_delete(self):
        node_1 = ListNode(3)
        node_2 = ListNode(4)
        node_3 = ListNode(5)

        node_1.next = node_2
        node_2.next = node_3
        node_2.prev = node_1
        node_3.prev = node_2

        node_2.delete()

        self.assertEqual(node_1.next, node_3)
        self.assertEqual(node_3.prev, node_1)

    def test_node_insert_before(self):
        self.node.insert_before(0)
        self.assertEqual(self.node.prev.value, 0)

    def test_list_add_to_head(self):
        self.assertEqual(self.dll.head.value, 1)

        self.dll.add_to_head(10)
        self.assertEqual(self.dll.head.value, 10)
        self.assertEqual(self.dll.head.next.value, 1)
        self.assertEqual(len(self.dll), 2)

    def test_node_insert_after(self):
        self.node.insert_after(2)
        self.assertEqual(self.node.next.value, 2)

    def test_list_move_to_end(self):
        self.dll.add_to_head(40)
        self.assertEqual(self.dll.tail.value, 1)
        self.assertEqual(self.dll.head.value, 40)

        self.dll.move_to_end(self.dll.head)
        self.assertEqual(self.dll.tail.value, 40)
        self.assertEqual(self.dll.tail.prev.value, 1)
        self.assertEqual(len(self.dll), 2)

        self.dll.add_to_tail(4)
        self.dll.move_to_end(self.dll.head.next)
        self.assertEqual(self.dll.tail.value, 40)
        self.assertEqual(self.dll.tail.prev.value, 4)
        self.assertEqual(len(self.dll), 3)

    def test_list_move_to_front(self):
        self.dll.add_to_tail(3)
        self.assertEqual(self.dll.head.value, 1)
        self.assertEqual(self.dll.tail.value, 3)

        self.dll.move_to_front(self.dll.tail)
        self.assertEqual(self.dll.head.value, 3)
        self.assertEqual(self.dll.head.next.value, 1)
        self.assertEqual(len(self.dll), 2)

        self.dll.add_to_head(29)
        self.dll.move_to_front(self.dll.head.next)
        self.assertEqual(self.dll.head.value, 3)
        self.assertEqual(self.dll.head.next.value, 29)
        self.assertEqual(len(self.dll), 3)

    def test_list_delete(self):
        self.dll.delete(self.node)
        self.assertIsNone(self.dll.head)
        self.assertIsNone(self.dll.tail)
        self.assertEqual(len(self.dll), 0)

        self.dll.add_to_tail(1)
        self.dll.add_to_head(9)
        self.dll.add_to_tail(6)

        self.dll.delete(self.dll.head)
        self.assertEqual(self.dll.head.value, 1)
        self.assertEqual(self.dll.tail.value, 6)
        self.assertEqual(len(self.dll), 2)

        self.dll.delete(self.dll.head)
        self.assertEqual(self.dll.head.value, 6)
        self.assertEqual(self.dll.tail.value, 6)
        self.assertEqual(len(self.dll), 1)

    def test_get_max(self):
        self.assertEqual(self.dll.get_max(), 1)
        self.dll.add_to_tail(100)
        self.assertEqual(self.dll.get_max(), 100)
        self.dll.add_to_tail(55)
        self.assertEqual(self.dll.get_max(), 100)
        self.dll.add_to_tail(101)
        self.assertEqual(self.dll.get_max(), 101)


# if __name__ == '__main__':
#     unittest.main()
