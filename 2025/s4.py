# way 1: treat edges as nodes
import sys, heapq
inpput = sys.stdin.readline

n, m = map(int, input().split())
adj = [[] for _ in range(n+1)]
edges = [0]
for i in range(1, m+1):
    a, b, c = map(int, input().split())
    adj[a].append((b, c, i))
    adj[b].append((a, c, i))
    edges.append(c)

adj[1].append((0, 0, 0))

distance = [float('inf')] * (m+1)
distance[0] = 0

queue = []
heapq.heappush(queue, (0, 1, 0))

while queue:
    c, u, prev = heapq.heappop(queue)
    
    if u == n:
        print(c)
        sys.exit()
    if c > distance[prev]:
        continue
    
    for v, w, i in adj[u]:
        c2 = c + abs(edges[prev] - w)
        if c2 < distance[i]:
            distance[i] = c2
            heapq.heappush(queue, (c2, v, i))


# way 2: binary search
import sys, heapq
from bisect import bisect_left
inpput = sys.stdin.readline

n, m = map(int, input().split())
adj = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    adj[a].append((c, b))
    adj[b].append((c, a))

adj[1].append((0, 0))

for i in range(1, n+1):
    adj[i].sort()

distance = [{} for _ in range(n+1)]
for i in range(1, n+1):
    for j, (c, v) in enumerate(adj[i]):
        distance[i][j] = float('inf')

queue = []
distance[1][0] = 0
heapq.heappush(queue, (0, 1, 0))

while queue:
    c, u, cl = heapq.heappop(queue)
    
    if u == n:
        print(c)
        sys.exit()
    if c > distance[u][cl]:
        continue
    
    w, v = adj[u][cl]
    
    if v != 0:
        cl2 = bisect_left(adj[v], (w, u))
        if cl2 < len(adj[v]) and adj[v][cl2] == (w, u):
            if distance[v][cl2] > c:
                distance[v][cl2] = c
                heapq.heappush(queue, (c, v, cl2))
    
    if cl > 0:
        w2, _ = adj[u][cl-1]
        c2 = c + abs(w - w2)
        if distance[u][cl-1] > c2:
            distance[u][cl-1] = c2
            heapq.heappush(queue, (c2, u, cl-1))
    
    if cl+1 < len(adj[u]):
        w2, _ = adj[u][cl+1]
        c2 = c + abs(w - w2)
        if distance[u][cl+1] > c2:
            distance[u][cl+1] = c2
            heapq.heappush(queue, (c2, u, cl+1))

