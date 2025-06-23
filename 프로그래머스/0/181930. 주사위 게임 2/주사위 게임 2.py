def solution(a, b, c):
    num = sorted([a, b, c])
    
    if num[0] == num[2]:
        return (a + b + c) * (a**2 + b**2 + c**2) * (a**3 + b**3 + c**3)
    elif num[0] == num[1] or num[1] == num[2]:
        return (a + b + c) * (a**2 + b**2 + c**2)
    else:
        return a + b + c