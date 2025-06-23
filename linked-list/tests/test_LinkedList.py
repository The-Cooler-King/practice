import unittest

import sys
import os

# this line modifies sys.path inside of the test files and is necessary to import our code files without turning them into a package
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from LinkedList import LinkedList


class TestLinkedList(unittest.TestCase):

    def test_list_initialization(self):
        # Arrange
        test_list = LinkedList()

        # Assert
        self.assertEqual(repr(test_list), "Empty List")

    def test_head(self):
        # Arrange
        test_list = LinkedList()
        test_list.prepend("A")

        # Act
        head_node = test_list.head()

        # Assert
        self.assertEqual(head_node.value, "A")
        self.assertIsNone(head_node.next)

    def test_head_empty_list(self):
        # Arrange
        test_list = LinkedList()

        # Act
        head_node = test_list.head()

        # Assert
        self.assertIsNone(head_node)

    def test_list_is_empty(self):
        # Arrange
        test_list = LinkedList()

        # Assert
        self.assertTrue(test_list.is_empty())

    def test_list_is_not_empty(self):
        # Arrange
        test_list = LinkedList()
        test_list.prepend(5)

        # Assert
        self.assertFalse(test_list.is_empty())

    def test_rebuild_index_map(self):
        # Arrange
        test_list = create_list_from_values(["D", "C", "B", "A"])

        # Act
        test_list.rebuild_index_map()

        # Assert
        self.assertEqual(test_list._index_map[0].value, "A")
        self.assertEqual(test_list._index_map[1].value, "B")
        self.assertEqual(test_list._index_map[2].value, "C")
        self.assertEqual(test_list._index_map[3].value, "D")

    def test_rebuild_index_map_empty_list(self):
        # Arrange
        test_list = create_list_from_values([])

        # Act
        test_list.rebuild_index_map()

        # Assert
        with self.assertRaises(KeyError) as context:
            test_list._index_map[0]

    def test_prepend_to_empty_list(self):
        # Arrange
        test_list = LinkedList()

        # Act
        test_list.prepend(5)

        # Assert
        self.assertEqual(repr(test_list), "LinkedList([5])")

    def test_prepend_to_list(self):
        # Arrange
        test_list = LinkedList()
        test_list.prepend(5)
        original_node = test_list._head

        # Act
        test_list.prepend(6)

        # Assert
        self.assertEqual(repr(test_list), "LinkedList([6 -> 5])")

    def test_pop_node_from_empty_list(self):
        # Arrange
        test_list = create_list_from_values([])

        # Act
        pop_value = test_list.pop()

        # Assert
        self.assertIsNone(pop_value)
        self.assertEqual(repr(test_list), "Empty List")

    def test_pop_node_from_single_node_list(self):
        # Arrange
        test_list = create_list_from_values([1])

        # Act
        pop_value = test_list.pop()

        # Assert
        self.assertEqual(pop_value, 1)
        self.assertEqual(repr(test_list), "Empty List")

    def test_pop_node_from_two_node_list(self):
        # Arrange
        test_list = create_list_from_values([1, 2])

        # Act
        pop_value = test_list.pop()

        # Assert
        self.assertEqual(pop_value, 1)
        self.assertEqual(repr(test_list), "LinkedList([2])")

    def test_pop_node_from_multiple_node_list(self):
        # Arrange
        test_list = create_list_from_values([1, 2, 3, 4])

        # Act
        pop_value = test_list.pop()

        # Assert
        self.assertEqual(pop_value, 1)
        self.assertEqual(repr(test_list), "LinkedList([4 -> 3 -> 2])")

    def test_iterating_over_list(self):
        # Arrange
        test_list = create_list_from_values(["S", "S", "E", "C", "C", "U", "S"])

        # Act
        result = ""
        for node_value in test_list:
            result += str(node_value)

        # Assert
        self.assertEqual(result, "SUCCESS")

    def test_iterating_over_empty_list(self):
        # Arrange
        test_list = create_list_from_values([])

        # Act
        result = ""
        for node_value in test_list:
            result += str(node_value)

        # Assert
        self.assertEqual(result, "")

    def test_iterating_over_cyclical_list(self):
        # Arrange
        test_list = create_list_from_values(["B", "A"])
        test_list._head.next.next = test_list._head  # set node "B" next to node "A"

        # Act & Assert
        with self.assertRaises(RuntimeError) as context:
            result = ""
            for node_value in test_list:
                result += str(node_value)

        self.assertEqual(str(context.exception), "Cannot iterate over a cyclic linked list")

    def test_repr_list(self):
        # Arrange
        test_list = create_list_from_values([1, 2, 3, 4])

        # Assert
        self.assertEqual(repr(test_list), "LinkedList([4 -> 3 -> 2 -> 1])")

    def test_repr_empty_list(self):
        # Arrange
        test_list = create_list_from_values([])

        # Assert
        self.assertEqual(repr(test_list), "Empty List")

    def test_repr_list_with_cycle(self):
        # Arrange
        test_list = create_list_from_values(["G", "F", "E", "D", "C", "B", "A"])
        # traverse list and to get node "B" and node "G"
        current_node = test_list._head
        while current_node:
            if current_node.value == "B":
                node_B = current_node

            if current_node.value == "G":
                node_G = current_node

            current_node = current_node.next

        node_G.next = node_B  # set node "G" next to node "B"

        # Assert
        self.assertEqual(repr(test_list), "LinkedList([A -> B -> C -> D -> E -> F -> G -> B ... (cycle detected)])")

    def test_has_cycle_empty_list(self):
        # Arrange
        test_list = LinkedList()

        # Act & Assert
        self.assertFalse(test_list.has_cycle())

    def test_has_cycle_single_node_list_no_cycle(self):
        # Arrange
        test_list = LinkedList()
        test_list.prepend("A")

        # Act & Assert
        self.assertFalse(test_list.has_cycle())

    def test_has_cycle_single_node_list_with_cycle(self):
        # Arrange
        test_list = LinkedList()
        test_list.prepend("A")
        test_list._head.next = test_list._head  # set head equal to itself. single node loop

        # Act & Assert
        self.assertTrue(test_list.has_cycle())

    def test_has_cycle_two_node_list_no_cycle(self):
        # Arrange
        test_list = create_list_from_values(["B", "A"])

        # Act & Assert
        self.assertFalse(test_list.has_cycle())

    def test_has_cycle_two_node_list_with_cycle(self):
        # Arrange
        test_list = create_list_from_values(["B", "A"])
        test_list._head.next.next = test_list._head  # set node "B" next to node "A"

        # Act & Assert
        self.assertTrue(test_list.has_cycle())

    def test_has_cycle_multi_node_list_no_cycle(self):
        # Arrange
        test_list = create_list_from_values(["G", "F", "E", "D", "C", "B", "A"])

        # Act & Assert
        self.assertFalse(test_list.has_cycle())

    def test_has_cycle_multi_node_list_with_cycle(self):
        # Arrange
        test_list = create_list_from_values(["G", "F", "E", "D", "C", "B", "A"])
        # traverse list and to get node "B" and node "G"
        current_node = test_list._head
        while current_node:
            if current_node.value == "B":
                node_b = current_node

            if current_node.value == "G":
                node_g = current_node

            current_node = current_node.next

        node_g.next = node_b  # set node "G" next to node "B"

        # Act & Assert
        self.assertTrue(test_list.has_cycle())

    def test_find_middle_empty_list(self):
        # Arrange
        test_list = create_list_from_values([])

        # Act & Assert
        with self.assertRaises(RuntimeError) as context:
            test_list.find_middle()

        self.assertEqual(str(context.exception), "Cannot find the middle of an empty list")

    def test_find_middle_cyclical_list(self):
        # Arrange
        test_list = create_list_from_values(["B", "A"])
        test_list._head.next.next = test_list._head  # set node "B" next to node "A"

        # Act & Assert
        with self.assertRaises(RuntimeError) as context:
            test_list.find_middle()

        self.assertEqual(str(context.exception), "Cannot find the middle of a cyclical linked list")

    def test_find_middle_even_node_list(self):
        # Arrange
        test_list = create_list_from_values(["F", "E", "D", "C", "B", "A"])

        # Act
        middle_node_value = test_list.find_middle()

        # Assert
        self.assertEqual(middle_node_value, "D")

    def test_find_middle_odd_node_list(self):
        # Arrange
        test_list = create_list_from_values(["I", "H", "G", "F", "E", "D", "C", "B", "A"])

        # Act
        middle_node_value = test_list.find_middle()

        # Assert
        self.assertEqual(middle_node_value, "E")

    def test_reverse_full_list(self):
        # Arrange
        test_list = create_list_from_values(["I", "H", "G", "F", "E", "D", "C", "B", "A"])

        # Act
        test_list.reverse()

        # Assert
        self.assertEqual(repr(test_list), "LinkedList([I -> H -> G -> F -> E -> D -> C -> B -> A])")

    def test_reverse_single_node_list(self):
        # Arrange
        test_list = create_list_from_values(["A"])

        # Act
        test_list.reverse()

        # Assert
        self.assertEqual(repr(test_list), "LinkedList([A])")

    def test_reverse_empty_list(self):
        # Arrange
        test_list = create_list_from_values([])

        # Act
        test_list.reverse()

        # Assert
        self.assertEqual(repr(test_list), "Empty List")

    def test_reverse_cyclical_list(self):
        # Arrange
        test_list = create_list_from_values(["B", "A"])
        test_list._head.next.next = test_list._head  # set node "B" next to node "A"

        # Act & Assert
        with self.assertRaises(RuntimeError) as context:
            test_list.reverse()

        self.assertEqual(str(context.exception), "Cannot reverse a cyclical linked list")


###### HELPER FUNCTIONS ######
def create_list_from_values(values):
    linked_list = LinkedList()
    for value in values:
        linked_list.prepend(value)
    return linked_list
