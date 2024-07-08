"""
이중 우선순위 큐

알게 된 점 !!!
    - 삭제할 특정 원소를 매번 heap에서 remove한 후, heapify(재구조화)하는 것은 비효율적(시간초과 발생)
    - 삭제해야 하는 원소를 관리할 list를 선언하여, 최솟값과 최댓값에 영향이 있는 원소만 그때그때 pop하는 것이 효율적
"""

import sys
import heapq


def solution(k, operations):
    # 최대 힙, 최소 힙 구현 (기본은 최소 힙, 최대 힙은 각 원소에 -를 붙여 구현)
    maxi = []
    mini = []
    visited = [False] * k

    for i in range(k):
        # "D"로 시작하는 연산의 경우, 삭제할 원소 표시
        if operations[i] == "D 1":
            if maxi:
                visited[maxi[0][1]] = False

        elif operations[i] == "D -1":
            if mini:
                visited[mini[0][1]] = False
        # 최소 힙에 그대로, 최대 힙에 - 붙인 값을 index(i)와 함께 push
        else:
            visited[i] = True
            heapq.heappush(maxi, [-int(operations[i][2:]), i])
            heapq.heappush(mini, [int(operations[i][2:]), i])

        # 삭제할 원소가 최댓값, 최솟값에 영향을 줄 경우, 힙에서 삭제
        while mini and not visited[mini[0][1]]:
            heapq.heappop(mini)

        while maxi and not visited[maxi[0][1]]:
            heapq.heappop(maxi)

    # 힙이 비었으면 "EMPTY", 그렇지 않으면 각 힙에서 최댓값과 최솟값을 찾아 출력
    if mini:
        sys.stdout.write(str(-maxi[0][0]) + " " + str(mini[0][0]) + "\n")
    else:
        sys.stdout.write("EMPTY\n")



t = int(sys.stdin.readline())

for i in range(t):
    k = int(sys.stdin.readline())
    operations = []

    for j in range(k):
        operations.append(sys.stdin.readline().strip())

    solution(k, operations)