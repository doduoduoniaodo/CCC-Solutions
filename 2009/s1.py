from sys import stdin
input = stdin.readline

a, b = int(input()), int(input())
count = 0
i = 1
while True:
    if a > i**6:
        i += 1
    elif i**6 <= b:
        count += 1
        i += 1
    else:
        break
print(count)