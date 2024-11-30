from collections import Counter

a, b = input(), input()

a_count = Counter(a)
b_count = Counter(b)

wildcards = b_count['*']

for char, count in a_count.items():
    missing = count - b_count.get(char, 0)
    if missing > 0:
        if wildcards < missing:
            print('N')
            break
        wildcards -= missing
else:
    print('A')