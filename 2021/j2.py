n = int(input())
d = {}
for i in range(n):
    a, b = input(), int(input())
    if b in d.keys():
        continue
    d[b] = a
print(d[max(d.keys())])