s = input()
c = int(input())
letters = []
numbers = [0]
b = False
last = 0
for i in range(len(s)):
    if s[i].isalpha():
        if i != 0:
            numbers.append(numbers[-1] + int(s[last:i]))
        last = i+1
        letters.append(s[i])
numbers.append(numbers[-1] + int(s[last:]))
    
m = c % numbers[-1]
for i in range(len(numbers)-1):
    if numbers[i] <= m < numbers[i+1]:
        print(letters[i])