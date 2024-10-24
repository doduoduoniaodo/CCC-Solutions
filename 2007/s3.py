from collections import deque
import sys
input = sys.stdin.readline

def bfs(a, b):
    queue = deque([(a, 0)])
    visited = [False] * (10000)
    visited[a] = True
    
    while queue:
        node, distance = queue.popleft()
        if node == b:
            return distance-1
        for i in friends[node]:
            if not visited[i]:
                visited[i] = True
                queue.append((i, distance+1))
    
    return -1

n = int(input())
friends = {i:[] for i in range(1, 10000)}
for _ in range(n):
    a, b = map(int, input().split())
    friends[a].append(b)

while True:
    a, b = map(int, input().split())
    if (a, b) == (0, 0):
        break
    distance = bfs(a, b)
    if distance == -1:
        print('No')
    else:
        print('Yes', distance)