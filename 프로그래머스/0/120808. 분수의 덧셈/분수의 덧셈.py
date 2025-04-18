def solution(numer1, denom1, numer2, denom2):
    num1 = numer1 * denom2 + numer2 * denom1
    num2 = denom1 * denom2
    
    for i in range(min(num1, num2), 1, -1):
        if num1 % i == 0 and num2 % i == 0:
            num1 //= i
            num2 //= i
    
    return [num1, num2]