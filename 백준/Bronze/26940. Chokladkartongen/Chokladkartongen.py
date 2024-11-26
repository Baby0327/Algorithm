n = int(input())
cho = list(map(int, input().split()))
print(sum(1 for i in range(n - 1) if cho[i + 1] > cho[i]))