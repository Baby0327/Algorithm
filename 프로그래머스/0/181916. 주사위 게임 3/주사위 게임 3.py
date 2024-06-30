def solution(a, b, c, d):
    num = len(set([a, b, c, d]))
    dice = sorted([a, b, c, d])
    if num == 1:
        answer = 1111 * dice[0]
    elif num == 2:
        if dice[0] == dice[2]:
            answer = (10 * dice[0] + dice[3])**2
        elif dice[1] == dice[3]:
            answer = (10 * dice[3] + dice[0])**2
        else:
            answer = (dice[1] + dice[2]) * abs(dice[1] - dice[2])
    elif num == 3:
        if dice[0] == dice[1]:
            answer = dice[2] * dice[3]
        elif dice[1] == dice[2]:
            answer = dice[0] * dice[3]
        else:
            answer = dice[0] * dice[1]
    else:
        answer = dice[0]
        
    return answer