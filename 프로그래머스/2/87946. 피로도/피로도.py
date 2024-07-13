from itertools import permutations

def solution(k, dungeons):
    answer = 0
    
    # 순열을 통해 모든 조합 찾고, 이를 모두 탐색하며 최대 결과값 찾기
    for case in permutations(dungeons, len(dungeons)):
        now = k
        count = 0
        
        for i, j in case:
            if i <= now:
                now -= j
                count += 1
                
        answer = max(answer, count)
        
    return answer
