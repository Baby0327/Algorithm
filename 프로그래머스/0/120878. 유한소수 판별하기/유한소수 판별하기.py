def solution(a, b):
    answer = 0
    i = 2
    
    while i <= a:
        if a % i == 0 and b % i == 0:
            a //= i
            b //= i
        i += 1

    if b % 5 == 0:
        while b % 5 == 0:
            b //= 5
    if b % 2 == 0:
        while b % 2 == 0:
            b //= 2

    return 1 if b == 1 else 2