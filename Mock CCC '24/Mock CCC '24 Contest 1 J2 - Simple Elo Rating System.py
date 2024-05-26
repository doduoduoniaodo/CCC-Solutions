n, ra, rb, k = map(int, input().split(' '))
float(ra)
float(rb)
rs = 0.0
a = input()

for i in range(n):
    if a[i] == 'W':
        s = 1
        rs = k * (s - 1/(10**((rb-ra)/400)+1))
        ra += rs
        rb -= rs
    elif a[i] == 'L':
        s = 0
        rs = k * (s - 1/(10**((rb-ra)/400)+1))
        ra -= rs
        rb += rs
    else:
        s = 0.5
    print('%.1f' % (ra), '%.1f' % (rb))