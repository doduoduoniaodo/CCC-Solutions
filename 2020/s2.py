import sys
from collections import deque
input = sys.stdin.readline

m, n = int(input()), int(input())
grid = [list(map(int, input().split())) for _ in range(m)]
graph = [[] for _ in range(1000001)]
for i in range(m):
    for j in range(n):
        graph[(i+1)*(j+1)].append(grid[i][j])

visited = [False] * 1000001
visited[1] = True
queue = deque([1])
while queue:
    u = queue.popleft()
    for i in graph[u]:
        if not visited[i]:
            visited[i] = True
            queue.append(i)

print("yes" if visited[m*n] else "no")