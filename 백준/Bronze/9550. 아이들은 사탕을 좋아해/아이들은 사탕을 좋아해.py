"""
아이들은 사탕을 좋아해
"""

t = int(input())

for i in range(t):
    n, k = map(int, input().split())
    candy = list(map(int, input().split()))
    child = sum(i//k for i in candy)

    print(child)