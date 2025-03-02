from sys import stdin
input = stdin.readline

a, b, x, y = map(int, input().split())
print(2*(min((b+y+max(a, x), a+x+max(b, y)))))