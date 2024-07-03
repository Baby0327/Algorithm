"""
RGB거리

틀린 이유 !!!
    최소금액을 찾는 과정에서 SET을 활용하여 list - list를 구현함
        -> 중복된 비용에 대한 처리가 잘못됨
알게 된 점 !!!
    list + list는 가능하지만 list - list는 불가능함
        -> 이는 set이나 comprehension을 활용하여 구현할 수 있음
"""

import sys

n = int(sys.stdin.readline())
price = []

for i in range(n):
    price.append(list(map(int, sys.stdin.readline().split())))

for i in range(1, n):
    for j in range(3):
        price[i][j] += min(price[i-1][j-1], price[i-1][j-2])

print(min(price[-1]))
