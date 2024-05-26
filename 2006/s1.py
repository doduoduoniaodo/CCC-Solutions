mother = input()
father = input()
abcde = ''

for _ in range(int(input())):
    baby = input()
    good = True
    for i in range(5):
        if baby[i].isupper():
            if father[i*2] != baby[i] and mother[i*2] != baby[i]:
                good = False
                break
        else:
            if father[i*2+1] != baby[i] or mother[i*2+1] != baby[i]:
                good = False
                break
    if good:
        print('Possible baby.')
    else:
        print('Not their baby!')
