a = [input() for _ in range(int(input()))]
for i in range(len(a)):
    a[i] += ' '
d = a[0][0]
ans = [[] for _ in range(len(a))]
e = 1
for i in range(len(a)):
    for j in range(len(a[i])-1):
        if a[i][j] == a[i][j+1]:
            e += 1
        else:
            ans[i].append(e)
            ans[i].append(a[i][j])
            e = 1
        d = a[i][j+1]

for i in range(len(ans)):
    for j in range(len(ans[i])):
        print(ans[i][j], end=' ')
        if j == len(ans[i])-1:
            print('\n')