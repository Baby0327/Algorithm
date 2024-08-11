"""
영식이와 친구들
"""

n, m, l = map(int, input().split())
count = {}
result = 0

for i in range(n):
    count[i] = 0

now = 0

while True:
    count[now] += 1
    result += 1

    if count[now] == m:
        break

    if count[now] % 2 == 1:
        now = (now + l) % n
    else:
        now = (now - l) % n

# 시작 부분은 던지는 횟수에 포함되지 않기 때문에 이를 차감하여 출력
print(result - 1)