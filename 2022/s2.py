must, mustnot = {}, {}
for i in (must, mustnot):
    for j in range(int(input())):
        a, b = input().split()
        if a not in i:
            i[a] = [b]
        else:
            i[a].append(b)
ans = 0
for _ in range(int(input())):
    group = input().split()
    for i in group:
        for m in must.get(i, []):
            if m not in group:
                ans += 1
        for n in mustnot.get(i, []):
            if n in group:
                ans += 1

print(ans)


'''
import sys
input = sys.stdin.readline

x = [(input().strip().split()) for _ in range(int(input()))]
y = [(input().strip().split()) for _ in range(int(input()))]
d = {}

for i in range(int(input())):
    a, b, c = input().strip().split()
    d[a] = d[b] = d[c] = i

ans = 0
for a, b in x:
    ans += d[a] != d[b]
for a, b in y:
    ans += d[a] == d[b]
#True --> 1
#False --> 0

print(ans)
'''