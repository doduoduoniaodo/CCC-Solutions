import sys
input = sys.stdin.readline

n = int(input())
h = list(map(int, input().split()))

memo = [[0] * n for _ in range(n)]
ans = [float('inf')] * (n+1)
for length in range(1, n+1):
    for l in range(n-length+1):
        r = l + length - 1
        if l == r:
            memo[l][r] = 0
        else:
            memo[l][r] = abs(h[l] - h[r]) + memo[l+1][r-1]
        ans[length] = min(ans[length], memo[l][r])

print(*ans[1:])


'''
import sys
input = sys.stdin.readline
n = int(input())
a = list(map(int, input().split()))
ans = [float('inf')]*(n+1)
for i in range(n):
    val, l, r = 0, i, i
    while 0<=l and r < n:
        val += abs(a[l] - a[r])
        ans[r-l+1] = min(ans[r-l+1], val)
        l, r = l-1, r+1
    val, l, r = 0, i, i+1
    while 0<=l and r < n:
        val += abs(a[l] - a[r])
        ans[r-l+1] = min(ans[r-l+1], val)
        l, r = l-1, r+1
print(*ans[1:n+1])
'''