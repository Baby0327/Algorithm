"""
양수 개수 세기
"""

num = list(map(int, input().split()))

print(len([i for i in num if i > 0]))