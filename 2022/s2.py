must, mustnot = {}, {}
for i in (must, mustnot):
    for j in range(int(input())):
        a, b = input().split()
        if a not in i:
            i[a] = [b]
        else:
            i[a].append(b)
ans = 0
for _ in range(int(input())):
    group = set(input().split())
    for i in group:
        for m in must.get(i, []):
            if m not in group:
                ans += 1
        for n in mustnot.get(i, []):
            if n in group:
                ans += 1
'''
for _ in range(int(input())):
    group = set(input().split())
    for i in group:
        ans += sum(1 for mi in must.get(i, []) if mi not in group) + \
            sum(1 for mni in mustnot.get(i, []) if mni in group)
'''
print(ans)