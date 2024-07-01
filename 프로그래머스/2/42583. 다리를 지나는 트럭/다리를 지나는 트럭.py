from collections import deque

def solution(bridge_length, weight, truck_weights):
    # 다리 길이만큼 0으로 초기화한 덱과 트럭 무게를 담은 덱 선언
    bridge = deque([0 for i in range(bridge_length)])
    truck_weights = deque(truck_weights)
    time = 0
    # 현재 다리 무게를 나타낼 변수 선언
    total = 0
    
    while truck_weights:
        time += 1
        total -= bridge.popleft()
        # 현재 트럭이 다리에 진입했을 때의 무게가 제한 하중을 넘지 않을 경우, 진입 허용
        if truck_weights[0] + total <= weight:
            total += truck_weights[0]
            bridge.append(truck_weights.popleft())
        # 제한 하중을 넘을 경우, 대기
        else:
            bridge.append(0)
    
    # 마지막 트럭이 다리에 진입한 후, 다리 길이만큼의 시간이 지나야 완전히 건널 수 있음을 반영
    return time + bridge_length