k = int(input())
m = int(input())
r = [int(input()) for _ in range(m)]
a = [[i for i in range(1, k+1)]]
for i in range(m):
    a.append([])
    for j in range(1, len(a[i])+1):
        if j % r[i] != 0:
            a[i+1].append(a[i][j-1])
for j in a[-1]:
    print(j)