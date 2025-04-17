def solution(n):
    answer = 1
    total = 1
    
    while 1:
        total *= answer
        
        if total > n:
            break
        
        answer += 1
    
    return answer - 1