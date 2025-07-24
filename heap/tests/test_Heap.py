import pytest

import sys
import os

# this line modifies sys.path inside of the test files and is necessary to import our code files without turning them into a package
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from heap import Heap


@pytest.mark.parametrize("max_heap", [False, True])
def test_heap_property_on_init(max_heap):
    # Act
    heap = Heap(
        list_of_values=[9, 2, 7, 4, 1, 6, 5, 8, 3],
        max_heap=max_heap
    )

    # Assert
    for i in range(len(heap._data)):
        left = 2 * i + 1
        right = 2 * i + 2

        if left < len(heap._data):
            assert heap._data[i] <= heap._data[left], \
                f"Heap property violated: parent {heap._data[i]} > left child {heap._data[left]} at index {i}"

        if right < len(heap._data):
            assert heap._data[i] <= heap._data[right], \
                f"Heap property violated: parent {heap._data[i]} > right child {heap._data[right]} at index {i}"


@pytest.mark.parametrize("max_heap, expected", [
    (False, "MinHeap data=[10]"),
    (True, "MaxHeap data=[10]")
])
def test_push_single_value(max_heap, expected):
    # Arrange
    heap = Heap(max_heap=max_heap)

    # Act
    heap.push(10)

    # Assert
    assert repr(heap) == expected
