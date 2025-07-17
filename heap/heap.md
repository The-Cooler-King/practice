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
heap = Heap()
heap.push(20)
heap.push(5)
heap.push(15)
heap.push(22)
heap.push(1)

print(heap._data) # Output: [1, 5, 15, 22, 20]
print(heap.pop()) # Output: 1
print(heap._data) # Output: [5, 20, 15, 22]
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

## Development Notes

- This is a **min-heap** by default.
- `_data` is currently a public-facing attribute for transparency during development.
- A full API will eventually abstract away direct access to `_data`.

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

---

## Future Roadmap

The class will expand to support:

- `extract_min()`
- `peek()`
- Internal reheapification (`_heapify_up`, `_heapify_down`)
- Optional max-heap toggle
- Input validation and robust error handling
