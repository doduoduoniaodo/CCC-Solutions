a = int(input())
o = [0]
for i in range(a):
    o.append(int(input()))

while True:
    a = int(input())
    if a == 77:
        break
    elif a == 99:
        b = int(input())
        c = int(input())
        o.insert(b, (o[b]*(c/100)))
        o[b+1] -= o[b]
    elif a == 88:
        b = int(input())
        c = o[b] + o[b+1]
        o[b] = c
        o.pop(b+1)

for j in range(1, len(o)):
    print(round(o[j]), end=' ')

