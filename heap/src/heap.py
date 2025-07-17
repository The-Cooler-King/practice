class Heap:
    def __init__(self):
        self._data = []

    def push(self, value):
        """
        Pushes value into the heap and places it in its rightful spot

        Args
            value: the value to place in the heap
        """

        # append the value to the end of the list
        self._data.append(value)

        # bubble up the new value to the proper place
        new_value_index = len(self._data) - 1
        self._bubble_up(new_value_index)

    def _bubble_up(self, index):
        parent_index = (index - 1) // 2

        while index > 0 and self._data[index] < self._data[parent_index]:
            # switch the new value with its parent
            self._data[index], self._data[parent_index] = self._data[parent_index], self._data[index]

            # update the new_value_index
            index = parent_index

            # calculate the new parent_index
            parent_index = (index - 1) // 2

    def peek(self):
        """
        Return the smallest element in the heap without removing it.

        Returns:
            The value of the smallest element (the root), or None if the heap is empty.
        """

        if not self._data:
            return None

        return self._data[0]

    def pop(self):
        """
        Remove and return the root element of the heap

        Notes:
            This is accomplished optimally by swapping the root element with the last element of our list binary tree
            representation. Then, since the root element is now in the final spot, we can perform a native list .pop().
            After the root element has been popped, we bubble down the new root element (previously the last element).
            By comparing the new root to its children and swapping with the smallest child, we restore the min-heap
            property.
        """
        if not self._data:
            return None

        # Swap the root element and the last element
        last_index = len(self._data) - 1
        self._data[0], self._data[last_index] = self._data[last_index], self._data[0]

        # Remove the min element and save the value
        min_element_value = self._data.pop()

        # Bubble down the new root element to restore min-heap property
        self._bubble_down(0)

        return min_element_value

    def _bubble_down(self, index):
        if not self._data:
            return

        heap_length = len(self._data)

        while index < heap_length:
            left = index * 2 + 1
            right = index * 2 + 2
            smallest = index

            if left < heap_length and self._data[left] < self._data[smallest]:
                smallest = left

            if right < heap_length and self._data[right] < self._data[smallest]:
                smallest = right

            if smallest == index:
                break

            self._data[index], self._data[smallest] = self._data[smallest], self._data[index]
            index = smallest
