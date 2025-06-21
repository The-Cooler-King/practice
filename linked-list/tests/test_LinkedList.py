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
        self.assertIsNone(test_list.head)

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
        self.assertEqual(test_list.head.value, 5)
        self.assertIsNone(test_list.head.next)

    def test_prepend_to_list(self):
        # Arrange
        test_list = LinkedList()
        test_list.prepend(5)
        original_node = test_list.head

        # Act
        test_list.prepend(6)

        # Assert
        self.assertEqual(test_list.head.value, 6)
        self.assertEqual(test_list.head.next, original_node)

    def test_pop_node_from_empty_list(self):
        # Arrange
        test_list = create_list_from_values([])

        # Act
        pop_value = test_list.pop()

        # Assert
        self.assertIsNone(pop_value)
        self.assertIsNone(test_list.head)

    def test_pop_node_from_single_node_list(self):
        # Arrange
        test_list = create_list_from_values([1])

        # Act
        pop_value = test_list.pop()

        # Assert
        self.assertEqual(pop_value, 1)
        self.assertIsNone(test_list.head)

    def test_pop_node_from_two_node_list(self):
        # Arrange
        test_list = create_list_from_values([1, 2])

        # Act
        pop_value = test_list.pop()

        # Assert
        self.assertEqual(pop_value, 1)
        self.assertEqual(test_list.head.value, 2)
        self.assertIsNone(test_list.head.next)

    def test_pop_node_from_multiple_node_list(self):
        # Arrange
        test_list = create_list_from_values([1, 2, 3, 4])

        # Act
        pop_value = test_list.pop()

        # Assert
        self.assertEqual(pop_value, 1)
        self.assertEqual(test_list.head.value, 4)
        self.assertEqual(test_list.head.next.value, 3)
        self.assertEqual(test_list.head.next.next.value, 2)
        self.assertIsNone(test_list.head.next.next.next)


###### HELPER FUNCTIONS ######
def create_list_from_values(values):
    linked_list = LinkedList()
    for value in values:
        linked_list.prepend(value)
    return linked_list
