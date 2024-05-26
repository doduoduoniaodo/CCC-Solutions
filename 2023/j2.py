a = int(input())
b = []
for i in range(a):
    b.append(input())
    
c = 0
for j in range(a):
    if b[j] == 'Poblano':
        c += 1500
    elif b[j] == 'Mirasol':
        c += 6000
    elif b[j] == 'Serrano':
        c += 15500
    elif b[j] == 'Cayenne':
        c += 40000
    elif b[j] == 'Thai':
        c += 75000
    elif b[j] == 'Habanero':
        c += 125000
    

print(c)
