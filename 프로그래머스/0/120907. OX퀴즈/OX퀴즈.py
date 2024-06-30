def solution(quiz):
    answer = ["O" if eval(i.replace("=", "==")) else "X" for i in quiz]
    return answer