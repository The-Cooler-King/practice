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