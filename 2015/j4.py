a = int(input())
b = [tuple(input().split(' ')) for _ in range(a)]
name = []
for i in range(a):
    if b[i][0] != 'W':
        if b[i][1] not in name:
            name.append(b[i][1])
name.sort()
for i in range(len(name)):
    time = 0
    add = False
    sent = False
    n1 = False
    for j in range(a):
        if b[j][0] == 'R' and b[j][1] == name[i]:
            add = True
        if b[j][0] == 'S' and b[j][1] == name[i]:
            add = False
            sent = True
        if j != a-1:
            if b[j][0] != 'W' and b[j+1][0] != 'W' and add:
                time += 1
                sent = False
            elif b[j][0] == 'W' and add:
                time += int(b[j][1])
        else:
            if sent == False:
                print(name[i], -1)
                n1 = True
    if n1 == False:
        print(name[i], time)
        