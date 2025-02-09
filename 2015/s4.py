import heapq
import sys
input = sys.stdin.readline

k, n, m = map(int, input().split())
adj = {i:[] for i in range(1, n+1)}
for _ in range(m):
    a, b, t, h = map(int, input().split())
    adj[a].append((b, t, h))
    adj[b].append((a, t, h))
a, b = map(int, input().split())

queue = []
heapq.heappush(queue, (0, a, 0))
distance = [[float('inf')]*k for _ in range(n+1)]
distance[a][0] = 0
while queue:
    d, u, h = heapq.heappop(queue)
    if u == b:
        print(d)
        sys.exit()
    for v, w, hull in adj[u]:
        state = h + hull
        if state < k and distance[v][state] > distance[u][h] + w:
            distance[v][state] = distance[u][h] + w
            heapq.heappush(queue, (distance[v][state], v, state))

print(-1)