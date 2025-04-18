def solution(numbers, k):
    answer = 0
    l = len(numbers)
    
    for i in range(k - 1):
        answer += 2
        
        if answer >= l:
            answer %= l
        
    return numbers[answer]