import sys
input = sys.stdin.readline

n = int(input())
a = [100, 500, 1000, 5000, 10000, 25000, 50000, 100000, 500000, 1000000]
for _ in range(n):
    a[int(input())-1] = 0
if int(input()) > sum(a)/(10-n):
    print('deal')
else:
    print('no deal')