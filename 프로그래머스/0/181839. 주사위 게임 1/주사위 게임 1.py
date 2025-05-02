def solution(a, b):
    case = sum([int(a % 2), int(b % 2)])
    
    if case == 2:
        return a**2 + b**2
    elif case == 1:
        return 2 * (a + b)
    else:
        return abs(a - b)