def solution(my_str, n):
    answer = []
    
    for i in range(len(my_str) // n):
        answer.append(my_str[i * n : i * n + n])
    
    if len(my_str) % n:
        answer.append(my_str[(i + 1) * n :])
        
    return answer