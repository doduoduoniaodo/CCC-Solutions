import sys
input = sys.stdin.readline

t, g = int(input()) - 1, int(input())
done = [[False] * 4 for _ in range(4)]
pts = [0] * 4
for i in range(g):
    a, b, sa, sb = map(int, input().split())
    done[a-1][b-1] = True
    if sa > sb:
        pts[a-1] += 3
    elif sa < sb:
        pts[b-1] += 3
    else:
        pts[a-1] += 1
        pts[b-1] += 1
remain = []
for a in range(4):
    for b in range(a+1, 4):
        if not done[a][b]:
            remain.append((a, b))
ways = 0

def fun(idx):
    global ways
    if idx == len(remain):
        if pts[t] == max(pts) and pts.count(pts[t]) == 1:
            ways += 1
        return
    a, b = remain[idx][0], remain[idx][1]
    pts[a] += 3; fun(idx+1); pts[a]-=3
    pts[b] += 3; fun(idx+1); pts[b]-=3
    pts[a] += 1; pts[b]+=1; fun(idx+1); pts[a]-=1; pts[b]-=1

fun(0)
print(ways)