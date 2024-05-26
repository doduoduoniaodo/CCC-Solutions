while True:
    line = input()
    if line == '0': break
    a = line.split()
    stk = []
    for i in range(len(a)-1, -1, -1):
        if a[i].isdigit():
            stk.append(a[i])
        else:
            op1 = stk.pop()
            op2 = stk.pop()
            stk.append(op1 + ' ' + op2 + ' ' + a[i])
    print(stk.pop())