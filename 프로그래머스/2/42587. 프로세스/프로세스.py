from collections import deque

def solution(priorities, location):
    # 프로세스 인덱스와 중요도를 담은 2차원 배열을 덱으로 저장
    process = deque([[i, p] for i, p in enumerate(priorities)])
    count = 0
    
    while True:
        # 현재 실행 대기 큐의 최전방에 있는 프로세스가 가장 우선순위가 높은 프로세스라면, 제거하고 실행횟수 +1
        if process[0][1] == max([i[1] for i in process]):
            i, p = process.popleft()
            count += 1
            # 현재 실행한 프로세스가 알고 싶은 프로세스라면 반복문 종료
            if i == location:
                break
        # 그렇지 않으면, process를 좌측으로 1칸 회전
        else:
            process.rotate(-1)
            
    return count