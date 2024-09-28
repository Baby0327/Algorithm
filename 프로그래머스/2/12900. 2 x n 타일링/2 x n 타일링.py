def solution(n):
    answer = [0, 1, 2]
    
    for i in range(n - 1):
        answer.append((answer[-1] + answer[-2]) % 1000000007)
        
    return answer[n]