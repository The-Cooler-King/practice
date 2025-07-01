from Node import Node


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        """
        Appends a new node with the given value to the end of the list.

        Args:
            value: The value to store in the new node.
        """
        new_node = Node(value)

        if not self.head:
            self.head = new_node
            return

        current_node = self.head
        while current_node.next:  # stop on the tail node
            current_node = current_node.next

        current_node.next = new_node

    def prepend(self, value):
        """
        Adds a new node with the given value to the front of the list.

        Args:
            value: The value to store in the new node.
        """
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def pop(self):
        """
        Removes and returns the value of the last node in the list.

        Returns:
            The value of the removed node, or None if the list is empty.
        """
        if not self.head:
            return None

        if not self.head.next:
            value = self.head.value
            self.head = None
            return value

        current_node = self.head
        while current_node.next.next:  # stop at the penultimate node
            current_node = current_node.next

        value = current_node.next.value
        current_node.next = None
        return value

    def insert(self, index, value):
        """
        Inserts a new node with the given value at the specified index.

        Args:
            index (int): Position to insert the new node.
            value: The value to store in the new node.

        Raises:
            IndexError: If the index is out of bounds.
            TypeError: If the index is not an integer.
        """
        if not isinstance(index, int):
            raise TypeError("Index must be an integer.")
        if index < 0:
            raise IndexError("Index out of bounds.")

        new_node = Node(value)

        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return

        index_counter = 1
        previous_node = self.head
        current_node = self.head.next

        while index != index_counter:
            if not current_node:
                raise IndexError("Index out of bounds.")
            previous_node = current_node
            current_node = current_node.next
            index_counter += 1

        previous_node.next = new_node
        new_node.next = current_node

    def remove(self, index):
        """
        Removes the node at the specified index from the list.

        Args:
            index (int): The index of the node to remove.

        Raises:
            IndexError: If the index is out of bounds or the list is empty.
            TypeError: If the index is not an integer.
        """
        if not isinstance(index, int):
            raise TypeError("Index must be an integer.")
        if index < 0:
            raise IndexError("Index out of bounds.")
        if not self.head:
            raise IndexError("Index out of bounds. List is empty.")

        if index == 0:
            self.head = self.head.next
            return

        index_counter = 1
        previous_node = self.head
        current_node = self.head.next

        while index != index_counter:
            if not current_node:
                raise IndexError("Index out of bounds.")
            previous_node = current_node
            current_node = current_node.next
            index_counter += 1

        if not current_node:
            raise IndexError("Index out of bounds.")
        previous_node.next = current_node.next

    def __getitem__(self, index):
        """
        Allows bracket-style indexing into the linked list.

        Args:
            index (int): The index of the node to retrieve.

        Returns:
            The value of the node at the given index.

        Raises:
            IndexError: If the index is out of bounds.
            TypeError: If the index is not an integer.
        """
        if not isinstance(index, int):
            raise TypeError("Index must be an integer.")
        if index < 0:
            raise IndexError("Index out of bounds.")

        index_counter = 0
        current_node = self.head

        while current_node:
            if index == index_counter:
                return current_node.value
            current_node = current_node.next
            index_counter += 1

        raise IndexError("Index out of bounds.")

    def __iter__(self):
        """
        Allows iteration over the linked list values.
        """
        current_node = self.head
        while current_node:
            yield current_node.value
            current_node = current_node.next

    def __repr__(self):
        """
        Returns a string representation of the linked list.
        """
        if not self.head:
            return "LinkedList([])"

        current_node = self.head
        node_values = []

        while current_node:
            node_values.append(str(current_node.value))
            current_node = current_node.next

        return "LinkedList([" + " -> ".join(node_values) + "])"
