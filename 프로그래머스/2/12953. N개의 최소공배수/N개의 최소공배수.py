def gcd(a, b):
    while b:
        a, b = b, a % b
        
    return a

def result(a, b):
    return a * b // gcd(a, b)

def solution(arr):
    answer = 1
    
    for i in arr:
        answer = result(answer, i)
        
    return answer