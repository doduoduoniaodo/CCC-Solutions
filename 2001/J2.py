import sys
input = sys.stdin.readline

a, b = int(input()), int(input())
for i in range(1, 100):
    if (b * i + 1) % a == 0:
        print((b * i + 1) // a)
        sys.exit()
    i += 1
print('No such integer exists.')