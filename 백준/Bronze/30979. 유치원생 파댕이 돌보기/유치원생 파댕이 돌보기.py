"""
유치원생 파댕이 돌보기
"""

t = int(input())
n = int(input())
taste = list(map(int, input().split()))

result = "Happy" if sum(taste) >= t else "Cry"

print(f"Padaeng_i {result}")