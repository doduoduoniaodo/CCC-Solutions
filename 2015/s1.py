import sys
input = sys.stdin.readline

a = int(input())
ans = []
for i in range(a):
    b = int(input())
    if b == 0 and len(ans) != 0:
        ans.pop(-1)
    else:
        ans.append(b)

print(sum(ans))