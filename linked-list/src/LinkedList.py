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

        if self.is_empty():
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def pop(self):
        """
        Takes the node from the end of the list

        Return: the value of the removed node
        """
        if self.is_empty():
            return None

        if not self.head.next:
            tail_value = self.head.value
            self.head = None
            return tail_value

        current_node = self.head
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
        hare_pointer = self.head
        tortoise_pointer = self.head

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

        hare_pointer = self.head
        tortoise_pointer = self.head

        while hare_pointer and hare_pointer.next:
            # if the hare pointer or next node is None then you have reached the end of the list

            # advance the pointers
            tortoise_pointer = tortoise_pointer.next
            hare_pointer = hare_pointer.next.next

        return tortoise_pointer.value

    def __iter__(self):
        """
        Allow list to be iterated over

        Raises:
            Runtime Error when list has a cycle to prevent endless recursion upon iterating
        """
        if self.has_cycle():
            raise RuntimeError("Cannot iterate over a cyclic linked list")
        current_node = self.head
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
        current_node = self.head
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
