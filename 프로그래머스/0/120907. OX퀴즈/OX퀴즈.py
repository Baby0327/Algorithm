def solution(quiz):
    answer = []
    
    for i in quiz:
        q, a = i.split(" = ")
        answer.append("O" if eval(q) == int(a) else "X")
    
    return answer