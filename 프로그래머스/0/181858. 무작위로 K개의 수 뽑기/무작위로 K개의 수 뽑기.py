def solution(arr, k):
    answer = []
    i = 0
    
    while i < len(arr):
        if arr[i] not in answer:
            answer.append(arr[i])
        
        if len(answer) == k:
            break
        
        i += 1
        
    return answer + [-1] * (k - len(answer))