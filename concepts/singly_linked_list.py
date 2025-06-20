class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        # TODO: initiate a hash map
        # TODO: modify the insert, prepend, append, delete methods to update the hashmap
        # TODO: create helper function to rebuild the hashmap
        self.index_map = {}
        self.head = None
        self.list_length = 0

    def append(self, value):
        """Add a node to the end of the list"""
        # initiate new node using the node class
        new_node = Node(value)

        # if no node exists, make this new node the head
        if not self.head:
            self.head = new_node
            self.index_map[0] = new_node
            self.list_length += 1
            return

        # loop through to the end of the find the last node
        current_node = self.head
        while current_node.next:
            current_node = current_node.next

        # append the new node to the last node by setting the last node's .next property to the new node
        current_node.next = new_node
        self.index_map[self.length()] = new_node
        self.list_length += 1

    def prepend(self, value):
        """Add a node to the front of the list"""
        # initiate new node using the node class
        new_node = Node(value)

        # set the .next property of the new node to the current head of the list
        new_node.next = self.head

        # make the new node the head of the list
        self.head = new_node
        self.list_length += 1

        # clear and rebuild the index map
        self.index_map = {}
        self._rebuild_index_map(
            current_node=self.head,
            index=0
        )

    def _rebuild_index_map(self, current_node, index):
        """Rewrites the index map hash map for all nodes including and after the current node at index"""
        # rebuild index_map from index and on to account for the mutation
        while current_node:
            self.index_map[index] = current_node
            current_node = current_node.next
            index += 1

    def pop(self):
        """Remove the last node in the list and return value"""
        # if list is empty, return None
        if not self.head:
            return None

        # if self.head is the only node, return its value and remove it
        if not self.head.next:
            value = self.head.value
            self.head = None
            del self.index_map[self.length() - 1]
            self.list_length -= 1
            return value

        # Loop until we reach the penultimate node
        current_node = self.head
        while current_node.next.next:
            current_node = current_node.next

        # get the value of the final node
        value = current_node.next.value
        # set the penultimate node's next property to None
        current_node.next = None
        del self.index_map[self.length() - 1]
        self.list_length -= 1
        # return the final node's value
        return value

    def delete(self, value):
        """Remove the first occurrence of a value from the list"""
        # if list is empty do nothing
        if not self.head:
            return

        # if self.head.value is the value, delete it by setting self.head equal to its next node
        if self.head.value == value:
            self.head = self.head.next
            self._rebuild_index_map(
                current_node=self.head,
                index=0
            )
            self.list_length -= 1
            return

        # loop through the nodes until there is no next node (end of list) and the next node is not equal to the value
        current_node = self.head
        index = 0
        while current_node.next and current_node.next.value != value:
            current_node = current_node.next
            index += 1

        # if there is a next node, that means that the while loop was stopped before the end of the list
        # if it was stopped before the end of the list, that means it encountered the value in current_node.next
        # NOTE: initially this confused me. why do we not need to check the value of the next node? Well the second part
        # of the while loop's conditional checks the value of the next node, meaning we could not get to the end of the
        # list if the value was present in the list. If the value is in the list, the loop will stop on the node prior
        if current_node.next:
            current_node.next = current_node.next.next
            self._rebuild_index_map(
                current_node=current_node.next,
                index=index + 1
            )
            self.list_length -= 1

    # TODO: return index instead of the node?
    def find(self, value):
        """Return the first node with the given value, or None"""
        # loop through the nodes and return the node if value is encountered
        current_node = self.head
        while current_node:
            if current_node.value == value:
                return current_node
            current_node = current_node.next

        # if the loop was complete, the value was not present. Return None
        return None

    def to_list(self):
        """Return a list of all values in the linked list"""
        # initiate an empty list to store values
        result = []

        # loop through the list values and append to the result
        current_node = self.head
        while current_node:
            result.append(current_node.value)
            current_node = current_node.next

        # after loop complete, return the result
        return result

    def length(self):
        """Returns the number of Nodes in the list"""
        return self.list_length

    def insert(self, index: int, value):
        """Inserts a node of value at index"""
        # if the index is negative or is greater the length of the list, it is out of bounds
        if index < 0 or index > self.length():
            raise IndexError("Index out of bounds")

        if index == 0:
            self.prepend(value)
            return
        if index == self.length():
            self.append(value)
            return

        # we have the edge cases of index 0 and append to last node, so now we will only be inserting from after the
        # head to before the tail
        index_counter = 0
        current_node = self.head
        # loop through the list until we hit the node before the index
        while index - 1 != index_counter:
            current_node = current_node.next
            index_counter += 1

        # initiate new node
        new_node = Node(value)
        # set the new node's next to the current node's next
        new_node.next = current_node.next
        # set the current node's next to the new node
        current_node.next = new_node
        self._rebuild_index_map(
            current_node=new_node,
            index=index
        )
        self.list_length += 1

    def index_value(self, index):
        """Returns the node at index"""
        # if the index is negative or is greater the length of the list, it is out of bounds
        if index < 0 or index >= self.length():
            raise IndexError("Index out of bounds")

        return self.index_map[index].value

    def reverse(self):
        """Reverses the order of the nodes"""
        previous_node = None
        current_node = self.head

        while current_node:
            next_node = current_node.next  # store the node after current
            current_node.next = previous_node  # set the current nodes next to the previous node
            previous_node = current_node  # store the current node now as the previous
            current_node = next_node  # set the current node to the next node
        # so as we move along the list, we are reversing the pointer that goes from current to next to go from next to
        # current

        self.head = previous_node
        self.index_map = {}
        self._rebuild_index_map(
            current_node=self.head,
            index=0
        )

    def has_cycle(self):
        """Returns True if the list has a cycle (a node pointing back to a previous node)"""
        # for this we need to have a pointer that jumps two nodes at a time and a pointer that jumps a node at a time
        # if there is a cycle the hare will catch the tortoise, if there is no cycle, the hare will reach the end
        tortoise_pointer = self.head
        hare_pointer = self.head

        while hare_pointer and hare_pointer.next:
            tortoise_pointer = tortoise_pointer.next
            hare_pointer = hare_pointer.next.next
            if tortoise_pointer == hare_pointer:
                return True

        return False

    def __iter__(self):
        """Allow list to be iterated over"""
        current_node = self.head
        while current_node:
            yield current_node.value
            current_node = current_node.next

    def __repr__(self):
        """Allow list to be printed"""
        return " -> ".join(str(value) for value in self) or "Empty List"

