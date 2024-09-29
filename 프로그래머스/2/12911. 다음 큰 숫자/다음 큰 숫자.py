def solution(n):
    answer = n + 1
    
    while True:
        temp = bin(answer)
        if bin(n).count("1") == temp.count("1"):
            break
        else:
            answer += 1
            
    return answer