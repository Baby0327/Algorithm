"""
등차수열에서 항 번호 찾기
"""

a, d, k = map(int, input().split())

print(1 + (k - a) // d if (k - a) % d == 0 and (k - a) // d >= 0 else "X")