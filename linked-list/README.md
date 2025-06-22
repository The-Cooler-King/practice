# Linked List Module

## Overview

This module implements a singly linked list in Python from scratch, designed for educational use and algorithm practice. It includes two core classes:

- `Node`: Represents a single element in the list, containing a value and a reference to the next node.
- `LinkedList`: Provides a collection of nodes and various methods for working with them (e.g., prepend, pop, reverse, detect cycle, find middle).

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
- `pop()` – Removes and returns the last node
- `has_cycle()` – Uses Floyd’s Tortoise-Hare algorithm to detect a cycle
- `find_middle()` – Efficiently finds the middle node of the list
- `reverse()` – Reverses the list in-place
- `__iter__()` and `__repr__()` – Pythonic support for iteration and printing

### Lessons Learned
- `Cycle Detection`: Algorithms must guard against cycles to prevent infinite loops in iteration and string conversion.
- `In-Place Reversal`: Managing pointer flipping can be complex; visualizing the node chain helps.
- `Robustness`: Defensive programming practices (e.g., has_cycle checks) make this implementation resilient.
- `Testing Philosophy`: Unit tests use the unittest module and follow the arrange-act-assert format for readability.

### Testing
This module is thoroughly tested using Python's unittest framework.

To run tests from `DataAnnotationApplicationPrompt\linked-list`:
```commandline
python -m unittest discover -s tests
```

### Where We Are Headed
 - Add documentation
 - Add O(1) lookups with indexes
 - Build new features enabled by indexed lookups
 - Transition to doubly linked list
 - Build new features enables by double link
 - Add benchmark comparisons against Python's native list