# TODO: add __set_item__ and __get_item__ methods
# TODO: add __len__ method to replace length
# TODO: add a remove at index function
# TODO: add clear function
# TODO: contains(value) – add value in linked_list support via __contains__


# Create a new list
ll = SinglyLinkedList()

# Append some values
ll.append(10)
ll.append(20)
ll.append(30)
print("After appends:", ll)  # 10 -> 20 -> 30

# Prepend a value
ll.prepend(5)
print("After prepend:", ll)  # 5 -> 10 -> 20 -> 30

# Insert at index
ll.insert(2, 15)
print("After inserting 15 at index 2:", ll)  # 5 -> 10 -> 15 -> 20 -> 30

# Get index_value
print("Value at index 3:", ll.index_value(3))  # 20

# Pop last element
popped = ll.pop()
print("Popped value:", popped)  # 30
print("After pop:", ll)  # 5 -> 10 -> 15 -> 20

# Delete a value
ll.delete(10)
print("After deleting 10:", ll)  # 5 -> 15 -> 20

# Find a value
found_node = ll.find(15)
print("Found value 15:", found_node.value if found_node else "Not found")  # 15

# Convert to Python list
as_list = ll.to_list()
print("As regular list:", as_list)  # [5, 15, 20]

# Get length
print("Length of list:", ll.length())  # 3

# Reverse the list
ll.reverse()
print("After reverse:", ll)  # 20 -> 15 -> 5

# Check for cycle (should be False)
print("Has cycle?", ll.has_cycle())  # False

# Test __iter__ by converting to list again
print("Iterated values:", [val for val in ll])  # [20, 15, 5]

