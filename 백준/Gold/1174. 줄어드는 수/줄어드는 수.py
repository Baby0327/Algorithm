"""
줄어드는 수

개선해야 할 점!!!
    - 백트래킹으로부터 값을 찾는 과정에서 꼭 특정 조건에 따라 return해야 한다는 고정관념을 버리자!!!(완전 비효울적)
"""

def number():
    if temp:
        result.append(int("".join(map(str, temp))))

    for i in range(10):
        if not temp or temp[-1] > num[i]:
            temp.append(num[i])
            number()
            temp.pop()


n = int(input())
num = [i for i in range(9, -1, -1)]
temp = []
result = []
number()
result.sort()

print(result[n-1] if len(result) >= n else -1)