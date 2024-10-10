from collections import deque
import sys
input = sys.stdin.readline

def bfs(r, c, grid):
    queue = deque([(0, 0, 1)])
    visited = [[False]*c for _ in range(r)]
    visited[0][0] = True
    while queue:
        x, y, distance = queue.popleft()
        
        if (x, y) == (r-1, c-1):
            return distance
        
        if grid[x][y] == '-':
            d = [(0, -1), (0, 1)]
        elif grid[x][y] == '|':
            d = [(-1, 0), (1, 0)]
        else:
            d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        for dx, dy in d:
            nx, ny = x+dx, y+dy
            if 0 <= nx < r and 0 <= ny < c and not visited[nx][ny] and grid[nx][ny] != '*':
                queue.append((nx, ny, distance+1))
                visited[nx][ny] = True

    return -1

for _ in range(int(input())):
    r, c = int(input()), int(input())
    grid = [list(input().strip()) for _ in range(r)]
    print(bfs(r, c, grid))