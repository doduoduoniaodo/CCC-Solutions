from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
taller = {i:[] for i in range(n+1)}
for _ in range(m):
    x, y = map(int, input().split())
    taller[x].append(y)
p, q = map(int, input().split())

def bfs(start, end):
    visited = [False] * (n+1)
    visited[start] = True
    queue = deque([start])
    while queue:
        current = queue.popleft()
        if current == end:
            return True
        for i in taller[current]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
    return False

if bfs(p, q):
    print('yes')
elif bfs(q, p):
    print('no')
else:
    print('unknown')