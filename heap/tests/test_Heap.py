import unittest

import sys
import os

# this line modifies sys.path inside of the test files and is necessary to import our code files without turning them into a package
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from heap import Heap


class TestHeap(unittest.TestCase):

    def test_push_single_value(self):
        # Arrange
        heap = Heap()

        # Act
        heap.push(10)

        # Assert
        self.assertEqual([10], heap._data)

    def test_push_multiple_values_maintains_min_heap(self):
        # Arrange
        heap = Heap()
        values = [10, 4, 7, 2, 8]

        # Act
        for val in values:
            heap.push(val)

        # Assert
        # The smallest value should bubble up to index 0
        self.assertEqual(min(values), heap._data[0])

    def test_push_maintains_order_for_heap_property(self):
        # Arrange
        heap = Heap()
        values = [20, 5, 15, 22, 1]

        # Act
        for val in values:
            heap.push(val)

        # Assert
        # Check that the heap property holds at each parent node
        data = heap._data
        for i in range(len(data)):
            left = 2 * i + 1
            right = 2 * i + 2
            if left < len(data):
                self.assertLessEqual(data[i], data[left])
            if right < len(data):
                self.assertLessEqual(data[i], data[right])

    def test_push_duplicate_values(self):
        # Arrange
        heap = Heap()
        values = [5, 3, 3, 5, 2]

        # Act
        for val in values:
            heap.push(val)

        # Assert
        self.assertEqual(2, heap._data[0])
        self.assertEqual(sorted(values), sorted(heap._data))

    def test_peek_empty_heap(self):
        # Arrange
        heap = Heap()

        # Act
        smallest_value = heap.peek()

        # Assert
        self.assertIsNone(smallest_value)

    def test_peek_single_element(self):
        # Arrange
        heap = Heap()
        heap.push(1)

        # Act
        smallest_value = heap.peek()

        # Assert
        self.assertEqual(1, smallest_value)

    def test_peek_multiple_elements(self):
        # Arrange
        heap = Heap()
        values = [20, 5, 15, 22, 1]
        for val in values:
            heap.push(val)

        # Act
        smallest_value = heap.peek()

        # Assert
        self.assertEqual(1, smallest_value)

    def test_peek_does_not_remove_element(self):
        # Arrange
        heap = Heap()
        heap.push(3)
        peeked = heap.peek()

        # Act
        still_peeked = heap.peek()

        # Assert
        self.assertEqual(peeked, still_peeked)

    def test_pop_returns_smallest(self):
        # Arrange
        heap = Heap()
        for value in [5, 3, 8, 1, 4]:
            heap.push(value)

        # Act
        result = heap.pop()

        # Assert
        self.assertEqual(result, 1)

    def test_pop_multiple_times_returns_sorted_values(self):
        # Arrange
        heap = Heap()
        for value in [5, 3, 8, 1, 4]:
            heap.push(value)

        # Act
        popped_values = [heap.pop() for _ in range(5)]

        # Assert
        self.assertEqual(popped_values, [1, 3, 4, 5, 8])

    def test_pop_on_empty_heap_returns_none(self):
        # Arrange
        heap = Heap()

        # Act
        result = heap.pop()

        # Assert
        self.assertIsNone(result)

    def test_heap_property_after_pop(self):
        # Arrange
        heap = Heap()
        for value in [5, 3, 8, 1, 4]:
            heap.push(value)

        # Act
        heap.pop()

        # Assert
        for i in range(len(heap._data) // 2):
            left = 2 * i + 1
            right = 2 * i + 2
            if left < len(heap._data):
                self.assertLessEqual(heap._data[i], heap._data[left])
            if right < len(heap._data):
                self.assertLessEqual(heap._data[i], heap._data[right])

    def test_pop_single_element_then_empty(self):
        # Arrange
        heap = Heap()
        heap.push(10)

        # Act
        first_pop = heap.pop()
        second_pop = heap.pop()

        # Assert
        self.assertEqual(first_pop, 10)
        self.assertIsNone(second_pop)


if __name__ == '__main__':
    unittest.main()
