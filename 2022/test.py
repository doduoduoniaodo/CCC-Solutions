a = {'A': [1, 2], 'B': [3, 4]}
b = ['A', 'B', 'C']
for i in b:
    for j in a.get(i, []):
        print(j)