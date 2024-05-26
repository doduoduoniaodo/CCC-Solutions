a = int(input())
b = int(input())
d = b-a
if b <= a:
    print('Congratulations, you are within the speed limit!')
elif 1 <= d and d <= 20:
    print('You are speeding and your fine is $100.')
elif 21 <= d and d <= 30:
    print('You are speeding and your fine is $270.')
else:
    print('You are speeding and your fine is $500.')