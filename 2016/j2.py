a = [input().split(' ') for _ in range(4)]
r = []
c = []
for i in range(4):
    b = 0
    for j in range(4):
        b += int(a[i][j])
    r.append(b)
for i in range(4):
    b = 0
    for j in range(4):
        b += int(a[j][i])
    c.append(b)
if r[0] == r[1] == r[2] == r[3] and c[0] == c[1] == c[2] == c[3]:
    print('magic')
else:
    print('not magic')