# 📘 Singly Linked List Module Documentation

A minimal Python implementation of a singly linked list with basic node operations. This includes common list behaviors like append, prepend, insert, remove, reverse, and indexing. Useful for learning, algorithm development, and interview preparation.

Main Classes:
- `Node`: Represents an element in the list
- `SinglyLinkedList`: Provides operations for managing a sequence of nodes

---

## 🧱 Node Class

### `Node(value, next_node=None)`

Creates a node that stores a value and optionally points to the next node.

#### Arguments:
- `value` (`any`): The value stored in the node.
- `next_node` (`Node`, optional): Reference to the next node. Defaults to `None`.

#### Methods:

##### `__repr__()`

Returns a string representation of the node, e.g. `Node(3)`.

##### `__eq__(other)`

Returns `True` if node is the comparison node.
- This method does not compare the attributes of nodes

#### Examples:

```python
n1 = Node(10)
n2 = Node(20, n1)

print(n1)  # Node(10)
print(n2)  # Node(20)
print(n2.next == n1)  # True
print(n2 == n1) # False
```

---

## 🔗 SinglyLinkedList Class

### `SinglyLinkedList()`

Initializes an empty linked list with `head` set to `None`.

### Attributes:
These attributes are internally managed and should not be manipulated externally.

- `self.head`: The head node of the list. If the list is empty, self.head will be `None`.

### Dunder Methods:

##### `__iter__()`
Allows iteration over the linked list using a `for` loop.

###### Examples:
```python
ll = SinglyLinkedList()
ll.prepend(1)
ll.prepend(2)

for value in ll:
    print(value)
# Output: 2, 1
```
---

##### `__repr__()`
Returns a string representation of the list, showing all node values.

###### Examples:
```python
ll = SinglyLinkedList()
ll.prepend(3)
ll.prepend(2)
ll.prepend(1)
print(ll)  # LinkedList([1 -> 2 -> 3])

ll.pop()
ll.pop()
ll.pop()
print(ll) # LinkedList([])
```
---

###### `__getitem__(index)`
Returns the value of the node at the given index.

###### Examples:
```python
ll = SinglyLinkedList()
ll.prepend(3)
ll.prepend(2)
ll.prepend(1)

ll[0]  # 1
ll[1]  # 2
ll[2]  # 3
```
---

### Public Methods:
These are supported methods to manipulate, analyze, and examine the SinglyLinkedList instance.

##### `prepend(value)`
Adds a new node to the front of the list.

###### Arguments:
- value (any): Value to store in the new head node.

###### Examples:
```python
ll = SinglyLinkedList()
ll.prepend(5)
ll.prepend(10)
print(ll)  # LinkedList([10 -> 5])
```
---

##### `pop()`
Removes and returns the value of the tail node

###### Returns:
- `value` of the removed node
- `None` if the list was empty

###### Examples:
```python
ll = SinglyLinkedList()
ll.prepend(1)
ll.prepend(2)
ll.pop()  # 1
ll.pop()  # 2
ll.pop()  # None
```
---

##### `reverse()`
Reverses the list in-place by flipping all node pointers.

###### Examples:
```python
ll = SinglyLinkedList()
ll.prepend(1)
ll.prepend(2)
ll.prepend(3)
print(ll)  # LinkedList([3 -> 2 -> 1])
ll.reverse()
print(ll)  # LinkedList([1 -> 2 -> 3])
```
---

##### `insert(index, value)`
Inserts a new node with the given value at the specified index.

###### Arguments:
- `index`: (int) The index at which to insert the node.
- `value`: The value to store in the new node

###### Examples:
```python
ll = SinglyLinkedList()
ll.prepend(10)
ll.prepend(20)
ll.prepend(30)
repr(ll)  # LinkedList([30 -> 20 -> 10])

ll.insert(index=2, value=15) # LinkedList([30 -> 20 -> 15 -> 10])
```
---

##### `append(value)`
Adds a new node to the end of the list.

###### Arguments:
- `value`: The value to store in the appended node

###### Examples:
```python
ll = SinglyLinkedList()
ll.append(10)
ll.append(20)
ll.append(30)
repr(ll)  # LinkedList([10 -> 20 -> 30])
```
---

##### `remove(index)`
Removes the node at the specified index.

###### Arguments:
- `index`: (int) The index at which to remove the node.

###### Examples:
```python
ll = SinglyLinkedList()
ll.prepend(10)
ll.prepend(20)
ll.prepend(30)
repr(ll)  # LinkedList([30 -> 20 -> 10])

ll.remove(index=1) # LinkedList([30 -> 10])
```
---