def solution(n):
    answer = 0
    
    for i in range(1, n + 1):
        check = 0
        
        for j in range(2, i):
            if i % j == 0:
                check = 1
                break
        if check:
            answer += 1
    
    return answer