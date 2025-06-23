# 📘 Linked List Module Documentation

This module implements a basic singly linked list using two core classes:

- `Node`: Represents an element in the list
- `LinkedList`: Provides operations for managing a sequence of nodes

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
n2 = Node(10, n1)

print(n1)  # Node(10)
print(n2)  # Node(20)
print(n2.next == n1)  # True
print(n2 == n1) # False
```

---

## 🔗 LinkedList Class

### `LinkedList()`

Initializes an empty linked list with `head` set to `None`.

#### Methods:

##### `head()`
Returns the head node of the list

###### Examples:
```python
ll = LinkedList()
ll.prepend(5)
ll.prepend(10)
print(ll.head().value)  # 5
```
---

##### `prepend(value)`
Adds a new node to the front of the list.

###### Arguments:
- value (any): Value to store in the new head node.

###### Examples:
```python
ll = LinkedList()
ll.prepend(5)
ll.prepend(10)
print(ll)  # LinkedList([10 -> 5])
```
---

##### `pop()`
Removes and returns the value of the last node in the list.

###### Returns:
- `value` of the removed node
- `None` if the list was empty

###### Examples:
```python
ll = LinkedList()
ll.prepend(1)
ll.prepend(2)
ll.pop()  # 1
ll.pop()  # 2
ll.pop()  # None
```
---

##### `is_empty()`
Returns `True` if the list has no nodes, else `False`.

###### Examples:
```python
ll = LinkedList()
ll.is_empty()  # True
ll.prepend(3)
ll.is_empty()  # False
```
---

##### `has_cycle()`
Uses Floyd's Tortoise-Hare algorithm to check for cycles in the list.

###### Returns:
- `True` if the list contains a cycle
- `False` otherwise

###### Examples:
```python
a = Node(1)
b = Node(2, a)
a.next = b  # cycle

ll = LinkedList()
ll._head = a # DO NOT DO THIS. Use public methods to affect the list instance
ll.has_cycle()  # True
```
---

##### `find_middle()`
Finds and returns the value of the middle node using the Tortoise-Hare strategy.

###### Returns:
- `value` of the middle node

###### Raises:
- `RuntimeError` if list is empty or contains a cycle

###### Notes:
- In an even-length list, returns the second of the two middle nodes.

###### Examples:
```python
ll_odd = LinkedList()
for i in [1, 2, 3, 4, 5]:
    ll_odd.prepend(i)  # list: 5 -> 4 -> 3 -> 2 -> 1

ll_odd.find_middle()  # 3

ll_odd.pop()
ll_even = ll_odd # list: 5 -> 4 -> 3 -> 2

ll_even.find_middle() # 3

ll_empty = LinkedList()
ll_empty.find_middle() # RuntimeError
```
---

##### `reverse()`
Reverses the list in-place by flipping all node pointers.

###### Raises:
- `RuntimeError` if list contains a cycle

###### Examples:
```python
ll = LinkedList()
ll.prepend(1)
ll.prepend(2)
ll.prepend(3)
print(ll)  # LinkedList([3 -> 2 -> 1])
ll.reverse()
print(ll)  # LinkedList([1 -> 2 -> 3])
```
---

##### `__iter__()`
Allows iteration over the linked list using a `for` loop.

###### Raises:
- `RuntimeError` if list contains a cycle

###### Examples:
```python
ll = LinkedList()
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
ll = LinkedList()
ll.prepend(3)
ll.prepend(2)
ll.prepend(1)
print(ll)  # LinkedList([1 -> 2 -> 3])

ll.pop()
ll.pop()
ll.pop()
print(ll) # Empty List
```

###### Cycle Safety:
If a cycle is detected, prints up to the first repeated node and then:
```python
LinkedList([1 -> 2 -> 3 -> 1 ... (cycle detected)])
```
