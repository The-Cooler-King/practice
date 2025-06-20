class Stack:
    """
    A stack data structure that supports push, pop, and retrieving the maximum element in O(1) time.

    Internally maintains two lists:
    - `stack`: stores all the pushed items.
    - `max_stack`: stores the maximum elements, allowing constant time max retrieval.
    """

    def __init__(self):
        """
        Initializes an empty Stack instance.
        """
        self.stack = []
        self.max_stack = []

    def _is_int(self, item):
        """
        Check if the given item is an integer.

        Parameters:
            item (any): The item to check.

        Returns:
            bool: True if item is an integer, False otherwise.
        """
        return isinstance(item, int)

    def append_item(self, item):
        """
        Push an integer item onto the stack.

        Also updates the max_stack to maintain the current maximum element.

        Parameters:
            item (int): The integer item to add to the stack.

        Raises:
            ValueError: If the item is not an integer.
        """
        if not self._is_int(item):
            raise ValueError("This stack does not accept non-integers")

        self.stack.append(item)

        if not self.max_stack:
            self.max_stack.append(item)
        elif item >= self.max_stack[-1]:
            self.max_stack.append(item)

    def delete_item(self):
        """
        Pop the top item from the stack.

        Also updates the max_stack if the popped item was the current maximum.

        Returns:
            int: The item removed from the top of the stack.

        Raises:
            IndexError: If the stack is empty.
        """
        if not self.stack:
            raise IndexError("Cannot perform delete. The stack is empty")

        popped_item = self.stack.pop()
        if popped_item == self.max_stack[-1]:
            self.max_stack.pop()

        return popped_item

    def get_max_item(self):
        """
        Retrieve the maximum element currently in the stack.

        Returns:
            int: The current maximum item.

        Raises:
            IndexError: If the stack is empty.
        """
        if not self.stack:
            raise IndexError("Cannot retrieve max. The stack is empty")

        return self.max_stack[-1]

    def __repr__(self):
        """
        Return a string representation of the stack and the max_stack.

        Returns:
            str: A string showing the stack contents and the max_stack contents.
        """
        return f"Stack({self.stack}), Max({self.max_stack})"


# Example usage
my_stack = Stack()  # []

my_stack.append_item(0)  # [0]
print(my_stack.get_max_item())  # 0

my_stack.append_item(100)  # [0, 100]
print(my_stack.get_max_item())  # 100

my_stack.delete_item()  # [0]
print(my_stack.get_max_item())  # 0

my_stack.delete_item()  # []

try:
    my_stack.get_max_item()
except Exception as e:
    print(repr(e))

try:
    my_stack.delete_item()
except Exception as e:
    print(repr(e))

try:
    my_stack.append_item("A")
except Exception as e:
    print(repr(e))
