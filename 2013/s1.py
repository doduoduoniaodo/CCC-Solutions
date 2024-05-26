n = int(input()) + 1
while len(set(str(n))) != len(str(n)):
    n += 1
print(n)


'''
a = int(input()) + 1
def dis(i):
    i = str(i)
    for k in i:
        if i.count(k) > 1:
            return False
    return True
while not dis(a):
    a += 1
print(a)
'''