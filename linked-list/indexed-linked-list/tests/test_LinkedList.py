import unittest

import sys
import os

# this line modifies sys.path inside of the test files and is necessary to import our code files without turning them into a package
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from LinkedList import LinkedList
from Node import Node


class TestLinkedList(unittest.TestCase):

    def test_list_initialization(self):
        # Arrange
        test_list = LinkedList()

        # Assert
        self.assertEqual(repr(test_list), "Empty List")
        self.assertEqual(len(test_list), 0)
        self.assertEqual(test_list._index_map, {})

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
        self.assertTrue(test_list.validate_index_map())

    def test_rebuild_index_map_empty_list(self):
        # Arrange
        test_list = create_list_from_values([])

        # Act
        test_list.rebuild_index_map()

        # Assert
        self.assertTrue(test_list.validate_index_map())

    def test__rebuild_index_map_partial(self):
        # Arrange
        test_list = create_list_from_values(["C", "B", "A"])
        node_b = test_list.head().next

        # Act
        test_list._rebuild_index_map_partial(start_index=1, start_node=node_b)

        # Assert
        self.assertTrue(test_list.validate_index_map())

    def test_validate_index_map_valid_map(self):
        # Arrange
        test_list = create_list_from_values(["C", "B", "A"])

        # Act & Assert
        self.assertTrue(test_list.validate_index_map())

    def test_validate_index_map_stale_index(self):
        # Arrange
        test_list = create_list_from_values(["C", "B", "A"])
        # pop node_c, but restore it to the index map
        node_c_value = test_list.pop()
        test_list._index_map[2] = Node(node_c_value)

        # Act & Assert
        self.assertFalse(test_list.validate_index_map())

    def test_validate_index_map_incorrect_mapping(self):
        # Arrange
        test_list = create_list_from_values(["C", "B", "A"])
        node_a = test_list.head()
        node_b = node_a.next
        # switch indexes of node_a and node_b
        test_list._index_map[0] = node_b
        test_list._index_map[1] = node_a

        # Act & Assert
        self.assertFalse(test_list.validate_index_map())

    def test_validate_index_map_missing_mapping(self):
        # Arrange
        test_list = create_list_from_values(["C", "B", "A"])
        test_list._index_map.pop(2)  # get rid of index 2 in the index map

        # Act & Assert
        self.assertFalse(test_list.validate_index_map())

    def test_prepend_to_empty_list(self):
        # Arrange
        test_list = LinkedList()

        # Act
        test_list.prepend(5)

        # Assert
        self.assertEqual(repr(test_list), "LinkedList([5])")
        self.assertTrue(test_list.validate_index_map())
        self.assertEqual(len(test_list), 1)

    def test_prepend_to_list(self):
        # Arrange
        test_list = LinkedList()
        test_list.prepend(5)

        # Act
        test_list.prepend(6)

        # Assert
        self.assertEqual(repr(test_list), "LinkedList([6 -> 5])")
        self.assertTrue(test_list.validate_index_map())
        self.assertEqual(len(test_list), 2)

    def test_classic_pop_node_from_empty_list(self):
        # Arrange
        test_list = create_list_from_values([])

        # Act
        pop_value = test_list.classic_pop()

        # Assert
        self.assertIsNone(pop_value)
        self.assertEqual(repr(test_list), "Empty List")
        self.assertTrue(test_list.validate_index_map())
        self.assertEqual(len(test_list), 0)

    def test_classic_pop_node_from_single_node_list(self):
        # Arrange
        test_list = create_list_from_values([1])

        # Act
        pop_value = test_list.classic_pop()

        # Assert
        self.assertEqual(pop_value, 1)
        self.assertEqual(repr(test_list), "Empty List")
        self.assertTrue(test_list.validate_index_map())
        self.assertEqual(len(test_list), 0)

    def test_classic_pop_node_from_two_node_list(self):
        # Arrange
        test_list = create_list_from_values([1, 2])

        # Act
        pop_value = test_list.classic_pop()

        # Assert
        self.assertEqual(pop_value, 1)
        self.assertEqual(repr(test_list), "LinkedList([2])")
        self.assertTrue(test_list.validate_index_map())
        self.assertEqual(len(test_list), 1)

    def test_classic_pop_node_from_multiple_node_list(self):
        # Arrange
        test_list = create_list_from_values([1, 2, 3, 4])

        # Act
        pop_value = test_list.classic_pop()

        # Assert
        self.assertEqual(pop_value, 1)
        self.assertEqual(repr(test_list), "LinkedList([4 -> 3 -> 2])")
        self.assertTrue(test_list.validate_index_map())
        self.assertEqual(len(test_list), 3)

    def test_pop_node_from_empty_list(self):
        # Arrange
        test_list = create_list_from_values([])

        # Act
        pop_value = test_list.pop()

        # Assert
        self.assertIsNone(pop_value)
        self.assertEqual(repr(test_list), "Empty List")
        self.assertTrue(test_list.validate_index_map())
        self.assertEqual(len(test_list), 0)

    def test_pop_node_from_single_node_list(self):
        # Arrange
        test_list = create_list_from_values([1])

        # Act
        pop_value = test_list.pop()

        # Assert
        self.assertEqual(pop_value, 1)
        self.assertEqual(repr(test_list), "Empty List")
        self.assertTrue(test_list.validate_index_map())
        self.assertEqual(len(test_list), 0)

    def test_pop_node_from_two_node_list(self):
        # Arrange
        test_list = create_list_from_values([1, 2])

        # Act
        pop_value = test_list.pop()

        # Assert
        self.assertEqual(pop_value, 1)
        self.assertEqual(repr(test_list), "LinkedList([2])")
        self.assertTrue(test_list.validate_index_map())
        self.assertEqual(len(test_list), 1)

    def test_pop_node_from_multiple_node_list(self):
        # Arrange
        test_list = create_list_from_values([1, 2, 3, 4])

        # Act
        pop_value = test_list.pop()

        # Assert
        self.assertEqual(pop_value, 1)
        self.assertEqual(repr(test_list), "LinkedList([4 -> 3 -> 2])")
        self.assertTrue(test_list.validate_index_map())
        self.assertEqual(len(test_list), 3)

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
        node_b = test_list.get_node(1)
        node_g = test_list.get_node(6)
        node_g.next = node_b  # set node "G" next to node "B"

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
        test_list._head.next = test_list._head  # set head.next equal to itself. single node loop

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
        node_b = test_list.get_node(1)
        node_g = test_list.get_node(6)
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
        self.assertTrue(test_list.validate_index_map())

    def test_reverse_single_node_list(self):
        # Arrange
        test_list = create_list_from_values(["A"])

        # Act
        test_list.reverse()

        # Assert
        self.assertEqual(repr(test_list), "LinkedList([A])")
        self.assertTrue(test_list.validate_index_map())

    def test_reverse_empty_list(self):
        # Arrange
        test_list = create_list_from_values([])

        # Act
        test_list.reverse()

        # Assert
        self.assertEqual(repr(test_list), "Empty List")
        self.assertTrue(test_list.validate_index_map())

    def test_reverse_cyclical_list(self):
        # Arrange
        test_list = create_list_from_values(["B", "A"])
        test_list._head.next.next = test_list._head  # set node "B" next to node "A"

        # Act & Assert
        with self.assertRaises(RuntimeError) as context:
            test_list.reverse()

        self.assertEqual(str(context.exception), "Cannot reverse a cyclical linked list")

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
            test_list[4]

        self.assertEqual(str(context.exception), "Index out of bounds.")

    def test_getitem_valid_index(self):
        # Arrange
        test_list = create_list_from_values(["D", "C", "B", "A"])

        # Act
        result = test_list[0]

        # Assert
        self.assertEqual(result, "A")

    def test_get_node_non_int_index(self):
        # Arrange
        test_list = create_list_from_values(["D", "C", "B", "A"])

        # Act & Assert
        with self.assertRaises(TypeError) as context:
            test_list.get_node("1")

        self.assertEqual(str(context.exception), "Index must be an integer.")

    def test_get_node_out_of_bounds_index(self):
        # Arrange
        test_list = create_list_from_values(["D", "C", "B", "A"])

        # Act & Assert
        with self.assertRaises(IndexError) as context:
            test_list.get_node(4)

        self.assertEqual(str(context.exception), "Index out of bounds.")

    def test_get_node_valid_index(self):
        # Arrange
        test_list = create_list_from_values(["D", "C", "B", "A"])
        node_a = test_list._head

        # Act
        result = test_list.get_node(0)

        # Assert
        self.assertEqual(result, node_a)

    def test_validate_index_valid_no_append_flag(self):
        # Arrange
        test_list = create_list_from_values(["D", "C", "B", "A"])

        # Act & Assert
        for index in range(4):
            test_list._validate_index(index)
        # none of the indexes should raise

    def test_validate_index_valid_append_flag(self):
        # Arrange
        test_list = create_list_from_values(["D", "C", "B", "A"])

        # Act & Assert
        for index in range(5):
            test_list._validate_index(index, True)
        # none of the indexes should raise

    def test_validate_index_invalid_type(self):
        # Arrange
        test_list = create_list_from_values(["D", "C", "B", "A"])

        # Act & Assert
        with self.assertRaises(TypeError) as context:
            test_list._validate_index("A")

        self.assertEqual(str(context.exception), "Index must be an integer.")

    def test_validate_index_negative_index(self):
        # Arrange
        test_list = create_list_from_values(["D", "C", "B", "A"])

        # Act & Assert
        with self.assertRaises(IndexError) as context:
            test_list._validate_index(-1)

        self.assertEqual(str(context.exception), "Index out of bounds.")

    def test_validate_index_too_high_index_no_append(self):
        # Arrange
        test_list = create_list_from_values(["D", "C", "B", "A"])

        # Act & Assert
        with self.assertRaises(IndexError) as context:
            test_list._validate_index(4)

        self.assertEqual(str(context.exception), "Index out of bounds.")

    def test_validate_index_too_high_index_append(self):
        # Arrange
        test_list = create_list_from_values(["D", "C", "B", "A"])

        # Act & Assert
        with self.assertRaises(IndexError) as context:
            test_list._validate_index(5)

        self.assertEqual(str(context.exception), "Index out of bounds.")

    def test_insert_at_head(self):
        # Arrange
        test_list = create_list_from_values(["D", "C", "B", "A"])

        # Act
        test_list.insert(index=0, value="test")

        # Assert
        self.assertEqual(repr(test_list), "LinkedList([test -> A -> B -> C -> D])")
        self.assertTrue(test_list.validate_index_map())
        self.assertEqual(len(test_list), 5)

    def test_insert_at_middle(self):
        # Arrange
        test_list = create_list_from_values(["D", "C", "B", "A"])

        # Act
        test_list.insert(index=1, value="test")

        # Assert
        self.assertEqual(repr(test_list), "LinkedList([A -> test -> B -> C -> D])")
        self.assertTrue(test_list.validate_index_map())
        self.assertEqual(len(test_list), 5)

    def test_insert_at_tail(self):
        # Arrange
        test_list = create_list_from_values(["D", "C", "B", "A"])

        # Act
        test_list.insert(index=3, value="test")

        # Assert
        self.assertEqual(repr(test_list), "LinkedList([A -> B -> C -> test -> D])")
        self.assertTrue(test_list.validate_index_map())
        self.assertEqual(len(test_list), 5)

    def test_insert_after_tail(self):
        # Arrange
        test_list = create_list_from_values(["D", "C", "B", "A"])

        # Act
        test_list.insert(index=4, value="test")

        # Assert
        self.assertEqual(repr(test_list), "LinkedList([A -> B -> C -> D -> test])")
        self.assertTrue(test_list.validate_index_map())
        self.assertEqual(len(test_list), 5)

    def test_insert_empty_list(self):
        # Arrange
        test_list = create_list_from_values([])

        # Act
        test_list.insert(index=0, value="test")

        # Assert
        self.assertEqual(repr(test_list), "LinkedList([test])")
        self.assertTrue(test_list.validate_index_map())
        self.assertEqual(len(test_list), 1)

    def test_remove_head(self):
        # Arrange
        test_list = create_list_from_values(["D", "C", "B", "A"])

        # Act
        test_list.remove(index=0)

        # Assert
        self.assertEqual(repr(test_list), "LinkedList([B -> C -> D])")
        self.assertTrue(test_list.validate_index_map())
        self.assertEqual(len(test_list), 3)

    def test_remove_middle_node(self):
        # Arrange
        test_list = create_list_from_values(["D", "C", "B", "A"])

        # Act
        test_list.remove(index=1)

        # Assert
        self.assertEqual(repr(test_list), "LinkedList([A -> C -> D])")
        self.assertTrue(test_list.validate_index_map())
        self.assertEqual(len(test_list), 3)

    def test_remove_tail(self):
        # Arrange
        test_list = create_list_from_values(["D", "C", "B", "A"])

        # Act
        test_list.remove(index=3)

        # Assert
        self.assertEqual(repr(test_list), "LinkedList([A -> B -> C])")
        self.assertTrue(test_list.validate_index_map())
        self.assertEqual(len(test_list), 3)

    def test_remove_from_empty_list(self):
        # Arrange
        test_list = create_list_from_values([])

        # Act & Assert
        with self.assertRaises(IndexError) as context:
            test_list.remove(index=0)

        self.assertEqual(str(context.exception), "Cannot remove from an empty list.")

    def test_setitem(self):
        # Arrange
        test_list = create_list_from_values(["D", "C", "B", "A"])

        # Act
        test_list[1] = "new value"

        # Assert
        self.assertEqual(repr(test_list), "LinkedList([A -> new value -> C -> D])")
        self.assertTrue(test_list.validate_index_map())
        self.assertEqual(len(test_list), 4)

    def test_append(self):
        # Arrange
        test_list = create_list_from_values(["D", "C", "B", "A"])

        # Act
        test_list.append("test")

        # Assert
        self.assertEqual(repr(test_list), "LinkedList([A -> B -> C -> D -> test])")
        self.assertTrue(test_list.validate_index_map())
        self.assertEqual(len(test_list), 5)

    def test_append_empty_list(self):
        # Arrange
        test_list = create_list_from_values([])

        # Act
        test_list.append("test")

        # Assert
        self.assertEqual(repr(test_list), "LinkedList([test])")
        self.assertTrue(test_list.validate_index_map())
        self.assertEqual(len(test_list), 1)

###### HELPER FUNCTIONS ######
def create_list_from_values(values):
    linked_list = LinkedList()
    for value in values:
        linked_list.prepend(value)
    return linked_list
