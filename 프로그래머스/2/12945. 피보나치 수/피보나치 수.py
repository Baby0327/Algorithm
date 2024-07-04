def solution(n):
    fib = [0, 1]
    
    for i in range(n-1):
        # 메모리 효율을 위해 매 계산마다 나머지 계산 포함
        fib.append((fib[-2] + fib[-1]) % 1234567)
        
    return fib[-1]