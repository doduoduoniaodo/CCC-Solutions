a = list(map(int, input().split()))
ans = [0, 0, 0, 0, 0]
for i in range(5):
    for j in range(5):
        ans[j] = 0
        if j < i:
            for k1 in range(j, i):
                ans[j] += a[k1]
        if j > i:
            for k2 in range(i, j):
                ans[j] += a[k2]
    for z in range(5):
        if z != 4:
            print(ans[z], end=' ')
        else:
            print(ans[z], end='\n')