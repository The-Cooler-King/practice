import pytest
import warnings

import sys
import os

# this line modifies sys.path inside of the test files and is necessary to import our code files without turning them into a package
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from heap import Heap


@pytest.mark.parametrize("max_heap", [False, True])
def test_heap_property_on_init(max_heap):
    # Act
    heap = Heap(
        data=[9, 2, 7, 4, 1, 6, 5, 8, 3],
        max_heap=max_heap
    )

    # Assert
    assert_heap_property(heap)


@pytest.mark.parametrize("max_heap, expected", [
    (False, "MinHeap(size=0, root=None)"),
    (True, "MaxHeap(size=0, root=None)")
])
def test_empty_heap_init(max_heap, expected):
    # Arrange
    heap = Heap(max_heap=max_heap)

    # Assert
    assert repr(heap) == expected


@pytest.mark.parametrize("max_heap, expected", [
    (False, "MinHeap(size=1, root=42)"),
    (True, "MaxHeap(size=1, root=42)")
])
def test_single_element_heap_init(max_heap, expected):
    # Arrange
    heap = Heap(
        data=[42],
        max_heap=max_heap
    )

    # Assert
    assert repr(heap) == expected


@pytest.mark.parametrize("max_heap, expected", [
    (False, "MinHeap(size=1, root=10)"),
    (True, "MaxHeap(size=1, root=10)")
])
def test_push_single_value(max_heap, expected):
    # Arrange
    heap = Heap(max_heap=max_heap)

    # Act
    heap.push(10)

    # Assert
    assert repr(heap) == expected


@pytest.mark.parametrize("max_heap, expected", [
    (False, 2),
    (True, 10)
])
def test_push_multiple_values_maintains_heap_property(max_heap, expected):
    # Arrange
    heap = Heap(max_heap=max_heap)
    values = [10, 4, 7, 2, 8]

    # Act
    for value in values:
        heap.push(value)

    # Assert
    assert heap.peek() == expected


@pytest.mark.parametrize("max_heap", [False, True])
def test_push_maintains_order_for_heap_property(max_heap):
    # Arrange
    heap = Heap(max_heap=max_heap)
    values = [20, 5, 15, 22, 1]

    # Act
    for val in values:
        heap.push(val)

    # Assert
    assert_heap_property(heap)


@pytest.mark.parametrize("max_heap, expected_head, expected_data", [
    (False, 2, [2, 3, 3, 5, 5]),
    (True, 5, [-5, -5, -3, -3, -2])
])
def test_push_duplicate_values(max_heap, expected_head, expected_data):
    # Arrange
    heap = Heap(max_heap=max_heap)
    values = [5, 3, 3, 5, 2]

    # Act
    for val in values:
        heap.push(val)

    # Assert
    assert heap.peek() == expected_head
    assert sorted(heap._data) == expected_data


@pytest.mark.parametrize("max_heap", [False, True])
def test_peek_empty_heap(max_heap):
    # Arrange
    heap = Heap(max_heap=max_heap)

    # Act
    head_value = heap.peek()

    # Assert
    assert head_value is None


@pytest.mark.parametrize("max_heap", [False, True])
def test_peek_single_element(max_heap):
    # Arrange
    heap = Heap([1])

    # Act
    head_value = heap.peek()

    # Assert
    assert head_value == 1


@pytest.mark.parametrize("max_heap, expected", [
    (False, 1),
    (True, 22)
])
def test_peek_multiple_elements(max_heap, expected):
    # Arrange
    heap = Heap(
        data=[20, 5, 15, 22, 1],
        max_heap=max_heap
    )

    # Act
    head_value = heap.peek()

    # Assert
    assert head_value == expected


@pytest.mark.parametrize("max_heap", [False, True])
def test_peek_does_not_remove_element(max_heap):
    # Arrange
    heap = Heap(
        data=[3],
        max_heap=max_heap
    )
    peeked = heap.peek()

    # Act
    still_peeked = heap.peek()

    # Assert
    assert still_peeked == peeked


@pytest.mark.parametrize("max_heap, expected", [
    (False, 1),
    (True, 8)
])
def test_pop_returns_smallest(max_heap, expected):
    # Arrange
    heap = Heap(
        data=[5, 3, 8, 1, 4],
        max_heap=max_heap
    )

    # Act
    result = heap.pop()

    # Assert
    assert result == expected


@pytest.mark.parametrize("max_heap, expected", [
    (False, [1, 3, 4, 5, 8]),
    (True, [8, 5, 4, 3, 1])
])
def test_pop_multiple_times_returns_sorted_values(max_heap, expected):
    # Arrange
    heap = Heap(
        data=[5, 3, 8, 1, 4],
        max_heap=max_heap
    )

    # Act
    popped_values = [heap.pop() for _ in range(5)]

    # Assert
    assert popped_values == expected


@pytest.mark.parametrize("max_heap", [False, True])
def test_pop_on_empty_heap_returns_none(max_heap):
    # Arrange
    heap = Heap(max_heap=max_heap)

    # Act
    result = heap.pop()

    # Assert
    assert result is None


@pytest.mark.parametrize("max_heap", [False, True])
def test_heap_property_after_pop(max_heap):
    # Arrange
    heap = Heap(
        data=[5, 3, 8, 1, 4],
        max_heap=max_heap
    )

    # Act
    heap.pop()

    # Assert
    assert_heap_property(heap)


@pytest.mark.parametrize("max_heap", [False, True])
def test_pop_single_element_then_empty(max_heap):
    # Arrange
    heap = Heap(
        data=[10],
        max_heap=max_heap
    )

    # Act
    first_pop = heap.pop()
    second_pop = heap.pop()

    # Assert
    assert first_pop == 10
    assert second_pop is None


