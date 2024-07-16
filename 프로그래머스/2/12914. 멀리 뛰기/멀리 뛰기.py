# 거리별 멀리뛰기 방법 반환하는 메서드 구현
def fib(n):
    num = [1, 2]
    
    while len(num) < n:
        num.append((num[-1] + num[-2]) % 1234567)
        
    return num[n-1]


def solution(n):
    return fib(n)