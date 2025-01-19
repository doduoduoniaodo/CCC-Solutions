# Dijkstra’s Algorithm

import heapq
from sys import stdin
input = stdin.readline

n = int(input())
t = int(input())
# use adjacency matrix
adj = [[float('inf')]*(n+1) for _ in range(n+1)]
for _ in range(t):
    x, y, c = map(int, input().split())
    adj[x][y] = c
    adj[y][x] = c
k = int(input())
queue = []
cost = [float('inf')] * (n+1)
for _ in range(k):
    z, p = tuple(map(int, input().split()))
    heapq.heappush(queue, (p, z))
    cost[z] = p
destination = int(input())

while queue:
    c, u = heapq.heappop(queue)
    if cost[u] < c:
        continue
    for v, w in enumerate(adj[u]):
        if cost[u]+w < cost[v]:
            cost[v] = cost[u]+w
            heapq.heappush(queue, (cost[u]+w, v))

print(cost[destination])
