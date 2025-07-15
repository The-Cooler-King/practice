# Heap Class Documentation

## Overview

The `Heap` class implements a min-heap using a Python list as the internal data container. This version initializes an empty heap and lays the foundation for future heap operations.

The heap uses **0-based indexing** for internal structure.

---

## Class: `Heap`

### Constructor

```python
class Heap:
    def __init__(self):
        self._data = []
```
---

### Example Usage

```python
from heap import Heap

heap = Heap()
print(heap._data)  # Output: []
```
---

## Private Attributes

### `_data`

- **Type**: `list`
- **Description**: Stores the elements of the heap.
- **Initial Value**: An empty list.

---

## Indexing Scheme

This implementation uses **0-based indexing**, which determines relationships like so:

- **Parent of node `i`**: `(i - 1) // 2`
- **Left child of node `i`**: `2 * i + 1`
- **Right child of node `i`**: `2 * i + 2`

This scheme aligns with how Python lists naturally operate. By indexing in this way, we turn a python list into a binary tree allowing for fast traversal and maintaining of minimum value.

---
## Public Methods

### `.insert(value)`
Inserts value into the heap and places it in its rightful spot

### Example
```python
heap = Heap()
heap.insert(20)
heap.insert(5)
heap.insert(15)
heap.insert(22)
heap.insert(1)

print(heap._data) # Output: [1, 5, 15, 22, 20]
```
---
## Private Methods
- `_bubble_up(index)`
  - Bubble up (aka Sift Up or Percolate Up) is the process of restoring the min-heap property after a new element is added to the heap
  - When a new value is inserted, it is initially placed at the end of the internal list (which corresponds to the next available leaf position of the binary tree representation). However, this new value might violate the heap property by being smaller than its parent.
  - To fix this, the value is repeatedly compared to its parent, and if it's smaller, the two are swapped. This continues until:
    - The value is no longer smaller than its parent, or
    - It reaches the root of the heap
  - This process ensures that the smallest value "bubbles up" toward the top, preserving the min-heap invariant: **Every parent node is less than or equal to its children**

## Development Notes

- This is a **min-heap** by default.
- `_data` is currently a public-facing attribute for transparency during development.
- A full API will eventually abstract away direct access to `_data`.

---

## Future Roadmap

The class will expand to support:

- `extract_min()`
- `peek()`
- Internal reheapification (`_heapify_up`, `_heapify_down`)
- Optional max-heap toggle
- Input validation and robust error handling
