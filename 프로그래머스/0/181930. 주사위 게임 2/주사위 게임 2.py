def solution(a, b, c):
    test = sorted([a, b, c])
    answer = a + b + c
    if test[0] == test[1] or test[1] == test[2]:
        answer *= (a**2 + b**2 + c**2)
        if test[0] == test[2]:
            answer *= (a**3 + b**3 + c**3)
    return answer