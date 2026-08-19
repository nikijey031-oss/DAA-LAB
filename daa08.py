import heapq
from itertools import permutations

INF = float('inf')


def reduce_matrix(mat):
    """Reduce matrix and return reduction cost"""
    import copy

    m = [row[:] for row in mat]
    n = len(m)
    cost = 0

    # Row reduction
    for i in range(n):
        row_min = min(m[i])
        if row_min and row_min != INF:
            cost += row_min
            m[i] = [x - row_min if x != INF else INF for x in m[i]]

    # Column reduction
    for j in range(n):
        col_min = min(m[i][j] for i in range(n))
        if col_min and col_min != INF:
            cost += col_min
            for i in range(n):
                if m[i][j] != INF:
                    m[i][j] -= col_min

    return m, cost


def tsp_brute_force(cost, n):
    """Brute force for verification"""
    cities = list(range(1, n))
    best_cost = INF
    best_path = None

    for perm in permutations(cities):
        path = [0] + list(perm) + [0]
        c = sum(cost[path[i]][path[i + 1]] for i in range(n))

        if c < best_cost:
            best_cost = c
            best_path = path

    return best_path, best_cost


# --- 5-city cost matrix ---
cost = [
    [INF, 12, 7, 15, 9],
    [12, INF, 6, 10, 8],
    [7, 6, INF, 11, 13],
    [15, 10, 11, INF, 5],
    [9, 8, 13, 5, INF]
]

n = 5
cities = ['A', 'B', 'C', 'D', 'E']

best_path, best_cost = tsp_brute_force(cost, n)

print('5-City TSP - Cost Matrix:')
print(f'{"":>4}', ' '.join(f'{c:>5}' for c in cities))

for i, row in enumerate(cost):
    r = ['INF' if x == INF else str(x) for x in row]
    print(f'{cities[i]:>4}', ' '.join(f'{v:>5}' for v in r))

print(f'\nOptimal Tour: {" -> ".join(cities[i] for i in best_path)}')
print(f'Minimum Cost: {best_cost}')

print(f'\nPath verification:')
for i in range(n):
    u, v = best_path[i], best_path[i + 1]
    print(f' {cities[u]} -> {cities[v]}: cost = {cost[u][v]}')

OUTPUT:

5-City TSP - Cost Matrix:
         A     B     C     D     E
   A   INF    12     7    15     9
   B    12   INF     6    10     8
   C     7     6   INF    11    13
   D    15    10    11   INF     5
   E     9     8    13     5   INF

Optimal Tour: A -> C -> B -> D -> E -> A
Minimum Cost: 37

Path verification:
 A -> C: cost = 7
 C -> B: cost = 6
 B -> D: cost = 10
 D -> E: cost = 5
 E -> A: cost = 9
