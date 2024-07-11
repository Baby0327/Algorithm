"""
줄서기
"""

n = int(input())
ticket = []

for i in range(n):
    ticket += list(input().split())

# 입장 순서 역순으로 정렬
order = sorted(ticket, key=lambda x : (x[:2], int(x[2:])), reverse=True)
wait = []
i = 0

while order:
    if i < (5 * n) and order[-1] == ticket[i]:  # 인덱스 범위 안에 있고, 현재 번호의 입장 순서일 때
        order.pop()
        i += 1
    elif wait and order[-1] == wait[-1]:    # 대기열에 사람이 있고, 우선 대기자가 입장 순서일 때
        wait.pop()
        order.pop()
    else:   # 현재 번호가 입장 순서가 아닐 때
        if i < (5 * n):
            wait.append(ticket[i])
            i += 1
        else:   # 더이상 입장 순서를 맞출 수 없을 때 break
            break

if wait:
    print("BAD")
else:
    print("GOOD")