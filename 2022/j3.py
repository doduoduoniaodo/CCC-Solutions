a = input()
b = ''
for i in range(len(a)):
    if a[i] == '+':
        b += ' tighten '
    elif a[i] == '-':
        b += ' loosen '
    else:
        b += a[i]
    if i != len(a) - 1:
        if a[i].isdigit() == True and a[i+1].isalpha() == True:
            b += '\n'
print(b)