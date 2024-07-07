"""
통나무 건너뛰기

알게 된 점 !!!
    - 실제 통나무를 배치한 list를 직접 구현하지 않고,
      2칸 차이의 원소가 인접 원소가 됨을 활용하여 시간을 줄임
"""

import sys

t = int(sys.stdin.readline())
for i in range(t):
    n = int(sys.stdin.readline())
    log = sorted(list(map(int, sys.stdin.readline().split())), reverse=True)

    maxi = 0

    for i in range(2, n):
        # 정렬한 list에서 2칸 차이의 원소가 실제 인접 원소가 됨을 반영하여 최댓값 찾기
        maxi = max(maxi, abs(log[i-2] - log[i]))

    sys.stdout.write(str(maxi) + "\n")
