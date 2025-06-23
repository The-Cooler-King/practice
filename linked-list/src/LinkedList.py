from Node import Node


class LinkedList:
    def __init__(self):
        """
        Initializes an empty singly linked list
        Sets the head to None
        """
        self._head = None
        self._index_map = {}

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

    def rebuild_index_map(self, start_index: int = 0, start_node: Node = self._head):
        """
        Traverses the list and (re)assigns a sequential index to each node from the given starting point.

        Args:
            start_index (int): Index to begin mapping from. Defaults to 0.
            start_node (Node): Node to begin mapping from. Defaults to the head of the list.

        Notes:
            If called with default arguments, this clears and fully rebuilds the index map.
            If called with a custom start_index and start_node, it updates the map from that point forward.
            In that case, earlier indices may remain stale, so ensure they were already accurate or explicitly updated.
        """

        # if rebuilding from scratch, clear self._index_map
        if start_node == self._head or start_index == 0:
            self._index_map = {}

        current_node = start_node
        index = start_index

        # traverse the list and assign a sequential integer index to each node
        while current_node:
            self._index_map[index] = current_node
            index += 1
            current_node = current_node.next

    def _remove_node_from_index_map(self, index):
        """
        Deletes the index, Node pair from self._index_map. Used when removing a node from the list
        """

        deleted_node = self._index_map.pop(index, None)

        if deleted_node.next: # if there are subsequent nodes, an update must be done to the self._index_map
            self.rebuild_index_map(index, deleted_node.next)

    def _add_node_to_index_map(self, index, node):
        """
        Adds the index, Node pair to self._index_map. Used when adding a node to the list.
        """
        self._index_map[index] = node

        if node.next: # if there are subsequent nodes, an update must be done to the self._index_map
            self.rebuild_index_map(index + 1, node.next)

    def validate_index_map(self):
        """
        Validates the integrity of the index map by ensuring each indexed node in the map corresponds exactly
        to the node at that position in the linked list.

        Returns:
            bool: True if the index map is accurate and consistent with the current list structure;
                  False if there are missing entries or incorrect mappings.

        Use Cases:
            - Debugging: Helps detect stale or corrupted index map entries.
            - Testing: Can be used in unit tests to assert internal consistency after list operations.
        """
        current_node = self._head
        index = 0

        while current_node:
            if index not in self._index_map or self._index_map[index] != current_node:
                return False
            index += 1
            current_node = current_node.next

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

    def pop(self):
        """
        Takes the node from the end of the list

        Return: the value of the removed node
        """
        if self.is_empty():
            return None

        if not self._head.next:
            tail_value = self._head.value
            self._head = None

            return tail_value

        current_node = self._head
        while current_node.next.next:  # stop at the penultimate node
            current_node = current_node.next

        tail_value = current_node.next.value
        current_node.next = None
        return tail_value

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
        # if self.is_empty():  # if there are no nodes
        #     return False

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

        Explanation:
            The first pointer is called next_node and points to self._head. The next pointer points to self._head.next
            and calls it current_node. The final pointer points to self._head.next.next and calls it previous. Now
            picture that you are physically traversing this list. You stand at head, and turn backwards. Head's pointer
            now points backwards between your legs to self.next. You flip that pointer around to point at nothing and
            then you hop back to the next node. You flip that nodes pointer around to point at head. You hop backwards
            again, and flip that nodes pointer to the one you were just at. So on and so on. This is essentially what is
            happening, and that is why we need the "next" point: to know where to jump after we have flipped the
            pointer of the node we are standing on. The first time I encountered this strategy, I was super confused.
            I wonder if this made it more or less complicated :)
        """
        if self.is_empty() or self._head.next is None:
            return  # Nothing to reverse
        if self.has_cycle():
            raise RuntimeError("Cannot reverse a cyclical linked list")

        previous_node = None
        current_node = self._head

        while current_node:
            next_node = current_node.next  # store the next node
            current_node.next = previous_node  # reverse the pointer
            previous_node = current_node  # move previous forward
            current_node = next_node  # move current forward

        self._head = previous_node

    def __iter__(self):
        """
        Allow list to be iterated over

        Raises:
            Runtime Error when list has a cycle to prevent endless recursion upon iterating
        """
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
        if self.is_empty():
            return "Empty List"

        node_values = []
        current_node = self._head
        visited_nodes = set()

        while current_node:
            if id(current_node) in visited_nodes:
                node_values.append(f"{str(current_node.value)} ... (cycle detected)")
                break

            # add to node_values list and visted_nodes set and advance to the next node
            node_values.append(str(current_node.value))
            visited_nodes.add(id(current_node))
            current_node = current_node.next

        return "LinkedList([" + " -> ".join(node_values) + "])"
