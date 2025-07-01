import unittest

import sys
import os

# this line modifies sys.path inside of the test files and is necessary to import our code files without turning them into a package
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from SinglyLinkedList import SinglyLinkedList
from Node import Node


class TestLinkedList(unittest.TestCase):

    def test_list_initialization(self):
        # Arrange
        test_list = SinglyLinkedList()

        # Assert
        self.assertEqual(repr(test_list), "LinkedList([])")

    def test_prepend_to_empty_list(self):
        # Arrange
        test_list = SinglyLinkedList()

        # Act
        test_list.prepend(5)

        # Assert
        self.assertEqual(repr(test_list), "LinkedList([5])")

    def test_prepend_to_list(self):
        # Arrange
        test_list = SinglyLinkedList()
        test_list.prepend(5)

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
        self.assertEqual(repr(test_list), "LinkedList([])")

    def test_pop_node_from_single_node_list(self):
        # Arrange
        test_list = create_list_from_values([1])

        # Act
        pop_value = test_list.pop()

        # Assert
        self.assertEqual(pop_value, 1)
        self.assertEqual(repr(test_list), "LinkedList([])")

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

    def test_repr_list(self):
        # Arrange
        test_list = create_list_from_values([1, 2, 3, 4])

        # Assert
        self.assertEqual(repr(test_list), "LinkedList([4 -> 3 -> 2 -> 1])")

    def test_repr_empty_list(self):
        # Arrange
        test_list = create_list_from_values([])

        # Assert
        self.assertEqual(repr(test_list), "LinkedList([])")

    def test_getitem_non_int_index(self):
        # Arrange
        test_list = create_list_from_values(["D", "C", "B", "A"])

        # Act & Assert
        with self.assertRaises(TypeError) as context:
            test_list["1"]

        self.assertEqual(str(context.exception), "Index must be an integer.")

    def test_getitem_out_of_bounds_index(self):
        # Arrange
        test_list = create_list_from_values(["D", "C", "B", "A"])

        # Act & Assert
        with self.assertRaises(IndexError) as context:
            test_list[-1]

        self.assertEqual(str(context.exception), "Index out of bounds.")

    def test_getitem_valid_index(self):
        # Arrange
        test_list = create_list_from_values(["D", "C", "B", "A"])

        # Act
        result = test_list[0]

        # Assert
        self.assertEqual(result, "A")

    def test_insert_at_head(self):
        # Arrange
        test_list = create_list_from_values(["D", "C", "B", "A"])

        # Act
        test_list.insert(index=0, value="test")

        # Assert
        self.assertEqual(repr(test_list), "LinkedList([test -> A -> B -> C -> D])")

    def test_insert_at_middle(self):
        # Arrange
        test_list = create_list_from_values(["D", "C", "B", "A"])

        # Act
        test_list.insert(index=1, value="test")

        # Assert
        self.assertEqual(repr(test_list), "LinkedList([A -> test -> B -> C -> D])")

    def test_insert_at_tail(self):
        # Arrange
        test_list = create_list_from_values(["D", "C", "B", "A"])

        # Act
        test_list.insert(index=3, value="test")

        # Assert
        self.assertEqual(repr(test_list), "LinkedList([A -> B -> C -> test -> D])")

    def test_insert_after_tail(self):
        # Arrange
        test_list = create_list_from_values(["D", "C", "B", "A"])

        # Act
        test_list.insert(index=4, value="test")

        # Assert
        self.assertEqual(repr(test_list), "LinkedList([A -> B -> C -> D -> test])")

    def test_insert_empty_list(self):
        # Arrange
        test_list = create_list_from_values([])

        # Act
        test_list.insert(index=0, value="test")

        # Assert
        self.assertEqual(repr(test_list), "LinkedList([test])")

    def test_remove_head(self):
        # Arrange
        test_list = create_list_from_values(["D", "C", "B", "A"])

        # Act
        test_list.remove(index=0)

        # Assert
        self.assertEqual("LinkedList([B -> C -> D])", repr(test_list))

    def test_remove_middle_node(self):
        # Arrange
        test_list = create_list_from_values(["D", "C", "B", "A"])

        # Act
        test_list.remove(index=1)

        # Assert
        self.assertEqual(repr(test_list), "LinkedList([A -> C -> D])")

    def test_remove_tail(self):
        # Arrange
        test_list = create_list_from_values(["D", "C", "B", "A"])

        # Act
        test_list.remove(index=3)

        # Assert
        self.assertEqual(repr(test_list), "LinkedList([A -> B -> C])")

    def test_remove_from_empty_list(self):
        # Arrange
        test_list = create_list_from_values([])

        # Act & Assert
        with self.assertRaises(IndexError) as context:
            test_list.remove(index=0)

        self.assertEqual("Cannot remove from an empty list.", str(context.exception))

    def test_append(self):
        # Arrange
        test_list = create_list_from_values(["D", "C", "B", "A"])

        # Act
        test_list.append("test")

        # Assert
        self.assertEqual(repr(test_list), "LinkedList([A -> B -> C -> D -> test])")

    def test_append_empty_list(self):
        # Arrange
        test_list = create_list_from_values([])

        # Act
        test_list.append("test")

        # Assert
        self.assertEqual(repr(test_list), "LinkedList([test])")

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
        self.assertEqual(repr(test_list), "LinkedList([])")


###### HELPER FUNCTIONS ######
def create_list_from_values(values):
    linked_list = SinglyLinkedList()
    for value in values:
        linked_list.prepend(value)
    return linked_list
