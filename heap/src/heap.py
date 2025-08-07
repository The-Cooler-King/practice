import warnings

class Heap:
    def __init__(self, list_of_values=None, max_heap=False):
        # handle incoming data
        self._data = list(list_of_values) if list_of_values is not None else []

        # set min-heap or max-heap property
        if max_heap:
            self._min_max_multiplier = -1
            self._data = [-element for element in self._data]
        else:
            self._min_max_multiplier = 1

        # heapify incoming data
        self._heapify()

    def push(self, value):
        """
        Pushes value into the heap and places it in its rightful spot

        Args
            value: the value to place in the heap
        """
        # adjust value based on max_heap flag
        value = self._min_max_multiplier * value

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

        return self._min_max_multiplier * self._data[0]

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

        return self._min_max_multiplier * min_element_value

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

    def _heapify(self):
        """
        Rearranges the internal list (_data) in-place to satisfy the min-heap property.
        This uses a bottom-up approach for O(n) performance.
        """
        last_parent = (len(self._data) - 2) // 2

        for index in reversed(range(last_parent + 1)):
            self._bubble_down(index)

    def is_min_heap(self):
        """
        Returns True if this heap is a min-heap, False if it is a max-heap
        """
        return self._min_max_multiplier == 1

    def toggle_heap_type(self):
        """
        Converts this heap to its opposite heap type (min-heap to max-heap and vice versa). All internal values are
        inverted and the heap property is restored
        """
        self._min_max_multiplier *= -1
        self._data = [-element for element in self._data]
        self._heapify()

    def __repr__(self):
        """
        Return a concise string representation showing heap type,
        size, and root value.
        """
        heap_type = "MinHeap" if self.is_min_heap() else "MaxHeap"
        return f"{heap_type}(size={len(self)}, root={self.peek()})"

    def __iter__(self):
        """
        Iterate over heap elements in pop order (sorted order).
        Yields elements by repeatedly popping from a copy of the heap.

        Warns if heap size > 1000 due to potential performance issues.
        """
        if len(self) > 1000:
            warnings.warn("Iterating over large heap (>1,000 elements); performance may degrade.", RuntimeWarning)

        if self.is_min_heap():
            max_heap = False
            data_copy = self._data.copy()
        else:
            max_heap = True
            data_copy = [-element for element in self._data]

        heap_copy = Heap(
            list_of_values=data_copy,
            max_heap=max_heap
        )

        while heap_copy:
            yield heap_copy.pop()

    def __bool__(self):
        return bool(self._data)

    def __len__(self):
        return len(self._data)

    def __contains__(self, item):
        return item * self._min_max_multiplier in self._data
