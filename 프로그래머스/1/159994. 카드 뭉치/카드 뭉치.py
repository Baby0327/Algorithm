def solution(cards1, cards2, goal):
    i = 0
    while i < len(goal):
        if cards1 and cards1[0] == goal[i]:
            cards1 = cards1[1:]
        elif cards2 and cards2[0] == goal[i]:
            cards2 = cards2[1:]
        else:
            return "No"
        i += 1
        
    return "Yes"