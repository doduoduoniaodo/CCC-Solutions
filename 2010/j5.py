from collections import deque
import sys
input = sys.stdin.readline

start = tuple(map(int, input().split()))
final = tuple(map(int, input().split()))

if start == final:
    print(0)
    sys.exit()

moves = [(-2, 1), (-1, 2), (1, 2), (2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]

queue = deque([(start[0], start[1], 0)])
visited = set([(start[0], start[1])])

while queue:
    x, y, move = queue.popleft()
    
    for i, j in moves:
        ix, jy = x+i, y+j
        if 1 <= ix <= 8 and 1 <= jy <= 8 and (ix, jy) not in visited:
            if (ix, jy) == final:
                print(move + 1)
                sys.exit()
            else:
                visited.add((ix, jy))
                queue.append((ix, jy, move+1))
