a = [(0, -1), (0, -2), (0, -3), (1, -3), (2, -3), (3, -3), (3, -4), (3, -5), (4, -5), (5, -5), (5, -4), (5, -3), (6, -3), (7, -3), (7, -4), (7, -5), (7, -6), (7, -7), (6, -7), (5, -7), (4, -7), (3, -7), (2, -7), (1, -7), (0, -7), (-1, -7), (-1, -6), (-1, -5)]
c = [-1, -5]
safe = 'safe'
while True:
    b1, b2 = input().split()
    b2 = int(b2)
    if b1 == 'q':
        break
    elif b1 == 'd':
        for i in range(b2):
            c[1] -= 1
            if tuple(c) in a:
                safe = 'DANGER'
            a.append(tuple(c))
    elif b1 == 'u':
        for i in range(b2):
            c[1] += 1
            if tuple(c) in a:
                safe = 'DANGER'
            a.append(tuple(c))
    elif b1 == 'r':
        for i in range(b2):
            c[0] += 1
            if tuple(c) in a:
                safe = 'DANGER'
            a.append(tuple(c))
    elif b1 == 'l':
        for i in range(b2):
            c[0] -= 1
            if tuple(c) in a:
                safe = 'DANGER'
            a.append(tuple(c))
    print(*c, safe)
    if safe == 'DANGER':
        break