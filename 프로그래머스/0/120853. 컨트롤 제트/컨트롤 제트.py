def solution(s):
    answer = []
    
    for i in s.split():
        if i == "Z":
            answer = answer[:-1]
        else:
            answer.append(int(i))
    
    return sum(answer)