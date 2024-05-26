c = int(input())
r1 = list(map(int, input().split(' ')))
r2 = list(map(int, input().split(' ')))

count = r1.count(1) * 3
count += r2.count(1) * 3

for i in range(c):
    if i != c-1:
        if r1[i] == 1 and r1[i+1] == 1:
            count -= 2
        if r2[i] == 1 and r2[i+1] == 1:
            count -= 2
    if i % 2 == 0 and r1[i] == 1 and r2[i] == 1:
        count -= 2

print(count)