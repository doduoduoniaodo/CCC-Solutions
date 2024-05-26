a = int(input())
b = []
for i in range(a):
    c = input().split(',')
    for i1 in range(2):
        c[i1] = int(c[i1])
    b.append(c)

blx = 100
bly = 100
trx = 0
tr_y = 0
for i in range(a):
    if b[i][0] <= blx:
        blx = b[i][0]
    if b[i][1] <= bly:
        bly = b[i][1]
    if b[i][0] >= trx:
        trx = b[i][0]
    if b[i][1] >= tr_y:
        tr_y = b[i][1]

ans_bottom_left = str(blx-1) + ',' + str(bly-1)
ans_top_right = str(trx+1) + ',' + str(tr_y+1)
print(ans_bottom_left)
print(ans_top_right)