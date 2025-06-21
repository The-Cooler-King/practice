class Node:
    def __init__(self, value: object, next_node: 'Node' = None):
        """
        Initializes a Node with a value and an optional reference to the next node.

        Args:
            value: The value to store in the node.
            next_node (Node, optional): The next node in the list. Defaults to None.
        """
        self.value = value
        self.next = next_node

    def __repr__(self) -> str:
        """
        Helps with debugging and testing.
        """
        return f"Node({self.value})"

    def __eq__(self, other: object) -> bool:
        """
        Enables object comparison in tests (e.g. self.assertEquals(node, Node(3)) )
        """
        if not isinstance(other, Node):  # check if other is a also an instance of the Node class
            return False

        return self.value == other.value and self.next == other.next
