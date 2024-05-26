a = int(input())
b = input()
if b.count('A') > b.count('B'):
    print('A')
elif b.count('A') == b.count('B'):
    print('Tie')
else:
    print('B')