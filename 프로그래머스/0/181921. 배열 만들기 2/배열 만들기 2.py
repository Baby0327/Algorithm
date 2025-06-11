def solution(l, r):
    answer = []
    
    for i in range(l, r + 1):
        num = set(map(int, list(str(i))))
        
        if num - {0, 5} == set():
            answer.append(i)
    
    return answer or [-1]