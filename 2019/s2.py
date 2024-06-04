import sys
input = sys.stdin.readline

def is_prime(n):
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

for _ in range(int(input())):
    n = int(input())
    for i in range(3, 2*n, 2):
        b = 2 * n - i
        if is_prime(i) and is_prime(b):
            if i + b == 2 * n:
                print(i, b)
                break
    