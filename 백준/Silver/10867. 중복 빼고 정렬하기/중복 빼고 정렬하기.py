"""
중복 빼고 정렬하기
"""

n = int(input())
print(*sorted(set(list(map(int, input().split())))))