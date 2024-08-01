"""
試験 (Exam)
"""

score = list(map(int, input().split()))
score.remove(min(score))

print(sum(score))