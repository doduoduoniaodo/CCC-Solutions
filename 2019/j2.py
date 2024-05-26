a = int(input())
b = []
for _ in range(a):
    b.append(input().split(' '))
for i in range(a):
    print(int(b[i][0]) * b[i][1])