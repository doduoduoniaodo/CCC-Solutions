b = ''
while True:
    a = input()
    if a == '99999':
        break
    if (int(a[0])+int(a[1])) % 2 == 0 and (int(a[0])+int(a[1])) != 0:
        print('right ' + a[2:])
        b = 'right'
    elif a[0] == '0' and a[1] == '0':
        print(b + ' ' + a[2:])
    else:
        print('left ' + a[2:])
        b = 'left'
