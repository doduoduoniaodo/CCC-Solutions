a = 0
for _ in range(6):
    if input() == 'W':
        a += 1
if a == 5 or a == 6:
    print(1)
elif a == 3 or a == 4:
    print(2)
elif a == 1 or a == 2:
    print(3)
else:
    print(-1)