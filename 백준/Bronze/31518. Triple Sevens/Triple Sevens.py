n = int(input())
print(777 if sum([1 for _ in range(3) if 7 in list(map(int, input().split()))]) == 3 else 0)