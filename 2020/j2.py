a = int(input())
b = int(input())
c = int(input())
d = b
e = 0
f = b
while d <= a:
    d += f * c
    f = f * c
    e += 1
print(e)