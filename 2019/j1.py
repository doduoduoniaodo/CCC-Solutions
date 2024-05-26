a = []
for _ in range(6):
    a.append(int(input()))
A = 3*a[0] + 2*a[1] + a[2]
B = 3*a[3] + 2*a[4] + a[5]
if A > B:
    print('A')
elif A < B:
    print('B')
else:
    print('T')