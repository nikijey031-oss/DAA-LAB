import heapq

# ---------- Union-Find for Kruskal ----------
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path Compression
        return self.parent[x]

    def union(self, x, y):
        rx, ry = self.find(x), self.find(y)

        if rx == ry:
            return False

        if self.rank[rx] < self.rank[ry]:
            rx, ry = ry, rx

        self.parent[ry] = rx

        if self.rank[rx] == self.rank[ry]:
            self.rank[rx] += 1

        return True


# ---------- Kruskal's Algorithm ----------
def kruskal(n, edges):
    edges.sort()  # Sort edges by weight

    uf = UnionFind(n)
    mst = []
    cost = 0

    for w, u, v in edges:
        if uf.union(u, v):
            mst.append((u, v, w))
            cost += w

            if len(mst) == n - 1:
                break

    return mst, cost


# ---------- Prim's Algorithm ----------
def prim(n, adj, start=0):
    INF = float('inf')

    key = [INF] * n
    parent = [-1] * n
    inMST = [False] * n

    key[start] = 0

    pq = [(0, start)]
    mst = []
    cost = 0

    while pq:
        w, u = heapq.heappop(pq)

        if inMST[u]:
            continue

        inMST[u] = True

        if parent[u] != -1:
            mst.append((parent[u], u, w))
            cost += w

        for v, wt in adj.get(u, []):
            if not inMST[v] and wt < key[v]:
                key[v] = wt
                parent[v] = u
                heapq.heappush(pq, (wt, v))

    return mst, cost


# ---------- Graph Definition ----------
n = 7

edges = [
    (6, 0, 1),
    (4, 0, 2),
    (10, 1, 2),
    (7, 1, 3),
    (5, 1, 4),
    (9, 2, 4),
    (8, 2, 5),
    (11, 3, 4),
    (3, 3, 5),
    (12, 4, 6),
    (7, 5, 6)
]

adj = {}

for w, u, v in edges:
    adj.setdefault(u, []).append((v, w))
    adj.setdefault(v, []).append((u, w))


# ---------- Run Algorithms ----------
k_mst, k_cost = kruskal(n, edges[:])
p_mst, p_cost = prim(n, adj)


# ---------- Output ----------
print("=== Kruskal's MST ===")

for u, v, w in k_mst:
    print(f"Edge ({u} - {v})  Weight: {w}")

print(f"Total MST Cost: {k_cost}")


print("\n=== Prim's MST ===")

for u, v, w in p_mst:
    print(f"Edge ({u} - {v})  Weight: {w}")

print(f"Total MST Cost: {p_cost}")

OUTPUT:

=== Kruskal's MST ===
Edge (3 - 5)  Weight: 3
Edge (0 - 2)  Weight: 4
Edge (1 - 4)  Weight: 5
Edge (0 - 1)  Weight: 6
Edge (1 - 3)  Weight: 7
Edge (5 - 6)  Weight: 7
Total MST Cost: 32

=== Prim's MST ===
Edge (0 - 2)  Weight: 4
Edge (0 - 1)  Weight: 6
Edge (1 - 4)  Weight: 5
Edge (1 - 3)  Weight: 7
Edge (3 - 5)  Weight: 3
Edge (5 - 6)  Weight: 7
Total MST Cost: 32
