for _ in range(int(input())):
	a = input()
	s = 0
	n = ''
	isN = False
	new = ''
	for i in a:
		if i.isalpha():
			if isN:
				s += int(n)
				n = ''
				isN = False
			if i.isupper():
				new += i
		elif i.isdigit():
			n += i
			isN = True
		else:
			if isN:
				s += int(n)
				n = '-'
				isN = False
			else:
				n += i
				isN = True
	if isN:
		s += int(n)
	print(new + str(s))

