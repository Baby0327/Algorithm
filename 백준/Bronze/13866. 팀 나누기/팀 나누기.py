level = list(map(int, input().split()))
level.sort()
result1 = level[0] + level[3]
result2 = level[1] + level[2]
print(max(result1, result2) - min(result1, result2))