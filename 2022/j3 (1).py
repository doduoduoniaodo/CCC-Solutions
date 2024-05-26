a = input()
s = False
o = ''
for i in range(len(a)):
    if s:
        if a[i].isalpha():
            s = False
            print(o)
            o = ''
    if a[i] == '+':
        s = True
        o += ' tighten '
    elif a[i] == '-':
        s = True
        o += ' loosen '
    else:
        o += a[i]
print(o)   