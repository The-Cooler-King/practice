from Node import Node


class LinkedList:
    def __init__(self):
        """
        Initializes an empty singly linked list
        Sets the head to None
        Initializes empty index map
        Sets list length to 0
        """
        self._head = None
        self._index_map = {}
        self._list_length = 0

    def head(self):
        """
        Return the head of the list
        """
        return self._head

    def is_empty(self) -> bool:
        """
        Returns True if the list is empty, False otherwise.
        """
        return self._head is None

    def rebuild_index_map(self):
        """
        Rebuilds index map from scratch.
        """
        self._index_map = {}
        self._rebuild_index_map_partial(start_index=0, start_node=self._head)

    def _rebuild_index_map_partial(self, start_index: int, start_node: Node):
        """
        Rebuilds a portion of the index map starting from the given index and node.

        This internal method assumes that the provided start_index and start_node
        accurately reflect the correct position of the node within the list. It updates
        self._index_map in place by traversing from start_node and assigning sequential
        indices starting from start_index.

        Args:
            start_index (int): The index to begin assigning to start_node.
            start_node (Node): The node at which to begin rebuilding the index map.

        NOTE:
            This method performs no validation of inputs. It is intended for internal use
            only, where the correctness of inputs is assumed.
            If index map must be fully rebuilt, use the public `rebuild_index_map()` method instead.
        """
        current_node = start_node
        index = start_index

        while current_node:
            self._index_map[index] = current_node
            index += 1
            current_node = current_node.next

    def validate_index_map(self):
        """
        Validates the integrity of the index map by ensuring each indexed node in the map corresponds exactly
        to the node at that position in the linked list.

        Returns:
            bool: True if the index map is accurate and consistent with the current list structure;
                  False if there are stale entries, missing entries, or incorrect mappings.

        Use Cases:
            - Debugging: Helps detect stale or corrupted index map entries.
            - Testing: Can be used in unit tests to assert internal consistency after list operations.
        """
        current_node = self._head
        index = 0

        if len(self._index_map) != self._list_length:  # if there are a different number of nodes than index mappings
            return False

        while current_node:
            if index not in self._index_map or self._index_map[index] != current_node:
                return False
            index += 1
            current_node = current_node.next

        return True

    def _remove_node_from_index_map(self, index):
        """
        Deletes the index, Node pair from self._index_map. Used when removing a node from the list
        """
        deleted_node = self._index_map.pop(index, None)

        tail_index = self._list_length - 1
        if index != tail_index:  # if the index of the deleted node was not the tail index
            del self._index_map[tail_index]  # delete tail node from index_map as it would be stale after rebuild

        if deleted_node.next:  # if there are subsequent nodes, an update must be done to the self._index_map
            self._rebuild_index_map_partial(index, deleted_node.next)

    def _add_node_to_index_map(self, index, node):
        """
        Adds the index, Node pair to self._index_map. Used when adding a node to the list.
        """
        if not node:
            node = self._head

        self._index_map[index] = node

        if node.next:  # if there are subsequent nodes, an update must be done to the self._index_map
            self._rebuild_index_map_partial(index + 1, node.next)

    def _increment_list_length(self):
        self._list_length += 1

    def _decrement_list_length(self):
        self._list_length -= 1

    def _update_list_metadata_for_add_node(self, index_to_add_node: int = 0, added_node: Node = None):
        self._add_node_to_index_map(index_to_add_node, added_node)
        self._increment_list_length()

    def _update_list_metadata_for_remove_node(self, index_of_removed_node: int = 0):
        self._remove_node_from_index_map(index_of_removed_node)
        self._decrement_list_length()

    def prepend(self, value):
        """
        Adds a node to the front or the head of the linked list

        Args:
            value: The value to store in the node that will be prepended
        """
        new_node = Node(value)

        if self.is_empty():
            self._head = new_node
        else:
            new_node.next = self._head
            self._head = new_node

        self._update_list_metadata_for_add_node()

    def classic_pop(self):
        """
        Takes the node from the end of the list

        Return: the value of the removed node
        """
        if self.is_empty():
            return None

        if not self._head.next:
            tail_node = self._head
            self._head = None
            self._update_list_metadata_for_remove_node(index_of_removed_node=0)
            return tail_node.value

        index = 0
        current_node = self._head
        while current_node.next.next:  # stop at the penultimate node
            current_node = current_node.next
            index += 1

        tail_node = current_node.next
        current_node.next = None
        self._update_list_metadata_for_remove_node(index_of_removed_node=index + 1)
        return tail_node.value

    def pop(self):
        """
        Removes the tail node from the list

        Return: the value of the removed node
        """
        # If the list is empty, there's nothing to remove
        if self.is_empty():
            return None

        # Handle the case where there's only one node in the list
        if self._list_length == 1:
            tail_node = self._head
            self._head = None
            self._update_list_metadata_for_remove_node(index_of_removed_node=0)
            return tail_node.value

        # Get the index of the tail node
        tail_index = self._list_length - 1

        # Use the index map to retrieve the tail and the node just before it
        tail_node = self._index_map[tail_index]
        penultimate_node = self._index_map[tail_index - 1]

        # Remove the tail by setting the penultimate node's next to None
        penultimate_node.next = None  # cut the connection to the tail node

        self._update_list_metadata_for_remove_node(index_of_removed_node=tail_index)

        return tail_node.value

    def has_cycle(self):
        """
        Use Floyd's Tortoise-Hare algorithm to determine if a list has a cycle.
            A cycle means that a node points back to a previous node. If you traverse the list you end up traveling in
            circles.
            e.g. A -> B -> C -> D -> E -> F
                      ^-------------------|
            In this example the traversal would lead you A -> B -> C -> D -> E -> F -> B -> C -> D -> E and on and on

            The algorithm uses two pointers: a hare pointer that jumps two nodes at a time, and a tortoise pointer that
            travels one node at a time. If you think about a racetrack that is a loop with two racers traveling at
            different speeds, eventually, the faster one will catch up to the slower one. This meeting tells us that we
            are traversing a loop.

        Return: a boolean indicating whether a cycle exists in the list
        """
        # set both pointers equal to head to get both racers to the starting line
        hare_pointer = self._head
        tortoise_pointer = self._head

        while hare_pointer and hare_pointer.next:
            # if the hare pointer or next node is None then you have reached the end of the list and there's no cycle

            # advance the pointers
            tortoise_pointer = tortoise_pointer.next
            hare_pointer = hare_pointer.next.next

            # if the hare pointer and the tortoise pointer are the same, the hare has caught the tortoise and the
            # presence of a cycle is confirmed
            if hare_pointer is tortoise_pointer:
                return True

        return False

    def find_middle(self):
        """
        Uses Tortoise-Hare algorithm to find the middle node of the list. The hare pointer reaches the end of the list
        twice as fast as the tortoise pointer since it is traveling at twice the speed. Therefore, the tortoise pointer
        will be at the middle node of the list as the hare reaches the end.

        NOTE: If a list has an odd number of nodes (e.g. [0, 1, 2, 3, 4]) the middle is obvious (2), but for an even
        number of nodes (e.g. [0, 1, 2, 3]), what will be returned? This algorithm returns the 2nd of the 2 middles (2)

        Return: the value of the middle node
        """
        if self.is_empty():
            raise RuntimeError("Cannot find the middle of an empty list")
        if self.has_cycle():
            raise RuntimeError("Cannot find the middle of a cyclical linked list")

        hare_pointer = self._head
        tortoise_pointer = self._head

        while hare_pointer and hare_pointer.next:
            # if the hare pointer or next node is None then you have reached the end of the list

            # advance the pointers
            tortoise_pointer = tortoise_pointer.next
            hare_pointer = hare_pointer.next.next

        return tortoise_pointer.value

    def reverse(self):
        """
        Reverses the order of the nodes in place using 3 pointers

        Explanation: The first pointer is called current_node and points to self._head. The next pointer points to
        current_node.next and calls it next_node. The final pointer points to self._head after the pointer has been
        reversed and calls it previous.

        Now picture that you are physically traversing this list. You stand at head, and turn backwards. Head's
        pointer now points backwards between your legs to self.next. You flip that pointer around to point at nothing
        and then you hop back to the next node. You flip that nodes pointer around to point at head. You hop
        backwards again, and flip that nodes pointer to the one you were just at. So on and so on. This is
        essentially what is happening, and that is why we need the "next" point: to know where to jump after we have
        flipped the pointer of the node we are standing on. The first time I encountered this strategy, I was super
        confused. I wonder if this made it more or less complicated :)
        """
        if self.is_empty() or self._head.next is None:
            return  # Nothing to reverse
        if self.has_cycle():
            raise RuntimeError("Cannot reverse a cyclical linked list")

        previous_node = None
        current_node = self._head

        index = self._list_length - 1
        while current_node:
            next_node = current_node.next  # store the next node
            current_node.next = previous_node  # reverse the pointer
            previous_node = current_node  # move previous forward
            self._index_map[index] = current_node  # update the index map
            current_node = next_node  # move current forward
            index -= 1

        self._head = previous_node

    def __iter__(self):
        """
        Allow list to be iterated over

        Raises:
            Runtime Error when list has a cycle to prevent endless recursion upon iterating
        """
        # TODO: optimize this. we cannot be checking in a performance critical method whether or not the list has a cycle. Let a recursion error generate if the user decided to create a cycle in their list
        if self.has_cycle():
            raise RuntimeError("Cannot iterate over a cyclic linked list")
        current_node = self._head
        while current_node:
            yield current_node.value
            current_node = current_node.next

    def __repr__(self):
        """
        Allow list to be printed

        NOTE:
            If the list has a cycle, the representation only shows up to the first repeat
        """
        # TODO: should we limit how many nodes will be printed?
        if self.is_empty():
            return "Empty List"

        node_values = []
        current_node = self._head
        visited_nodes = set()

        while current_node:
            if id(current_node) in visited_nodes:
                node_values.append(f"{str(current_node.value)} ... (cycle detected)")
                break

            # add to node_values list and visited_nodes set and advance to the next node
            node_values.append(str(current_node.value))
            visited_nodes.add(id(current_node))
            current_node = current_node.next

        return "LinkedList([" + " -> ".join(node_values) + "])"

    def __len__(self):
        """
        The number of nodes in the linked list.

        Returns:
            int: The length of the list.
        """
        return self._list_length

    def __getitem__(self, index: int):
        """
        Allows bracket-style indexing into the linked list.
        Example: my_list[2]

        Args:
            index (int): The index of the node to retrieve.

        Returns:
            The value of the node at the given index.

        Raises:
            IndexError: If the index is out of bounds.
        """
        if not isinstance(index, int):
            raise TypeError("Index must be an integer.")

        if index < 0 or index >= self._list_length:
            raise IndexError("Index out of bounds.")

        return self._index_map[index].value

    def get_node(self, index: int):
        """
        Retrieves the node object at an index

        Args:
            index (int): The index of the node to retrieve.

        Returns:
            The node at the given index.

        Raises:
            IndexError: If the index is out of bounds.
        """
        if index < 0 or index >= self._list_length:
            raise IndexError("Index out of bounds.")

        return self._index_map[index]

    def __setitem__(self, index: int, value):
        """
        Sets the value of the node at the specified index.

        Args:
            index (int): The index of the node to update.
            value: The new value to assign to the node.

        Raises:
            IndexError: If the index is out of bounds.
        """
        if isinstance(index, int):
            raise TypeError
        if index not in self._index_map:
            raise IndexError("No node at this index.")

        self._index_map[index].value = value

    def insert(self, index: int, value):
        """
        Inserts a new node with the given value at the specified index.

        Args:
            index (int): The index at which to insert the node.
            value: The value to store in the new node.

        Raises:
            IndexError: If the index is out of bounds.
        """
        if index == 0:
            self.prepend(value)
            return
        elif index == self._list_length:
            self.append(value)
            return
        elif index < 0 or index > self._list_length:
            raise IndexError("Index out of bounds.")

        preceding_node = self._index_map[index - 1]
        node_to_insert = Node(value)
        subsequent_node = preceding_node.next

        preceding_node.next = node_to_insert
        node_to_insert.next = subsequent_node

        self._update_list_metadata_for_add_node(index_to_add_node=index, added_node=node_to_insert)

    def append(self, value):
        """
        Appends a new node with the given value to the end of the list.

        Args:
            value: The value to store in the new node.
        """
        if self.is_empty():
            self.prepend(value)
            return

        node_to_append = Node(value)
        tail_node = self._index_map[self._list_length - 1]

        tail_node.next = node_to_append

        self._update_list_metadata_for_add_node(index_to_add_node=self._list_length, added_node=node_to_append)

    def remove(self, index: int):
        """
        Removes the node at the specified index from the list.

        Args:
            index (int): The index of the node to remove.

        Raises:
            IndexError: If the index is out of bounds.
        """
        if self.is_empty():
            raise IndexError("Cannot remove from an empty list.")

        if index not in self._index_map:
            raise IndexError("No node at this index.")

        if index == 0:
            self._head = self._head.next
        else:
            node_to_remove = self._index_map[index]
            preceding_node = self._index_map[index - 1]
            subsequent_node = node_to_remove.next
            preceding_node.next = subsequent_node

        self._update_list_metadata_for_remove_node(index_of_removed_node=index)