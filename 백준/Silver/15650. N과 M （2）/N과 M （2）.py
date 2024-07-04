"""
N과 M (2)

인생 첫 백트래킹 문제...!
재귀함수에 익숙해질 필요가 있음을 느낌
"""

def solution():
    # 길이 m의 수열이 완성되었다면, 리스트에서 unpacking하여 출력
    if len(result) == m:
        print(*result)
        return

    for i in range(1, n+1):
        if not visited[i]:
            # 수열 원소에 대한 중복 처리
            if result and result[-1] >= i:
                continue
            visited[i] = True
            result.append(i)
            # 다음 원소에 대한 재귀호출
            solution()
            # 이전 상태로 복구
            visited[i] = False
            result.pop()


n, m = map(int, input().split())
num = [i for i in range(1, n+1)]
visited = [False for i in range(n+1)]
visited[0] = True
result = []

solution()