h, m = map(int, input().split(':'))
t = h * 60 + m
for _ in range(120):
    if 7*60 <= t < 10*60 or 15*60 <= t < 19*60:
        t += 2
    else:
        t += 1
print('%02d:%02d' % (t / 60 % 24, t % 60))