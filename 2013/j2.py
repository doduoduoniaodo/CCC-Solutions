import sys
a = input()
b = ['I', 'O', 'S', 'H', 'Z', 'X', 'N']
for i in a:
    if i not in b:
        print('NO')
        sys.exit()
print('YES')