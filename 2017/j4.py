a = int(input())
b = 0
b1 = 12
c = []
for i in range(a + 1):
    if b == 60:
        b = 0
        if i <= 60:
            b1 = 0
        b1 += 1
    if len(str(b)) == 1:
        c.append((str(b1) + '0' + str(b)))
    else:
        c.append((str(b1) + str(b)))
    b += 1

f = 0
for j in range(a + 1):
    if len(str(c[j])) == 4:
        if int(c[j][3]) - int(c[j][2]) == int(c[j][2]) - int(c[j][1]) and int(c[j][2]) - int(c[j][1]) == int(c[j][1]) - int(c[j][0]):
            f += 1
    else:
        if int(c[j][2]) - int(c[j][1]) == int(c[j][1]) - int(c[j][0]):
            f += 1

print(f)