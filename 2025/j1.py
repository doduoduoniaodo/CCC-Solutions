from sys import stdin
input = stdin.readline

n, c, p = int(input()), int(input()), int(input())
if n <= c*p:
    print('yes')
else:
    print('no')