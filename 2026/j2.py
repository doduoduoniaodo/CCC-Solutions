import sys
input = sys.stdin.readline

s = [int(input()) for _ in range(5)]
d = int(input())

s.sort()
print((s[1] + s[2] + s[3]) * d)

