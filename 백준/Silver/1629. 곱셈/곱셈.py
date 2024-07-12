"""
곱셈

알게 된 점 !!!
    - 첫 분할 정복을 이용한 거듭제곱 문제
    - 재귀호출 어렵다...
    - 모듈러 성질 : (a*b) % c = (a%c * b%c) % c
"""

def solution(b):
    if b == 1:
        return a % c

    if b % 2 == 0:
        return (solution(b // 2) ** 2) % c
    else:
        return ((solution((b - 1) // 2) ** 2) * a) % c


a, b, c = map(int, input().split())
print(solution(b))