import heapq

def solution(scoville, K):
    food = []
    
    # 최소 힙 생성
    for i in scoville:
        heapq.heappush(food, i)
    
    count = 0
    
    # 최소 힙의 루트값(최솟값)이 K 이상이 될 때까지 반복
    while food[0] < K:
        min1 = heapq.heappop(food)
        min2 = heapq.heappop(food)
        heapq.heappush(food, min1 + (min2 * 2))
        count += 1
        
        # 모든 음식의 스코빌 지수를 K 이상으로 만들 수 없는 경우 처리
        if len(food) == 1 and food[0] < K:
            return -1
        
    return count