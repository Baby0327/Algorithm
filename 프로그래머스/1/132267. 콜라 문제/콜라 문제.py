def solution(a, b, n):
    count = 0
    
    while n >= a:
        count += (n // a) * b   # 마트로부터 받은 콜라 수
        n = (n % a) + (n // a) * b  # 교환하지 못한 콜라 + 마트로부터 새로 받은 콜라 수
        
    return count