input()
print(sum(i // 2 + i % 2 for i in list(map(int, input().split()))))