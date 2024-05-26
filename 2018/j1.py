a = [input() for _ in range(4)]
if a[0] == '8' or a[0] == '9': 
    if a[1] == a[2]: 
        if a[3] == '8' or a[3] == '9': print('ignore')
if a[0] != '8' and a[0] != '9': print('answer')
elif a[1] != a[2]: print('answer')
elif a[3] != '8' and a[3] != '9': print('answer')