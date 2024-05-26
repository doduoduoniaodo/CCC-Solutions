a = int(input())

b = 0

#1
if a % 4 == 0:
    b += 1

#2
if a% 5 == 0:
    b += 1

#3
c = a
while (c - 4) > 0:
    c -= 4
    if c % 5 == 0:
        b += 1


print(b)