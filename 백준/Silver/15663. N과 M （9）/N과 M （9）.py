"""
N과 M (9)

알게 된 점 !!!
    - set과 같은 hash를 적용하기 위해서는 immutable한 구조가 필요함
    - list는 mutable하기 때문에 set을 바로 적용할 수 없음
    - 따라서 immutable한 tuple로 변환한 후 set을 적용해야 함
"""

def solution():
    # 길이 m의 수열이 완성되었다면, 리스트에서 unpacking하여 출력
    if len(result) == m:
        temp.append([*result])
        return

    for i in range(1, n+1):
        if not visited[i]:
            visited[i] = True
            result.append(num[i-1])
            # 다음 원소에 대한 재귀호출
            solution()
            # 이전 상태로 복구
            visited[i] = False
            result.pop()


n, m = map(int, input().split())
num = list(map(int, input().split()))
visited = [False for i in range(n+1)]
visited[0] = True
result = []
temp = []

solution()

# list는 mutable하기에 hsahable하지 않으므로 tuple형으로 변환하여 처리
output = sorted(list(set([tuple(i) for i in temp])))

for i in output:
    print(*i)