def solution(arr, queries):
    answer = []
    
    for s, e, k in queries:
        num = sorted([arr[i] for i in range(s, e + 1) if arr[i] > k])
        
        if num:
            answer.append(num[0])
        else:
            answer.append(-1)
        
    return answer