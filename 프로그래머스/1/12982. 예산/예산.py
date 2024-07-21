def solution(d, budget):
    answer = 0
    
    for i in sorted(d):
        if i <= budget:
            answer += 1
            budget -= i
            
    return answer