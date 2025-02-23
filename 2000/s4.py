from sys import stdin
input = stdin.readline

d, c = int(input()), int(input())
clubs = [int(input()) for _ in range(c)]

dp = [float('inf')]*(d+1)
dp[0] = 0
for i in range(1, d+1):
    for c in clubs:
        if d >= c:
            dp[i] = min(dp[i], dp[i-c]+1)

if dp[d] == float('inf'):
    print('Roberta acknowledges defeat.')
else:
    print('Roberta wins in', dp[d], 'strokes.')