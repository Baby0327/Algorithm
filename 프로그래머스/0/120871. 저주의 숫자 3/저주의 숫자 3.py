def solution(n):
    answer = [0]
    i = 0
    
    while len(answer) <= n:
        i += 1
        
        if i % 3 == 0 or "3" in str(i):
            continue
            
        answer.append(i)
        
    return answer[-1]