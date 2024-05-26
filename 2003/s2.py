vowel = 'aeiou'
for _ in range(int(input())):
    cnt = 0
    r = []
    for i in range(4):
        a = input().lower().split()
        good = False
        for j in range(len(a[-1])-1, 0, -1):
            if a[-1][j] in vowel:
                r.append(a[-1][j:])
                good = True
                break
        if not good:
            r.append(a[-1])
    if r[0] == r[1] == r[2] == r[3]:
        print('perfect')
    elif r[0] == r[1] and r[2] == r[3]:
        print('even')
    elif r[0] == r[2] and r[1] == r[3]:
        print('cross')
    elif r[0] == r[3] and r[1] == r[2]:
        print('shell')
    else:
        print('free')
    