# 1
import sys
input = sys.stdin.readline

r, l = int(input()), int(input())
grid = [''.join((input().split())) for _ in range(r)]

rows = [int(r, 2) for r in grid]

dp = [set() for _ in range(r)]
dp[0].add(rows[0])

for i in range(1, r):
    for prev in dp[i-1]:
        dp[i].add(rows[i])          # not press the button
        dp[i].add(rows[i] ^ prev)   # press the button

print(len(dp[-1]))


# 2
import sys
input = sys.stdin.readline

r, l = int(input()), int(input())
grid = [tuple(map(int, input().split())) for _ in range(r)]

cur = {grid[0]}

def xor(a, b):
    return tuple([a[i] ^ b[i] for i in range(l)])

for i in range(1, r):
    new = {grid[i]}
    for j in cur:
        new.add(xor(grid[i], j))
    cur = new

print(len(cur))
