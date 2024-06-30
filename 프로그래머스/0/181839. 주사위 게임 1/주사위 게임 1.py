def solution(a, b):
    if a * b % 2 == 0:
        if (a + b) % 2 == 0:
            answer = abs(a - b)
        else:
            answer = 2 * (a + b)
    else:
        answer = a**2 + b**2
    return answer