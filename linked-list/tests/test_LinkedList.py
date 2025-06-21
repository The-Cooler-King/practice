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

    def test_prepend_to_empty_list(self):
        # Arrange
        test_list = LinkedList()

        # Act
        test_list.prepend(5)

        # Assert
        self.assertEqual(repr(test_list), "5")

    def test_prepend_to_list(self):
        # Arrange
        test_list = LinkedList()
        test_list.prepend(5)
        original_node = test_list.head

        # Act
        test_list.prepend(6)

        # Assert
        self.assertEqual(repr(test_list), "6 -> 5")

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
        self.assertEqual(repr(test_list), "2")

    def test_pop_node_from_multiple_node_list(self):
        # Arrange
        test_list = create_list_from_values([1, 2, 3, 4])

        # Act
        pop_value = test_list.pop()

        # Assert
        self.assertEqual(pop_value, 1)
        self.assertEqual(repr(test_list), "4 -> 3 -> 2")

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

        # Act
        result = repr(test_list)

        # Assert
        self.assertEqual(result, "4 -> 3 -> 2 -> 1")

    def test_repr_empty_list(self):
        # Arrange
        test_list = create_list_from_values([])

        # Act
        result = repr(test_list)

        # Assert
        self.assertEqual(result, "Empty List")

###### HELPER FUNCTIONS ######
def create_list_from_values(values):
    linked_list = LinkedList()
    for value in values:
        linked_list.prepend(value)
    return linked_list
