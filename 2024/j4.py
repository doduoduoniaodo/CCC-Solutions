a, b = input(), input()
sa, sb = set(a), set(b)
common = sb.intersection(sa)

for i in common:
    sa.remove(i)
    sb.remove(i)

if len(sa) == 1:
    print(*sa, *sb)
    print('-')
else:
    sa, sb = list(sa), list(sb)
    
    a2 = a.replace(sa[0], sb[0])
    a2 = a2.replace(sa[1], '')
    
    a3 = a.replace(sa[1], sb[0])
    a3 = a3.replace(sa[0], '')
    
    if a2 == b:
        print(sa[0], sb[0])
        print(sa[1])
    else:
        print(sa[1], sb[0])
        print(sa[0])