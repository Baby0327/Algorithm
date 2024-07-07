import heapq

def solution(jobs):
    task = []   # 작업시간이 짧은 작업을 우선으로 처리
    now = 0     # 현재 시간
    count = 0  # 종료된 작업 수
    finish = -1 # 이전 작업이 종료된 시간 (첫 작업 시작을 위해 초기값 음수로 설정)
    time = 0    # 총 대기 시간
    
    while count < len(jobs):
        for i, j in jobs:
            # 현재 시간 이전에 시작하는 작업 중 이전 작업 시작 시간보다 늦게 시작하는 작업 push
            if finish < i <= now:
                heapq.heappush(task, [j, i])    # 소요시간 기준 정렬을 위해 i, j 순서 바꿈
            
        if task:
            now_task = heapq.heappop(task)
            finish = now
            now += now_task[0]
            time += (now - now_task[1])     # 현재 작업을 끝내기까지의 대기시간 반영
            count += 1
        else:
            now += 1
            
    # 소수점을 버린 평균 대기 시간 반환
    return time // len(jobs)