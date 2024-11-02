def solution(n):
    answer = 0
    
    for i in range(1, n + 1):
        now = 0
        for j in range(i, n + 1):
            now += j
            if now == n:
                answer += 1
                break
            elif now > n:
                break
            
    return answer