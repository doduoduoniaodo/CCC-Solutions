from sys import stdin
input = stdin.readline

a, b, n = int(input()), int(input()), int(input())
motels = [0, 990, 1010, 1970, 2030, 2940, 3060, 3930, 4060, 4970, 5030, 5990, 6010, 7000]
for _ in range(n):
    motels.append(int(input()))
motels.sort()

dp = [0]*7001
dp[0] = 1
for i in motels:
    if i == 0:
        continue
    for j in motels:
        if j < i and a <= i - j <= b:
            dp[i] += dp[j]
            
print(dp[7000])