@pytest.mark.parametrize("max_heap, expected", [(False, True), (True, False)])
def test_is_min_heap_no_data(max_heap, expected):
    # Arrange
    heap = Heap(max_heap=max_heap)

    # Act and Assert
    assert heap.is_min_heap() == expected


@pytest.mark.parametrize("max_heap, expected", [(False, True), (True, False)])
def test_is_min_heap_with_data(max_heap, expected):
    # Arrange
    heap = Heap(
        data=[5, 3, 8, 1, 4],
        max_heap=max_heap
    )

    # Act and Assert
    assert heap.is_min_heap() == expected


@pytest.mark.parametrize("max_heap, expected", [(False, False), (True, True)])
def test_toggle_heap_type_no_data(max_heap, expected):
    # Arrange
    heap = Heap(max_heap=max_heap)

    # Act
    heap.toggle_heap_type()

    # Assert
    assert heap.is_min_heap() == expected


@pytest.mark.parametrize("max_heap, expected", [(False, False), (True, True)])
def test_is_min_heap_with_data(max_heap, expected):
    # Arrange
    heap = Heap(
        data=[5, 3, 8, 1, 4],
        max_heap=max_heap
    )

    # Act
    heap.toggle_heap_type()

    # Assert
    assert heap.is_min_heap() == expected
    assert_heap_property(heap)


@pytest.mark.parametrize("max_heap, expected", [(False, "MinHeap(size=0, root=None)"), (True, "MaxHeap(size=0, root=None)")])
def test_repr_no_data(max_heap, expected):
    # Arrange
    heap = Heap(max_heap=max_heap)

    # Act and Assert
    assert repr(heap) == expected


@pytest.mark.parametrize("max_heap, expected", [(False, "MinHeap(size=1, root=10)"), (True, "MaxHeap(size=1, root=10)")])
def test_repr_one_element(max_heap, expected):
    # Arrange
    heap = Heap(
        data=[10],
        max_heap=max_heap
    )

    # Act and Assert
    assert repr(heap) == expected


@pytest.mark.parametrize("max_heap, expected",
                         [(False, "MinHeap(size=5, root=1)"), (True, "MaxHeap(size=5, root=8)")])
def test_repr_multiple_elements(max_heap, expected):
    # Arrange
    heap = Heap(
        data=[5, 3, 8, 1, 4],
        max_heap=max_heap
    )

    # Act & Assert
    assert repr(heap) == expected


@pytest.mark.parametrize("max_heap", [False, True])
def test_bool_empty_heap(max_heap):
    # Arrange
    heap = Heap(max_heap=max_heap)

    # Act & Assert
    assert not heap


@pytest.mark.parametrize("max_heap", [False, True])
def test_bool_non_empty_heap(max_heap):
    # Arrange
    heap = Heap(
        data=[5, 3, 8, 1, 4],
        max_heap=max_heap
    )

    # Act & Assert
    assert heap

@pytest.mark.parametrize("max_heap", [False, True])
def test_len_empty_heap(max_heap):
    # Arrange
    heap = Heap(max_heap=max_heap)

    # Act & Assert
    assert len(heap) == 0


@pytest.mark.parametrize("max_heap", [False, True])
def test_len_non_empty_heap(max_heap):
    # Arrange
    heap = Heap(
        data=[5, 3, 8, 1, 4],
        max_heap=max_heap
    )

    # Act & Assert
    assert len(heap) == 5

@pytest.mark.parametrize("max_heap", [False, True])
def test_contains_empty_heap(max_heap):
    # Arrange
    heap = Heap(max_heap=max_heap)

    # Act & Assert
    assert 5 not in heap


@pytest.mark.parametrize("max_heap", [False, True])
def test_contains_value_not_present(max_heap):
    # Arrange
    heap = Heap(
        data=[5, 3, 8, 1, 4],
        max_heap=max_heap
    )

    # Act & Assert
    assert 10 not in heap


@pytest.mark.parametrize("max_heap", [False, True])
def test_contains_value_not_present(max_heap):
    # Arrange
    heap = Heap(
        data=[5, 3, 8, 1, 4],
        max_heap=max_heap
    )

    # Act & Assert
    assert 5 in heap

@pytest.mark.parametrize("max_heap", [False, True])
def test_iter_empty_heap(max_heap):
    # Arrange
    heap = Heap(max_heap=max_heap)

    # Act & Assert
    assert list(heap) == []


@pytest.mark.parametrize("max_heap, reverse", [(False, False), (True, True)])
def test_iter_non_empty_heap(max_heap, reverse):
    # Arrange
    values = [5, 3, 8, 1, 4]
    heap = Heap(
        data=values,
        max_heap=max_heap
    )

    # Act and Assert
    assert list(heap) == sorted(values, reverse=reverse)


def test_iter_large_heap_warns():
    # Arrange
    values = list(range(1001))
    heap = Heap(
        data=values,
        max_heap=False
    )

    # Act
    with warnings.catch_warnings(record=True) as w:
        warnings.simplefilter("always")  # Trigger all warnings
        result = list(heap)

        # Assert
        assert len(result) == 1001
        assert result == sorted(values)
        assert any(issubclass(warning.category, RuntimeWarning) for warning in w)


def assert_heap_property(heap):
    # Check that the heap property holds at each parent node
    for i in range(len(heap._data)):
        left = 2 * i + 1
        right = 2 * i + 2

        if left < len(heap._data):
            assert heap._data[i] <= heap._data[left], \
                f"Heap property violated: parent {heap._data[i]} > left child {heap._data[left]} at index {i}"

        if right < len(heap._data):
            assert heap._data[i] <= heap._data[right], \
                f"Heap property violated: parent {heap._data[i]} > right child {heap._data[right]} at index {i}"
