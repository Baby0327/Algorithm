def solution(ingredient):
    answer = 0
    temp = []
    
    for i in ingredient:
        temp.append(i)
        if i == 1 and len(temp) >= 4 and temp[-4:] == [1, 2, 3, 1]:
            temp.pop()
            temp.pop()
            temp.pop()
            temp.pop()
            answer += 1
            
    return answer