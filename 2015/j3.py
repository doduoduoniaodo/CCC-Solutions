alphabet = 'abcdefghijklmnopqrstuvwxyz'
consonant = 'bcdfghjklmnpqrstvwxyz'
vowel = {'a': 0, 'e': 4, 'i': 8, 'o': 14, 'u': 20}
a = input()
ans = ''
for i in range(len(a)):
    ans += a[i]
    if a[i] != 'a' and a[i] != 'e' and a[i] != 'i' and a[i] != 'o' and a[i] != 'u':
        ind = alphabet.find(a[i])
        ind_c = consonant.find(a[i])
        mia = abs(ind-vowel['a'])
        mie = abs(ind-vowel['e'])
        mii = abs(ind-vowel['i'])
        mio = abs(ind-vowel['o'])
        miu = abs(ind-vowel['u'])
        mi = min(mia, mie, mii, mio, miu)
        if mi == mia:
            ans += 'a'
        elif mi == mie:
            ans += 'e'
        elif mi == mii:
            ans += 'i'
        elif mi == mio:
            ans += 'o'
        else:
            ans += 'u'
        if a[i] != 'z':
            ans += consonant[ind_c+1]
        else:
            ans += 'z'
print(ans)