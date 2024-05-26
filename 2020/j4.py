a = input()
b = input()
c = []
d = b
for i in range(len(b)):
    c.append(d)
    d = d[1:] + d[0]
for j in range(len(c)):
    if c[j] in a:
        print('yes')
        e = 'yes'
        break
    else:
        e = 'no'
if e == 'no':
    print('no')