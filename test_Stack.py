import unittest

from stack_class import Stack  # Change to match your actual file name if needed


class TestStack(unittest.TestCase):

    def test_append_and_get_max_with_one_item(self):
        # Arrange
        stack = Stack()

        # Act
        stack.append_item(42)
        result = stack.get_max_item()

        # Assert
        self.assertEqual(result, 42)

    def test_append_multiple_and_get_max(self):
        # Arrange
        stack = Stack()

        # Act
        stack.append_item(5)
        stack.append_item(1)
        stack.append_item(10)
        stack.append_item(7)
        result = stack.get_max_item()

        # Assert
        self.assertEqual(result, 10)

    def test_delete_and_get_max_updates_correctly(self):
        # Arrange
        stack = Stack()
        stack.append_item(3)
        stack.append_item(9)
        stack.append_item(5)

        # Act
        stack.delete_item()  # removes 5
        result = stack.get_max_item()

        # Assert
        self.assertEqual(result, 9)

    def test_delete_top_max_value_removes_from_max_stack(self):
        # Arrange
        stack = Stack()
        stack.append_item(4)
        stack.append_item(10)

        # Act
        stack.delete_item()  # removes 10
        result = stack.get_max_item()

        # Assert
        self.assertEqual(result, 4)

    def test_get_max_raises_on_empty_stack(self):
        # Arrange
        stack = Stack()

        # Act & Assert
        with self.assertRaises(IndexError):
            stack.get_max_item()

    def test_delete_item_raises_on_empty_stack(self):
        # Arrange
        stack = Stack()

        # Act & Assert
        with self.assertRaises(IndexError):
            stack.delete_item()

    def test_append_non_integer_raises_value_error(self):
        # Arrange
        stack = Stack()

        # Act & Assert
        with self.assertRaises(ValueError):
            stack.append_item("hello")

    def test_repr_output(self):
        # Arrange
        stack = Stack()
        stack.append_item(1)
        stack.append_item(5)

        # Act
        result = repr(stack)

        # Assert
        self.assertEqual(result, "Stack([1, 5]), Max([1, 5])")


if __name__ == "__main__":
    unittest.main()
