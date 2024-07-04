def solution(n):
    fib = [0, 1]
    for i in range(n-1):
        fib.append((fib[-2] + fib[-1]) % 1234567)
    return fib[-1]