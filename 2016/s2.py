import sys
input = sys.stdin.readline

qtype = int(input())
n = int(input())
dmojistan = sorted(list(map(int, input().split())))
pegland = sorted(list(map(int, input().split())))
ans = 0

if qtype == 1:
    for i in range(n):
        ans += max(dmojistan[i], pegland[i])
    print(ans)
else:
    s = sorted(dmojistan + pegland, reverse=True)
    for i in range(n):
        ans += s[i]
    print(ans)