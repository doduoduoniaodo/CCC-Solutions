q = int(input())
m = [int(input()), int(input()), int(input())]
p = [30, 60, 9]
t = [35, 100, 10]
cnt = 0

while q > 0:
    a = cnt % 3
    m[a] += 1
    if m[a] == t[a]:
        q += p[a]
        m[a] = 0
    q -= 1
    cnt += 1
print('Martha plays', cnt, 'times before going broke.')