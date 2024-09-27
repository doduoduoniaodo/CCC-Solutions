from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
m = [list(map(int, input().split())) for _ in range(n)]

adjacent_list = {i: [] for i in range(0, n+1)}

for i in range(n):
    for j in range(1, m[i][0]+1):
        adjacent_list[i+1].append(m[i][j])

queue = deque([1])
visited = [False] * (n+1)
visited[1] = True
while queue:
    current = queue.popleft()
    
    for i in adjacent_list[current]:
        if not visited[i]:
            visited[i] = True
            queue.append(i)

if all(visited[1:]):
    reachable = True
else:
    reachable = False
    
queue = deque([(1, 1)])
visited = [False] * (n+1)
visited[1] = True
while queue:
    current, distance = queue.popleft()
    
    if len(adjacent_list[current]) == 0:
        print('Y' if reachable else 'N')
        print(distance)
        sys.exit()
    
    for i in adjacent_list[current]:
        if not visited[i]:
            visited[i] = True
            queue.append((i, distance+1))