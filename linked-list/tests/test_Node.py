import unittest

import sys
import os

# this line modifies sys.path inside of the test files and is necessary to import our code files without turning them into a package
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from Node import Node


class TestNode(unittest.TestCase):

    def test_node_initialization(self):
        # Arrange
        value = 10

        # Act
        node = Node(value)

        # Assert
        self.assertEqual(node.value, 10)
        self.assertIsNone(node.next)

    def test_node_with_next(self):
        # Arrange
        node1 = Node(1)
        node2 = Node(2, node1)

        # Act
        next_node = node2.next

        # Assert
        self.assertEqual(next_node, node1)
        self.assertEqual(node2.value, 2)

    def test_node_repr(self):
        # Arrange
        node = Node(5)

        # Act
        node_repr = repr(node)

        # Assert
        self.assertEqual(node_repr, "Node(5)")

    def test_node_equality(self):
        # Arrange
        node1 = Node(5)
        node2 = Node(5)
        node3 = Node(5, Node(6))

        # Act & Assert
        self.assertEqual(node1, node2)
        self.assertNotEqual(node1, node3)


if __name__ == "__main__":
    unittest.main()
