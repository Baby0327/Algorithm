def gcd(a, b):
    while b != 0:
        a, b = b, a%b
    
    return a

def solution(n, m):
    num = gcd(n, m)
    
    return [num, n*m // num]