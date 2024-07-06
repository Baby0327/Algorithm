"""
N과 M (12)
"""

def solution():
    # 길이 m의 수열이 완성되었다면, 리스트에서 unpacking하여 출력
    if len(result) == m:
        print(*result)
        return

    # 중복 처리를 위한 변수 선언
    check = 0

    for i in range(1, n+1):
        # 같은 값을 가진 원소에 대한 중복 처리
        if not visited[i] and num[i-1] != check:
            # 비내림차순 처리
            if result and result[-1] > num[i-1]:
                continue
            visited[i-1] = True
            result.append(num[i-1])
            check = num[i-1]
            # 다음 원소에 대한 재귀호출
            solution()
            # 이전 상태로 복구
            visited[i-1] = False
            result.pop()


n, m = map(int, input().split())
num = sorted(list(map(int, input().split())))
visited = [False for i in range(n+1)]
visited[0] = True
result = []

solution()