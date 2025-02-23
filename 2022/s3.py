from collections import deque
import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
if k < n:
    print(-1)
    sys.exit()

k -= n
a = [0]*(n+1)
a[1] = 1
queue = deque([1])
last = 1
for i in range(2, n+1):
    if k >= len(queue):
        last += 1
        if last <= m:
            k -= last-1
            a[i] = last
            queue.append(last)
        else:
            a[i] = queue[0]
            queue.popleft()
            k -= m-1
            queue.append(a[i])
    else:
        a[i] = queue[len(queue) - 1 - k]
        k = 0
        queue.append(a[i])

if k:
    print(-1)
else:
    print(*a[1:])