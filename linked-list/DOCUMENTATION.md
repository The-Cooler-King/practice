# 📘 Linked List Module Documentation

A Python module implementing a custom singly linked list from scratch, with optional index map for O(1) lookups.
Includes cycle detection, in-place reversal, and iteration support. Designed for learning, testing algorithms,
and exploring hybrid data structures.

Main Classes:
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

### Attributes:
These attributes are internally managed and should not be manipulated externally.

- `self._head`: The head node of the list. If the list is empty, self._head will be `None`.
- `self._index_map`: The map of indexes paired with their corresponding nodes.
- `self._length`: The amount of nodes in the list.

### Dunder Methods:

##### `__len__()`
Returns the amount of nodes in the list.

###### Examples:
```python
ll = LinkedList()
ll.prepend(1)
ll.prepend(2)

len(ll)  # 2
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
---

###### `__getitem__(index)`
Returns the value of the node at the given index.

###### Examples:
```python
ll = LinkedList()
ll.prepend(3)
ll.prepend(2)
ll.prepend(1)

ll[0]  # 1
ll[1]  # 2
ll[2]  # 3
```
---

###### `__setitem__(index, value)`
Sets the value of the node at the given index.

###### Examples:
```python
ll = LinkedList()
ll.prepend(3)
ll.prepend(2)
ll.prepend(1)

ll[1]  # 2
ll[1] = 4
ll[1]  # 4
```
---

### Public Methods:
These are supported methods to manipulate, analyze, and examine the LinkedList instance. If only public methods are used
to manipulate the LinkedList, the user can be assured that the list and its metadata will have reliable integrity.

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

##### `classic_pop()`
Removes and returns the value of the tail node in the list with O(N) time complexity. This method is retained for instructional purposes only. Use `pop()` for production logic.

###### Returns:
- `value` of the removed node
- `None` if the list was empty

###### Examples:
```python
ll = LinkedList()
ll.prepend(1)
ll.prepend(2)
ll.classic_pop()  # 1
ll.classic_pop()  # 2
ll.classic_pop()  # None
```
---

##### `pop()`
Removes and returns the value of the tail node in the list with O(1) time complexity.

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

##### `get_node(index)`
Returns the node object at the given index.

###### Arguments:
- `index` (int): The position of the node.

###### Returns:
- The `Node` instance at the given index.

###### Raises:
- `IndexError` if the index is out of bounds.
- `TypeError` if the index is not an integer.

###### Examples:
```python
ll = LinkedList()
ll.prepend(10)
ll.prepend(20)
node = ll.get_node(1)
print(node.value)  # 10
```
---

##### `rebuild_index_map()`
Clears the current index map, and then traverses the list from head to tail, assigning a index to each node.

###### Examples:
```python
ll = LinkedList()
ll.prepend(10)
ll.prepend(20)
ll._index_map  # {0: Node(20), 1: Node(10)}
ll.index_map = {}

ll.rebuild_indes_map()
ll._index_map  # {0: Node(20), 1: Node(10)}
```
---

##### `validate_index_map()`
Validates the integrity of the index map by ensuring each indexed node in the map corresponds exactly to the node at that position in the linked list.

###### Returns:
- __Boolean__: `True` if index map is valid, `False` otherwise

###### Examples:
```python
ll = LinkedList()
ll.prepend(10)
ll.prepend(20)
ll._index_map  # {0: Node(20), 1: Node(10)}
ll.validate_index_map()  # True

ll.index_map = {}
ll.validate_index_map()  # False
```
---

##### `insert(index, value)`
Inserts a new node with the given value at the specified index.

###### Arguments:
- `index`: (int) The index at which to insert the node.
- `value`: The value to store in the new node

###### Examples:
```python
ll = LinkedList()
ll.prepend(10)
ll.prepend(20)
ll.prepend(30)
repr(ll)  # LinkedList([30 -> 20 -> 10])

ll.insert(index=2, value=15) # LinkedList([30 -> 20 -> 15 -> 10])
```
---

##### `append(value)`
Removes the node at the specified index.

###### Arguments:
- `value`: The value to store in the appended node

###### Examples:
```python
ll = LinkedList()
ll.append(10)
ll.append(20)
ll.append(30)
repr(ll)  # LinkedList([10 -> 20 -> 30])
```
---

##### `remove(index, value)`
Removes the node at the specified index.

###### Arguments:
- `index`: (int) The index at which to remove the node.

###### Examples:
```python
ll = LinkedList()
ll.prepend(10)
ll.prepend(20)
ll.prepend(30)
repr(ll)  # LinkedList([30 -> 20 -> 10])

ll.remove(index=1) # LinkedList([30 -> 10])
```
---

#### Private Methods:

### 🔧 Internal Methods

#### `_rebuild_index_map_partial(start_index, start_node)`
Incrementally rebuilds the index map starting from `start_index` and `start_node`.

Use only when it is known that preceding mappings are already correct. If in doubt, use `rebuild_index_map()`.

#### `_add_node_to_index_map(index, node)`
Adds an entry to the index map and updates mappings for all downstream nodes.

#### `_remove_node_from_index_map(index)`
Removes the specified index and rebuilds mappings for subsequent nodes if needed.

#### `_increment_list_length()` / `_decrement_list_length()`
Internal counters for maintaining list length.

#### `_update_list_metadata_for_add_node()` / `_update_list_metadata_for_remove_node()`
Helper methods that bundle together all index map and length updates for adding or removing nodes.

#### `_validate_index()`
Helper methods that ensures index is an integer and within the bounds. Used to validate index at the start of public methods that take index as an arg.
