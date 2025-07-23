# Heap Class Documentation

## Overview

The `Heap` class implements a min-heap or max heap using a Python list as the internal data container. This version initializes a list of values as a heap and provides heap operations.

The heap uses **0-based indexing** for internal structure.

---

## Class: `Heap`

### Constructor

```python
def __init__(self, list_of_values=None, max_heap=False):
    self._data = list(list_of_values) if list_of_values is not None else []
    
    if max_heap:
        self._min_max_multiplier = -1
        self._data = [-element for element in self._data]
    else:
        self._min_max_multiplier = 1
    
    self._heapify()
```
---

### Example Usage

```python
from heap import Heap

empty_heap = Heap()
print(empty_heap._data)  # Output: []

min_heap = Heap([3, 7, 1, 5, 10])
print(min_heap._data) # Output: [1, 5, 3, 7, 10]

max_heap = Heap(list_of_values=[3, 7, 1, 5, 10], max_heap=True)
print(max_heap._data) # Output: [-10, -7, -1, -5, -3]
```
---

## Private Attributes

### `_data`
- **Type**: `list`
- **Description**: Stores the elements of the heap.
- **Default Value**: An empty list.

### `_min_max_multiplier`
- **Type**: `integer`
- **Description**: The value for each ingested or outputted value to be multiplied by (`1` or `-1`)
- **Default Value**: `1`
---

## Indexing Scheme

This implementation uses **0-based indexing**, which determines relationships like so:

- **Parent of node `i`**: `(i - 1) // 2`
- **Left child of node `i`**: `2 * i + 1`
- **Right child of node `i`**: `2 * i + 2`

This scheme aligns with how Python lists naturally operate. By indexing in this way, we turn a python list into a binary tree allowing for fast traversal and maintaining of minimum value.

---
## Public Methods

### `.push(value)`
Pushes value into the heap and places it in its rightful spot

### Example
```python
heap = Heap()
heap.push(20)
heap.push(5)
heap.push(15)
heap.push(22)
heap.push(1)

print(heap._data) # Output: [1, 5, 15, 22, 20]
```
---
### `.peek()`
Returns the smallest element of the heap without removing

### Example
```python
heap = Heap()

print(heap().peek()) # Output: None

heap.push(20)
heap.push(5)
heap.push(15)
heap.push(22)
heap.push(1)

print(heap.peek()) # Output: 1
```
---

### `.pop()`
Removes the minimum element from the heap, returns its value, and restores min-heap property.

### Example
```python
heap = Heap([20, 5, 15, 22, 1])

print(heap._data) # Output: [1, 5, 15, 22, 20]
print(heap.pop()) # Output: 1
print(heap._data) # Output: [5, 20, 15, 22]
```
---

### `.is_min_heap()`
Returns True if this heap is a min-heap, False if it is a max-heap

### Example
```python
max_heap = Heap(list_of_values=[1], max_heap=True)
print(max_heap.is_min_heap()) # False

min_heap = Heap(list_of_values=[1], max_heap=False)
print(min_heap.is_min_heap()) # True
```
---


### `.toggle_heap_type()`
Converts this heap to its opposite heap type (min-heap to max-heap and vice versa). All internal values are inverted and the heap property is restored

### Example
```python
heap = Heap(list_of_values=[1, 4, 5], max_heap=False)
print(heap._data) # Output: [1, 4, 5]

heap.toggle_heap_type()
print(heap._data) # Output: [-5, -4, -1]
```
---

## Private Methods

`_bubble_up(index)`
- Bubble up (aka Sift Up or Percolate Up) is the process of restoring the min-heap property after a new element is added to the heap
- When a new value is pushed, it is initially placed at the end of the internal list (which corresponds to the next available leaf position of the binary tree representation). However, this new value might violate the heap property by being smaller than its parent.
- To fix this, the value is repeatedly compared to its parent, and if it's smaller, the two are swapped. This continues until:
  - The value is no longer smaller than its parent, or
  - It reaches the root of the heap
- This process ensures that the smallest value "bubbles up" toward the top, preserving the min-heap invariant: **Every parent node is less than or equal to its children**

`._bubble_down(index)`
- Bubble down (aka Sift Down or Percolate Down) is the process of restoring the min-heap property after the root element is removed or replaced.
    - When the root (or any internal node) is out of place — typically because the last element was moved to the root position — it may violate the heap property by being greater than one or both of its children.
    - To fix this, the value is repeatedly compared to its children, and if it is greater than either, it is swapped with the smaller child. This continues until:
      - The value is no longer greater than either of its children, or
      - It reaches a leaf node (i.e., has no children)
    - This process ensures that the smallest values "sink down" toward the leaves, preserving the min-heap invariant: **Every parent node is less than or equal to its children**

