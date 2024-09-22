"""
모든 순열

!!! 알게 된 점 !!!
    - L10에서  list와 list[:]의 차이를 잊어 오류 발생
    - list는 값이 계속 변하기에 참조만 추가할 경우 그에 따라 값도 변하는 현상이 발생함
    - 이를 예방하기 위해 참조인 list가 아닌 값 그 자체인 list[:](복사본)을 저장해야 함
"""

def back():
    if len(list) == n:
        result.append(list[:])
        return

    for i in range(1, n+1):
        if not visited[i]:
            visited[i] = True
            list.append(i)
            back()
            visited[i] = False
            list.pop()

result = []
n = int(input())
visited = [False] * (n + 1)
list = []
back()
result.sort()

for i in result:
    print(*i)