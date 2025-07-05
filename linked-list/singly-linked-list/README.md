# 🔗 Singly Linked List

## Overview

A minimalist, custom-built **singly linked list** implementation in Python. Built from scratch to reinforce core algorithmic thinking, pointer manipulation, and robust object-oriented design.

Includes:

- `Node`: Stores a value and a pointer to the next node
- `SinglyLinkedList`: Manages the chain of nodes and supports common list operations

---

## 📦 Standard Features

| Method              | Description                                      |
|---------------------|--------------------------------------------------|
| `append(value)`     | Add a node to the end of the list                |
| `prepend(value)`    | Add a node to the front of the list              |
| `insert(index, v)`  | Insert a node at a specified index               |
| `remove(index)`     | Remove the node at a specified index             |
| `pop()`             | Remove and return the last node                  |
| `reverse()`         | Reverse the list in-place                        |
| `__getitem__()`     | Index into the list using brackets (`list[2]`)   |
| `__iter__()`        | Iterate through the list                         |
| `__repr__()`        | Pretty string output                             |

---

## 🧱 Node Example

```python
from Node import Node

node = Node(5)
next_node = Node(10, node)
print(node)           # Node(5)
print(next_node.next) # Node(5)
```

## 🚀 Usage
```python
from SinglyLinkedList import SinglyLinkedList

ll = SinglyLinkedList()
ll.append(1)
ll.append(2)
ll.append(3)

print(ll)       # LinkedList([1 -> 2 -> 3])
print(ll[1])    # 2

ll.reverse()
print(ll)       # LinkedList([3 -> 2 -> 1])

ll.remove(1)
print(ll)       # LinkedList([3 -> 1])
```

## 🧪 Testing
Tests are written using Python’s unittest framework. From the root directory:

```bash
python -m unittest discover -s tests
```

## 🧠 Design Principles
- `Pointer Management`: Manually handle next references for every node.
- `Safety First`: Defensive programming ensures clean error handling (e.g. invalid indices).
- `Pythonic Interface`: Implements dunder methods like __repr__, __iter__, __getitem__ for ease of use.