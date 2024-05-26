input()
a = input().split()
p = {}
b = input().split()
for i in range(len(a)):
    p[a[i]] = b[i]
ok = True
for i in range(len(a)):
    if a[i] == b[i] or p[b[i]] != a[i]:
        ok = False
        break
print('good' if ok else 'bad')