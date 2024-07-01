def solution(participant, completion):
    
    # 동명이인 처리를 위해 이름별 참가자 수 저장
    player = {}
    for i in participant:
        if i not in player:
            player[i] = 1
        else:
            player[i] += 1
    
    # 완주한 선수 이름은 딕셔너리에서 삭제
    for i in completion:
        player[i] -= 1
        if player[i] == 0:
            del player[i]
        
    return list(player.keys())[0]