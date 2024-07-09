"""
어려운 소인수분해

알게 된 점!!!
    - 에라토스테네스의 체 결과를 True, False로만 표시해야 한다는 편견을 버리자.
"""

import sys

# 에라토스테네스의 체
def prime_number():
    for i in range(2, int(5000001**0.5) + 1):
        if num[i] == i:
            for j in range(i*2, 5000001, i):
                # 한 번도 체크하지 않은 수에 가장 작인 소인수 저장
                if num[j] == j:
                    num[j] = i


# 오름차순으로 소인수분해 결과 출력
def result(test):
    while True:
        if test == 1:
            break
        sys.stdout.write(f"{num[test]} ")
        test //= num[test]


n = int(sys.stdin.readline())
k = list(map(int, sys.stdin.readline().split()))
num = [i for i in range(5000001)]
prime_number()

for i in k:
    result(i)
    sys.stdout.write("\n")