"""
감소하는 수
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

print(result[n] if len(result) > n else -1)