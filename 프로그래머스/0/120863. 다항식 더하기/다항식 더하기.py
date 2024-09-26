def solution(polynomial):
    s = polynomial.split()
    result = [0, 0]
    answer = ""
    
    for i in s:
        if i != "+":
            if i[-1] == "x":
                result[0] += int(i[:-1]) if len(i) > 1 else 1
            else:
                result[1] += int(i)
    
    if result[0] > 1:
        answer += str(result[0]) + "x"
    elif result[0] == 1:
        answer += "x"
        
    if result[1] > 0:
        if len(answer):
            answer += " + " + str(result[1])
        else:
            answer += str(result[1])
    
    return answer