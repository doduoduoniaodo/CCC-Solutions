import sys
input = sys.stdin.readline
from collections import Counter

n, t = map(int, input().split())
for _ in range(n):
    a = list(input())
    c = Counter(a)
    heavy = c[a[0]]>1
    s = True
    for i in range(1, t):
        if heavy:
            if c[a[i]] > 1:
                print('F')
                s = False
                break
            else:
                heavy = False
        else:
            if c[a[i]] == 1:
                print('F')
                s = False
                break
            else:
                heavy = True
    if s:
        print('T')