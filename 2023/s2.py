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