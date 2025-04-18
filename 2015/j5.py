import sys
input = sys.stdin.readline

n = int(input())
k = int(input())

# dp[i][j]: number of ways to write i as sum of j non-decreasing positive integers
dp = [[0] * (k + 1) for _ in range(n + 1)]
dp[0][0] = 1

for i in range(1, n + 1):           # min value of each part
    for j in range(i, n + 1):       # total pies
        for k in range(1, k + 1):   # number of parts
            dp[j][k] += dp[j - i][k - 1]

print(dp[-1][-1])

