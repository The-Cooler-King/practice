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

## Internal Attributes

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

This scheme aligns with how Python lists naturally operate.

---

## Development Notes

- This is a **min-heap** by default.
- `_data` is currently a public-facing attribute for transparency during development.
- A full API will eventually abstract away direct access to `_data`.

---

## Future Roadmap

The class will expand to support:

- `insert(value)`
- `extract_min()`
- `peek()`
- Internal reheapification (`_heapify_up`, `_heapify_down`)
- Optional max-heap toggle
- Input validation and robust error handling
