d = int(input())
for _ in range(int(input())):
	op = input()
	q = int(input())
	if op == '+':
		d += q
	else:
		d -= q
print(d)
