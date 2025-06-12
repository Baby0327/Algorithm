def solution(arr):
    answer = []
    i = 0
    
    while i < len(arr):
        if answer and answer[-1] == arr[i]:
            answer.pop()
        else:
            answer.append(arr[i])
        
        i += 1
    
    
    return answer or [-1]