def solution(a, b):
    num = sorted([a, b])
    return sum([i for i in range(num[0], num[1] + 1)])