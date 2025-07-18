# Heap Class Documentation

## Overview

The `Heap` class implements a min-heap using a Python list as the internal data container. This version initializes a list of values as a heap and provides heap operations.

The heap uses **0-based indexing** for internal structure.

---

## Class: `Heap`

### Constructor

```python
def __init__(self, list_of_values=None):
    self._data = list(list_of_values) if list_of_values is not None else []
    self._heapify()
```
---

### Example Usage

```python
from heap import Heap

empty_heap = Heap()
print(empty_heap._data)  # Output: []

populated_heap = Heap([3, 7, 1, 5, 10])
print(populated_heap._data) # Output: [1, 5, 3, 7, 10]
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
heap = Heap([20, 5, 15, 22, 1])

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

---

## Future Roadmap

The class will expand to support:

- `extract_min()`
- `peek()`
- Internal reheapification (`_heapify_up`, `_heapify_down`)
- Optional max-heap toggle
- Input validation and robust error handling
