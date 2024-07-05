"""
N과 M (4)
"""

def solution():
    # 길이 m의 수열이 완성되었다면, 리스트에서 unpacking하여 출력
    if len(result) == m:
        print(*result)
        return

    for i in range(1, n+1):
        if not visited[i]:
            # 비내림차순 처리
            if result and result[-1] > i:
                continue
            # 현재 원소보다 작은 수에 대한 접근 방지
            visited[i-1] = True
            result.append(i)
            # 다음 원소에 대한 재귀호출
            solution()
            # 이전 상태로 복구
            visited[i-1] = False
            result.pop()


n, m = map(int, input().split())
num = [i for i in range(1, n+1)]
visited = [False for i in range(n+1)]
visited[0] = True
result = []

solution()