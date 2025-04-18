def solution(polynomial):
    answer = [0, 0]
    num = polynomial.split(" + ")
    
    for i in num:
        if "x" in i:
            answer[0] += 1 if len(i) == 1else int(i[:-1])
        else:
            answer[1] += int(i)

    if answer[0] and answer[1]:
        return f"{'' if answer[0] == 1 else answer[0]}x + {answer[1]}"
    elif answer[0]:
        return f"{'' if answer[0] == 1 else answer[0]}x"
    else:
        return f"{answer[1]}"