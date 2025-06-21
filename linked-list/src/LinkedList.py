from Node import Node

class LinkedList:
    def __init__(self):
        """
        Initializes an empty singly linked list
        Sets the head to None
        """
        self.head = None

    def is_empty(self) -> bool:
        """
        Returns True if the list is empty, False otherwise.
        """
        return self.head is None

    def prepend(self, value):
        """
        Adds a node to the fron or the head of the linked list

        Args:
            value: The value to store in the node that will be prepended
        """
        new_node = Node(value)

        if not self.head:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def pop(self):
        """
        Takes the node from the end of the list

        Return: the value of the removed node
        """
        if not self.head:
            return None

        if not self.head.next:
            tail_value = self.head.value
            self.head = None
            return tail_value

        current_node = self.head
        while current_node.next.next: # stop at the penultimate node
            current_node = current_node.next

        tail_value = current_node.next.value
        current_node.next = None
        return tail_value
