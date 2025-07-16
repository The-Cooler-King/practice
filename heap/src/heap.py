class Heap:
    def __init__(self):
        self._data = []

    def insert(self, value):
        """
        Inserts value into the heap and places it in its rightful spot

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

