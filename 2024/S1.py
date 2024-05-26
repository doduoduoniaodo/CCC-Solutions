import sys
input = sys.stdin.readline

n = int(input())
h = [int(input()) for _ in range(n)]
ans = 0
d = n // 2
for i in range(n - d):
    if h[i] == h[i+d]:
        ans += 2
print(ans)