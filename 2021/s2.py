import sys
input = sys.stdin.readline

m, n, k = int(input()), int(input()), int(input())

row, col = [0]*(m+1), [0]*(n+1)
for i in range(k):
	op, id = input().strip().split()
	if op == 'R':
		row[int(id)] += 1
	else:
		col[int(id)] += 1
    
odd, even, ans = 0, 0, 0
for i in range(1, n+1):
	if col[i] % 2 != 0:
		odd += 1
	else:
		even += 1
for i in range(1, m+1):
	if row[i] % 2 != 0:
		ans += even
	else:
		ans += odd
    
print(ans)