import heapq

def solution(operations):
    # 최대 힙, 최소 힙 구현 (기본은 최소 힙, 최대 힙은 각 원소에 -를 붙여 구현)
    maxi = []
    mini = []

    for i in operations:
        # 최대 힙에서 최댓값을 pop하고, -를 붙인 값을 최소 힙에서 삭제
        if i == "D 1" :
            if maxi and mini:
                num = heapq.heappop(maxi)
                mini.remove(-num)
                heapq.heapify(mini)     # remove로 깨진 힙 재구조화
        # 최소 힙에서 최솟값을 pop하고, -를 붙인 값을 최소 힙에서 삭제
        elif i == "D -1":
            if maxi and mini:
                num = heapq.heappop(mini)
                maxi.remove(-num)
                heapq.heapify(maxi)     # remove로 깨진 힙 재구조화
        # 최소 힙에 push, 최대 힙에 - 붙인 값을 push
        else:
            heapq.heappush(maxi, -int(i[2:]))
            heapq.heappush(mini, int(i[2:]))
            
    # 힙이 비었으면 [0, 0], 그렇지 않으면 각 힙에서 최댓값과 최솟값을 찾아 반환
    return [-maxi[0], mini[0]] if maxi and mini else [0, 0]

