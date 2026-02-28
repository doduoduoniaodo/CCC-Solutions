import sys
input = sys.stdin.readline

b, t, p = int(input()), int(input()), int(input())

if (p+b) > t:
    print('N')
else:
    print('Y', t-p-b)

