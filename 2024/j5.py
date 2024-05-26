import sys
sys.setrecursionlimit(100000)
R, C = int(input()), int(input())
g = [list(input()) for i in range(R)]
r, c = int(input()), int(input())
ans = 0
d = {'S': 1, 'M': 5, 'L': 10}
def fun(r, c):
    global ans
    ans += d[g[r][c]]
    g[r][c] = '*'
    if r - 1 >= 0 and g[r - 1][c] != '*': fun(r - 1, c)
    if r + 1 < R and g[r + 1][c] != '*': fun(r + 1, c)
    if c - 1 >= 0 and g[r][c - 1] != '*': fun(r, c - 1)
    if c + 1 < C and g[r][c + 1] != '*': fun(r, c + 1)

fun(r, c)
print(ans)