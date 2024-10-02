from collections import deque

flooring = int(input())
R = int(input())
C = int(input())
grid = [list(input()) for _ in range(R)]
visited = [[False] * C for _ in range(R)]
room = []

def bfs(r, c):
    queue = deque()
    area = 0
    queue.append((r, c))
    visited[r][c] = True
    d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    while queue:
        r, c = queue.popleft()
        area += 1
        for dr, dc in d:
            nr, nc = r + dr, c + dc
            if 0 <= nr < R and 0 <= nc < C and not visited[nr][nc] and grid[nr][nc] != 'I':
                queue.append((nr, nc))
                visited[nr][nc] = True
    
    return area

for i in range(R):
    for j in range(C):
        if grid[i][j] == '.' and not visited[i][j]:
            room.append(bfs(i, j))

room.sort(reverse=True)
cnt = 0
for area in room:
    if flooring >= area:
        flooring, cnt = flooring-area, cnt+1
    else:
        break
if cnt == 1:
    print(cnt, 'room,', flooring, 'square metre(s) left over')
else:
    print(cnt, 'rooms,', flooring, 'square metre(s) left over')