"""
언더프라임

!!! 시간초과 발생
    - 원인 
        1. 에라토스테네스의 체를 활용할 때 제한 값인 100000까지의 소수 판별 과정을 거침
        2. 이 결과를 활용하여 소인수분해 과정을 거침
    - 피드백
        1. 필요한 부분에 대해서만 그때그때 에라토스테네스의 체를 활용해도 되는 문제였음.
        2. 소인수분해 과정은 가장 쉽고 직관적으로 구현했어야 함. 너무 어렵게 생각한 것이 문제.
"""


# 소수 판별 함수
def prime(num):
    if num > 1:
        for i in range(2, int(num ** 0.5) + 1):
            if not num % i:
                return False
    else:
        return False
    return True

# 소인수분해 함수
def factorization(num):
    count = 0
    i = 2
    while i  <= num ** 0.5:
        if not num % i:
            num //= i
            count += 1
        else:
            i += 1
    if num != 1:    # 마지막 i에 대한 결과 반영
        count += 1
    return count

# 언더프라임 판별 함수
def underprime(n):
    return prime(factorization(n))


a, b = map(int, input().split())
result = 0

for i in range(a, b + 1):
    if underprime(i):
        result += 1

print(result)