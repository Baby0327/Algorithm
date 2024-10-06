def solution(bandage, health, attacks):
    answer = health
    index = 0
    time = 1
    bonus = 0
    
    while time <= attacks[-1][0]:
        if attacks[index][0] == time:
            answer -= attacks[index][1]
            bonus = 0
            index += 1
            if answer <= 0:
                answer = -1
                break
        else:
            answer += bandage[1]
            bonus += 1
            if bonus == bandage[0]:
                answer += bandage[2]
                bonus = 0
            if answer > health:
                answer = health
        time += 1
            
    return answer