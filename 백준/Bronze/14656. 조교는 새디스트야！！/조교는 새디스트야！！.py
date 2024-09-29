"""
조교는 새디스트야!!
"""

n = int(input())
now = list(map(int, input().split()))
correct = sorted(now)

print(sum([1 for i in range(n) if now[i] != correct[i]]))