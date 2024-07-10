def solution(n):
    num = 2
    while n % num != 1:
        num += 1
    return num