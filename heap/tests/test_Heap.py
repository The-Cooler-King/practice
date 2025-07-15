import unittest

import sys
import os

# this line modifies sys.path inside of the test files and is necessary to import our code files without turning them into a package
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from heap import Heap


class TestHeapInsert(unittest.TestCase):

    def test_insert_single_value(self):
        # Arrange
        heap = Heap()

        # Act
        heap.insert(10)

        # Assert
        self.assertEqual(heap._data, [10])

    def test_insert_multiple_values_maintains_min_heap(self):
        # Arrange
        heap = Heap()
        values = [10, 4, 7, 2, 8]

        # Act
        for val in values:
            heap.insert(val)

        # Assert
        # The smallest value should bubble up to index 0
        self.assertEqual(heap._data[0], min(values))

    def test_insert_maintains_order_for_heap_property(self):
        # Arrange
        heap = Heap()

        # Act
        heap.insert(20)
        heap.insert(5)
        heap.insert(15)
        heap.insert(22)
        heap.insert(1)

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

    def test_insert_duplicate_values(self):
        # Arrange
        heap = Heap()
        values = [5, 3, 3, 5, 2]

        # Act
        for val in values:
            heap.insert(val)

        # Assert
        self.assertEqual(heap._data[0], 2)
        self.assertEqual(sorted(heap._data), sorted(values))


if __name__ == '__main__':
    unittest.main()
