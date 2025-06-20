class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))  # Initially, each node is its own parent
        self.size = [1] * n           # Size of each community

    def find(self, x):
        # Path compression
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        # Find leaders of each community
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return

        # Union by size
        if self.size[root_x] < self.size[root_y]:
            root_x, root_y = root_y, root_x

        self.parent[root_y] = root_x
        self.size[root_x] += self.size[root_y]

    def get_size(self, x):
        return self.size[self.find(x)]


n = 3
queries = ["Q 1", "M 1 2", "Q 2", "M 2 3", "Q 3", "Q 2"]
uf = UnionFind(n)

for query in queries:
    action = query[0]
    target = query[2:]

    if action == "Q":
        print(f"Community size [{int(target) - 1}]: {uf.get_size(int(target) - 1)}")
    else:
        person_i = int(target.split(" ")[0]) - 1
        person_j = int(target.split(" ")[1]) - 1
        uf.union(person_i, person_j)