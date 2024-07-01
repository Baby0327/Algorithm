from collections import deque

def solution(prices):
    price = deque(prices)
    result = []   
    
    while price:
        # 현재 주식 가격을 popleft함
        now = price.popleft()
        result.append(0)
        for i in price:
            # 현재 주식 가격이 얼만큼 떨어지지 않는지 파악하고, 현재 주식 가격보다 낮은 가격이 있을 경우 break
            result[-1] += 1
            if i < now:
                break
    
    return result