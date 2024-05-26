a = input()
b = [0, 0]
b[0], b[1] = a.count(':-)'), a.count(':-(')
if b[0] > b[1]:
    print('happy')
elif b[0] < b[1]:
    print('sad')
elif b[0] == b[1] and b[0] != 0:
    print('unsure')
else:
    print('none')