class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None
        # this approach uses a double linked list, so each node must know its neighbor to the left and the right


class LeastRecentlyUsedCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # used to map keys to nodes
        self.left = Node(0, 0)  # LRU dummy
        self.right = Node(0, 0)  # MRU dummy
        # left and right attributes are the bookends of the linked list. when insert a book (a node), you put it in
        # between the rightmost book (self.right.prev) and the right bookend (self.right).
        self.left.next = self.right
        self.right.prev = self.left
        # at initialization there are only the left and right bookends and so they are
        # linked to each other

    def _remove(self, node: Node):
        # Remove node from list by taking its two neighbors and linking them together
        previous_node, next_node = node.prev, node.next
        previous_node.next = next_node
        next_node.prev = previous_node

    def _insert(self, node: Node):
        # Insert a node by placing it in between the rightmost node and the right bookend node
        # This spot is considered Most Recently Used
        rightmost_node, right_bookend_node = self.right.prev, self.right
        # establish connection between the previously rightmost node and the inserted node
        rightmost_node.next = node
        node.prev = rightmost_node
        # establish the connection between the right bookend node and the inserted node
        right_bookend_node.prev = node
        node.next = right_bookend_node

    def get(self, key: int) -> int:
        if key in self.cache:
            self._remove(self.cache[key])  # use the cache hash map to get the node
            # remove the node from the linked list and then insert it back on the right as the most recently used node
            self._insert(self.cache[key])

            return self.cache[key].value

        return -1  # return -1 if key not in cache

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self._remove(self.cache[key])

        self.cache[key] = Node(key, value)
        self._insert(self.cache[key])

        if len(self.cache) > self.capacity:
            # remove least recently used from linked list and delete it from hash map to remove from cache
            least_recently_used_node = self.left.next
            self._remove(least_recently_used_node)
            del self.cache[least_recently_used_node.key]


def test_lru_cache():
    print("Creating LRU cache with capacity 2")
    lru = LeastRecentlyUsedCache(2)

    print("\nPut (1, 1)")
    lru.put(1, 1)

    print("Put (2, 2)")
    lru.put(2, 2)

    print("Get 1 (expected 1):", lru.get(1))  # returns 1, makes key 1 most recently used

    print("Put (3, 3) - should evict key 2")
    lru.put(3, 3)

    print("Get 2 (expected -1, was evicted):", lru.get(2))  # returns -1 (not found)

    print("Put (4, 4) - should evict key 1")
    lru.put(4, 4)

    print("Get 1 (expected -1, was evicted):", lru.get(1))  # returns -1
    print("Get 3 (expected 3):", lru.get(3))  # returns 3
    print("Get 4 (expected 4):", lru.get(4))  # returns 4


test_lru_cache()
