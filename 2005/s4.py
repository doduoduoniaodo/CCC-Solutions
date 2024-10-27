for _ in range(int(input())):
    n = int(input())
    a = [input() for _ in range(n)]
    
    current = a[-1]
    d = {current: 0}
    for i in a:
        if i not in d:
            d[i] = d[current] + 1
        current = i
    
    print(n*10 - 2*10*max(d.values()))
