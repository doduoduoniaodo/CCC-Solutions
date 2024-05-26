import sys
input = sys.stdin.readline
w = int(input())
n = int(input())
a = [int(input()) for _ in range(n)]
weight = []
ans = 0
for i in range(n):
    if len(weight) == 4:
        weight.pop(0)
    weight.append(a[i])
    if sum(weight) <= w:
        ans += 1
    else:
        break
print(ans)