def solution(name, yearning, photo):
    answer = []
    
    for people in photo:
        total = 0
        
        for person in people:
            if person in name:
                total += yearning[name.index(person)]
                
        answer.append(total
                     )
    return answer