`_heapify()`
- Heapify allows the conversion of a list of values into a valid binary tree representation of a heap.
  - Since `.push(value)` operates with time complexity O(log n), simply pushing all the list values onto the heap would result in time complexity O(n log n)
  - To optimize this operation, _bubble_down can be used on all the parent nodes in the binary tree, making the heap valid from leaf nodes up to the root
  - To find the last parent: `(n - 2) // 2`

## Development Notes

- This is a **min-heap** by default.

## Lessons Learned

### "Stack-Safe"
When creating the private ._bubble_down(index) method, ChatGPT brought a term to my attention: stack-safe. It refers to the danger of recursive functions causing stack overflows.
The stack refers to the call stack or "the runtime memory that tracks function calls". Each function call has a frame which gives us a helpful visual for recursive functions.
Each recursion creates a layer or a frame. The first recursion leads to the next which leads to the next which eventually leads to the final recursion. Once the final recursion is resolved,
the penultimate recursion can be resolved, and the recursion before that and before that until we get back to the first recursion and resolve it.

Previously, I was thinking of recursion as a winding and then an unwinding. There is actually a video of a brick wall being built, and the top row of bricks have been set up like dominoes.
The first brick is tipped and knocks into the next one which knocks into the next one. The first brick is resting on the second brick which is then resting on the third, so on and so forth.
Once the last brick is tipped, it is allowed to fall over flat (with no subsequent brick to prop it up), this allows all the previous bricks to also fall flat.

Anyway, this seems to be a very good physical representation of a recursive function.
Here is a [link](https://www.reddit.com/r/oddlysatisfying/comments/etunfx/the_way_these_bricks_fall_into_place/) to a reddit post of a video of this phenomenon.

Further observations:
- python has a call stack frame limit of ~1,000 frames
- nested functions also use the call stack, but obviously carry much lower risk of stack overflow than recursion.
- each frame stores:
  - local variables
  - the return address
  - arguments

### Mutable Default Arguments
Python is a excellent language because it allows you to create quickly, but at the cost of making a lot of hidden decisions on behalf of the user.
Out of sight, out of mind. When Python is working so hard in the background to pave the way, the implications of these decisions often sneak up and bite you.

I just learned that using mutable default arguments nearly guarantees unwanted behavior.
```python
def mutate_list(my_list = []):
    my_list.append("wow")
    return my_list

print(mutate_list()) # Output: ['wow']
print(mutate_list()) # Output: ['wow', 'wow']
print(mutate_list([1, 2, 3])) # Output: [1, 2, 3, 'wow']
print(mutate_list()) # Output: ['wow', 'wow', 'wow']
```
At the moment of the function definition, the mutable default list is created. It is not recreated per function call. We can see from the behavior that a list is shared by all the function calls which use the default argument.

Mutable refers to anything that can be changed in place. E.g. `list`, `dict`, `set`, `bytearray`

### DOWN GOES `unittest`! DOWN GOES `unittest`!
The late Howard Cosell was shouting in my ear as `unittest` hit the canvas. In implementing the max-heap capability, I realized that I would need to essentially double up my unit test since nearly every operation needs a set of tests for a min-heap and for a max-heap.
The clean way to accomplish this is through parameterization, or having your tests run twice: once for min-heap, once for max-heap. And `unittest`'s options for accomplishing this were ugly and verbose.
```python
import unittest

class TestHeap(unittest.TestCase):
    def test_pop(self):
        for max_heap, expected in [(False, [1, 2, 3]), (True, [3, 2, 1])]:
            with self.subTest(max_heap=max_heap):
                heap = Heap(list_of_values=[3, 1, 2], max_heap=max_heap)
                result = [heap.pop() for _ in range(3)]
                self.assertEqual(expected, result)
```
That is just the grossest thing I have ever seen(dramatic). Where do I put my "Arrange-Act-Assert"?! There is nothing glaringly wrong; it's just bad feng shui.
Here is how it is done using parameters in `pytest`:
```python
import pytest

@pytest.mark.parametrize("max_heap", [True, False])
def test_pop(max_heap):
    # Arrange
    heap = Heap(list_of_values=[3, 1, 2], max_heap=max_heap)
    expected = [3, 2, 1] if max_heap else [1, 2, 3]
    
    # Act
    results = [heap.pop() for _ in range(3)]
    
    # Assert
    assert results == expected
```
This version is so much cleaner in my opinion and I find that to be important enough to me to make the switch to `pytest`, which
is apparently the more serious unit testing python library anyway. As a result this class will feature a full test suite in `pytest`.

---

