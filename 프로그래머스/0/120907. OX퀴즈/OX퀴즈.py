def solution(quiz):
    answer = []
    
    for i in quiz:
        now = i.split()
        if now[1] == "+":
            if int(now[0]) + int(now[2]) == int(now[4]):
                answer.append("O")
            else:
                answer.append("X")
        else:
            if int(now[0]) - int(now[2]) == int(now[4]):
                answer.append("O")
            else:
                answer.append("X")
        
    return answer