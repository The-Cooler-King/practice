# Linked List Module

## Overview

This module implements a custom singly linked list in Python with an optional index map for O(1) lookups—blending a simple data structure behavior with enhanced performance. It was built from scratch for educational purposes, hands-on algorithm practice, and clean code design.

- `Node`: Represents a single element in the list, containing a value and a pointer to the next node.
- `LinkedList`: Manages a collection of nodes and exposes methods for manipulating and analyzing.

---

## Usage

### Create a Node
```python
from Node import Node

node = Node(5)
next_node = Node(10, node)
```

### Create and Use a Linked List
```python
from LinkedList import LinkedList

ll = LinkedList()
ll.prepend(3)
ll.prepend(2)
ll.prepend(1)

print(ll)  # LinkedList([1 -> 2 -> 3])
print(ll.pop())  # 3
```

### Key Features
- `prepend(value)` – Adds a node to the front of the list
- `pop()` – Removes and returns the tail node (O(1) with index map)
- `has_cycle()` – Uses Floyd’s Tortoise-Hare algorithm to detect a cycle
- `find_middle()` – Efficiently finds the middle node of the list
- `reverse()` – Reverses the list in-place
- `__getitem__(index)` - Access value at a given index using bracket notation.
- `__iter__()`, `__repr__()`, `__len__()`– Pythonic iteration, printing, length

### Lessons Learned
- `Cycle Detection`: Algorithms must guard against cycles to prevent infinite loops in iteration and string conversion.
- `In-Place Reversal`: Managing pointer flipping can be complex; visualizing the node chain helps.
- `Robustness`: Defensive programming practices (e.g., has_cycle checks) make this implementation resilient.
- `Testing Philosophy`: Unit tests use the unittest module and follow the arrange-act-assert format for readability.
- `Indexing`: Indexing transforms a linked list into a hybrid structure with powerful capabilities, but the index must be managed carefully internally to maximize performance.

### Indexing Implementation
This change made obvious the importance of public and internal methods. A corrupted index map is anti-useful, and exposing the management of the index to public use raises the risk of corrupting the index map.
A series of internal methods were constructed to carefully manage the index map, without sacrificing performance for robustness. The methods are brittle, but fast.
A safe method was made publicly available to completely rebuild the index map from scratch which ensures integrity.

### Testing
This module is thoroughly tested using Python's unittest framework.

To run tests from `DataAnnotationApplicationPrompt\linked-list`:
```commandline
python -m unittest discover -s tests
```

### Where We Are Headed
 - Build new features enabled by indexed lookups
 - Transition to doubly linked list
 - Build new features enables by double link
 - Add benchmark comparisons against Python's native list